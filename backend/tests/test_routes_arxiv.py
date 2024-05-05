import http


def test_arxiv_search_route_contains_articles(client, session):
    response = client.get("/v1/arxiv/search?author=A.%20Del%20Maestro&max_query_results=10")
    query = response.json()
    assert "articles" in query.keys()
    assert query["articles"]  # is not empty


def test_arxiv_search_route_with_empty_search(client, session):
    response = client.get("/v1/arxiv/search")
    query = response.json()
    assert query["num_results"] == 0
    assert query["status"] == http.HTTPStatus.BAD_REQUEST.value
