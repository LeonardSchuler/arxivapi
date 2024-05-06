import datetime
import http

import pytest

from app.models import Article, Author, Query


# TODO: split into multiple tests
@pytest.mark.anyio
async def test_queries_route(session, client):
    # generate a query with 10 articles
    author = Author(**{"name": "Max Mustermann"})
    coauthor = Author(**{"name": "Max Mustermann2"})
    coauthors = [author, coauthor]

    def article_generator(i: int) -> Article:
        article_data = {
            "title": f"Very important paper number {i}",
            "journal": "Physics",
            "summary": "Summary",
            "author": author,
            "coauthors": coauthors,
        }
        article = Article(**article_data)
        return article

    query_data = {
        "query": 'au:"Mustermann"',
        "articles": [article_generator(i) for i in range(1, 11)],
        "status": http.HTTPStatus.OK.value,
        "num_results": 10,
    }
    query = Query(**query_data, timestamp=datetime.datetime(2024, 5, 5, 15, 3, 19))
    session.add(query)
    await session.commit()

    # get page 1 with 4 items per page given 10 articles
    response = client.get("v1/results/?query_id=1&page=1&items_per_page=4")
    articles = response.json()
    assert len(articles) == 4
    assert articles[0]["title"] == "Very important paper number 1"
    assert articles[3]["title"] == "Very important paper number 4"

    # get page 2 with 4 items per page given 10 articles
    response = client.get("v1/results/?query_id=1&page=2&items_per_page=4")
    articles = response.json()
    assert len(articles) == 4
    assert articles[0]["title"] == "Very important paper number 5"
    assert articles[3]["title"] == "Very important paper number 8"

    # get page 3 with 4 items per page given 10 articles
    response = client.get("v1/results/?query_id=1&page=3&items_per_page=4")
    articles = response.json()
    assert len(articles) == 2
    assert articles[0]["title"] == "Very important paper number 9"
    assert articles[1]["title"] == "Very important paper number 10"
