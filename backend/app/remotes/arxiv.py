import http
import logging
from typing import Any, AsyncGenerator, Self

import feedparser
import httpx

from app.exceptions import RemoteNotAvailableException
from app.models import ArticleCreate, AuthorCreate, QueryCreate


logger = logging.getLogger(__name__)


ARXIV_API_BASE_URL = "https://export.arxiv.org"
PATH_TEMPLATE = "/api/query?search_query={query}&skip={skip}&max_results={max_results}&sortBy={sort_by}&sortOrder={sort_order}"


class QueryBuilder:
    """Creates a simple builder API to create arxiv queries. Query components are joined using 'AND'.
    Note that url encoding is not handled here.
    Details: https://info.arxiv.org/help/api/user-manual.html#51-details-of-query-construction
    """

    def __init__(self):
        self._query = []

    def build(self):
        return " AND ".join(self._query)

    def _add_query_component(self, prefix: str, value: str) -> None:
        if not value:
            return
        # elif len(value) > 256:
        #    raise ValueError(f"{value} exceeds maximum length of 256 characters")
        self._query.append(f'{prefix}:"{value}"')

    def author(self, author: str) -> Self:
        self._add_query_component("au", author)
        return self

    def title(self, title: str) -> Self:
        self._add_query_component("ti", title)
        return self

    def journal(self, journal: str) -> Self:
        self._add_query_component("jr", journal)
        return self


class ArxivApi:
    def __init__(self, client: None | httpx.AsyncClient = None):
        if client is None:
            client = httpx.AsyncClient(base_url=ARXIV_API_BASE_URL)
        self._client = client

    async def _query(
        self,
        query: str,
        skip: int = 0,
        max_results: int = 8,
        sort_by: str = "relevance",
        sort_order: str = "descending",
    ) -> httpx.Response:
        # TODO: Implement paging + 3s wait to reduce the load on arxiv
        path = PATH_TEMPLATE.format(
            query=query, skip=skip, max_results=max_results, sort_by=sort_by, sort_order=sort_order
        )
        full_url = str(self._client.base_url) + path
        logger.info(f"GET {full_url}")
        response = await self._client.get(path)
        return response

    def validate_response(self, response: httpx.Response):
        status = response.status_code
        if status != http.HTTPStatus.OK:
            raise RemoteNotAvailableException("arxiv")

    def to_feed(self, response: httpx.Response) -> dict[str, Any]:
        feedparser.mixin._FeedParserMixin.namespaces[
            "http://a9.com/-/spec/opensearch/1.1/"
        ] = "opensearch"
        # add arxiv namespace to _FeedParserMixin.namespace under key 'arxiv', which defines the arXiv Atom feed
        feedparser.mixin._FeedParserMixin.namespaces["http://arxiv.org/schemas/atom"] = "arxiv"
        # parse response content
        feed = feedparser.parse(response.content)
        if feed.bozo:
            logger.warning("Parsed malformed XML successfully.")
        return feed

    def to_query_result(self, feed: dict[str, Any]) -> QueryCreate:
        """
        >>> feed.keys()
        dict_keys(['bozo', 'entries', 'feed', 'headers', 'encoding', 'version', 'namespaces'])
        >>> # feed["entries"]: list[dict[str, Any]]
        >>> feed["entries"][0].keys()
        dict_keys(['id', 'guidislink', 'link', 'updated', 'updated_parsed', 'published', 'published_parsed', 'title', 'title_detail', 'summary', 'summary_detail', 'authors', 'author_detail', 'author', 'arxiv_doi', 'links', 'arxiv_comment', 'arxiv_journal_ref', 'arxiv_primary_category', 'tags'])
        >>> feed["entries"][0]["arxiv_journal_ref"]
        'Physical Review B 88, 064512 (2013)'
        >>> feed["entries"][0]["title"]
        'Local Superfluidity at the Nanoscale'
        >>> feed["entries"][0]["authors"]
        [{'name': 'B. Kulchytskyy'}, {'name': 'G. Gervais'}, {'name': 'A. Del Maestro'}]
        >>> feed["entries"][0]["author_detail"]
        {'name': 'A. Del Maestro'}
        >>> feed["feed"].keys()
        dict_keys(['links', 'title', 'title_detail', 'id', 'guidislink', 'link', 'updated', 'updated_parsed', 'opensearch_totalresults', 'opensearch_startindex', 'opensearch_itemsperpage'])
        >>> from pprint import pprint
        >>> pprint(feed["feed"])
        {'guidislink': True,
         'id': 'http://arxiv.org/api/nRLM9eDdevfkqTi73OBL1i1CPDU',
         'link': 'http://arxiv.org/api/nRLM9eDdevfkqTi73OBL1i1CPDU',
         'links': [{'href': 'http://arxiv.org/api/query?search_query%3Dau%3A%22A.%20Del%20Maestro%22%26id_list%3D%26start%3D0%26max_results%3D10',
                    'rel': 'self',
                    'type': 'application/atom+xml'}],
         'opensearch_itemsperpage': '10',
         'opensearch_startindex': '0',
         'opensearch_totalresults': '12',
         'title': 'ArXiv Query: search_query=au:"A. Del '
                  'Maestro"&amp;id_list=&amp;start=0&amp;max_results=10',
         'title_detail': {'base': '',
                          'language': None,
                          'type': 'text/html',
                          'value': 'ArXiv Query: search_query=au:"A. Del '
                                   'Maestro"&amp;id_list=&amp;start=0&amp;max_results=10'},
         'updated': '2024-05-04T00:00:00-04:00',
         'updated_parsed': time.struct_time(tm_year=2024, tm_mon=5, tm_mday=4, tm_hour=4, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=125, tm_isdst=0)}

        Args:
            feed (dict[str, Any]): Contains the parsed XML result from the arxiv endpoint

        Returns:
            Query: _description_
        """
        articles = []
        for raw_article in feed.get("entries", []):
            author_data = raw_article["author_detail"]
            author = AuthorCreate(**author_data)
            # Prevent duplicate creation of author in coauthors
            coauthors = [
                AuthorCreate(**cad) for cad in raw_article["authors"] if cad != author_data
            ]
            coauthors.append(author)
            article_data = {
                "title": raw_article["title"],
                "journal": raw_article.get("arxiv_journal_ref", ""),
                "summary": raw_article.get("summary", ""),
                "author_name": author.name,
                "author": author,
                "coauthors": coauthors,
            }
            article = ArticleCreate(**article_data)
            articles.append(article)
        query_data = {
            "query": feed["feed"]["title"],
            "articles": articles,
            "status": http.HTTPStatus.OK.value,
            "num_results": feed["feed"]["opensearch_totalresults"],
        }
        query_result = QueryCreate(**query_data)
        return query_result

    async def query(
        self, author: str = "", title: str = "", journal: str = "", max_query_results: int = 8
    ) -> QueryCreate:
        query = QueryBuilder().author(author).title(title).journal(journal).build()
        response = await self._query(query=query, max_results=max_query_results)
        self.validate_response(response)
        feed = self.to_feed(response)
        query_result = self.to_query_result(feed)
        return query_result


async def get_arxiv() -> AsyncGenerator[ArxivApi, None]:
    async with httpx.AsyncClient(base_url=ARXIV_API_BASE_URL) as client:
        arxiv = ArxivApi(client)
        yield arxiv
