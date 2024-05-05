import http

import pytest


@pytest.mark.anyio
async def test_arxiv_client_fixture_can_be_queried(arxiv_client):
    response = await arxiv_client.get(
        "/api/query?search_query={query}&skip=0&max_results=8&sortBy=relevance&sortOrder=descending"
    )
    assert response.status_code == http.HTTPStatus.OK
    assert response.text != ""


@pytest.mark.anyio
async def test_arxiv_facade_can_be_queried(arxiv):
    response = await arxiv._query("llm")
    assert response.status_code == http.HTTPStatus.OK
    assert response.text != ""


@pytest.mark.anyio
async def test_arxiv_facade_response_equals_direct_get_request(arxiv, arxiv_client):
    query = "llm"
    response = await arxiv_client.get(
        f"/api/query?search_query={query}&skip=0&max_results=8&sortBy=relevance&sortOrder=descending"
    )
    facade_response = await arxiv._query(query=query)
    assert response.text == facade_response.text


@pytest.mark.anyio
async def test_get_author_query_from_arxiv_of_length_10(arxiv):
    author = "A. Del Maestro"
    query = await arxiv.query(author=author, max_query_results=10)
    assert len(query.articles) == 10
