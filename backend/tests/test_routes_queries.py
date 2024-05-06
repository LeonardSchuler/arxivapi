import datetime
import http

import pytest

from app.models import Article, Author, Query


# TODO: split into multiple tests
@pytest.mark.anyio
async def test_queries_route(session, client):
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
    query1 = Query(**query_data, timestamp=datetime.datetime(2024, 5, 5, 15, 3, 19))
    query2 = Query(**query_data, timestamp=datetime.datetime(2024, 5, 5, 15, 21, 6))
    session.add(query1)
    session.add(query2)
    await session.commit()

    start = "2024-05-05T15:01:29"
    start_encoded = start.replace(":", "%3A")
    end = "2024-05-05T15:05:02"
    end_encoded = end.replace(":", "%3A")

    # include both start and end and expect all queries
    response = client.get(
        f"v1/queries/?query_timestamp_start={start_encoded}&query_timestamp_end={end_encoded}"
    )
    queries = response.json()
    assert len(queries) == 1
    assert queries[0]["timestamp"] == "2024-05-05T15:03:19"

    # no end, still expect both
    response = client.get(f"v1/queries/?query_timestamp_start={start_encoded}")
    queries = response.json()
    assert len(queries) == 2

    # skip first no end by using end date as start
    response = client.get(f"v1/queries/?query_timestamp_start={end_encoded}")
    queries = response.json()
    assert len(queries) == 1
    assert queries[0]["timestamp"] == "2024-05-05T15:21:06"

    # find no queries by setting start and end the same
    response = client.get(
        f"v1/queries/?query_timestamp_start={start_encoded}&query_timestamp_end={start_encoded}"
    )
    queries = response.json()
    assert len(queries) == 0
