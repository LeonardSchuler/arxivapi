from app.remotes.arxiv import QueryBuilder


def test_empty_author_query():
    query = QueryBuilder().author("").build()
    assert query == ""


def test_author_query():
    query = QueryBuilder().author("A. Del Maestro").build()
    assert query == 'au:"A. Del Maestro"'


def test_author_query_with_empty_journal_only_contains_the_author():
    query = QueryBuilder().author("A. Del Maestro").journal("").build()
    assert query == 'au:"A. Del Maestro"'


def test_journal_query():
    query = QueryBuilder().journal("Phys. Rev. B 74, 214517 (2006)").build()
    assert query == 'jr:"Phys. Rev. B 74, 214517 (2006)"'


def test_title_query():
    title = "A striped supersolid phase and the search for deconfined quantum criticality in hard-core bosons on the triangular lattice"
    query = QueryBuilder().title(title).build()
    assert query == f'ti:"{title}"'


def test_author_and_title_query():
    author = "A. Del Maestro"
    title = "A striped supersolid phase and the search for deconfined quantum criticality in hard-core bosons on the triangular lattice"
    query = QueryBuilder().author(author).title(title).build()
    assert query == f'au:"{author}" AND ti:"{title}"'
