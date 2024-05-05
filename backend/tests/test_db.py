import http

import pytest

from app.models import Article, Author, Query


@pytest.mark.anyio
async def test_author_creation(session):
    author = Author(**{"name": "Max Mustermann"})
    assert author.id is None
    session.add(author)
    await session.commit()
    await session.refresh(author)
    assert author.id == 1


@pytest.mark.anyio
async def test_article_creation(session):
    author = Author(**{"name": "Max Mustermann"})
    coauthor = Author(**{"name": "Max Mustermann2"})
    coauthors = [author, coauthor]
    article_data = {
        "title": "Very important paper",
        "journal": "Physics",
        "summary": "Summary",
        "author": author,
        "coauthors": coauthors,
    }
    article = Article(**article_data)
    assert article.id is None
    session.add(article)
    await session.commit()
    await session.refresh(article, ["author", "coauthors"])
    assert article.id == 1
    assert article.author == author
    assert article.coauthors == coauthors


@pytest.mark.anyio
async def test_query_creation(session):
    author = Author(**{"name": "Max Mustermann"})
    coauthor = Author(**{"name": "Max Mustermann2"})
    coauthors = [author, coauthor]
    article_data = {
        "title": "Very important paper",
        "journal": "Physics",
        "summary": "Summary",
        "author": author,
        "coauthors": coauthors,
    }
    article = Article(**article_data)
    query_data = {
        "query": 'au:"Mustermann"',
        "articles": [article],
        "status": http.HTTPStatus.OK.value,
        "num_results": 1,
    }
    query = Query(**query_data)
    assert query.id is None
    session.add(query)
    await session.commit()
    await session.refresh(query)
    assert query.id == 1
