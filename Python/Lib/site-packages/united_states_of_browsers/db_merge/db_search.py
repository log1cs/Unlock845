import sqlite3
from datetime import datetime as dt

from united_states_of_browsers.db_merge import helpers
from united_states_of_browsers.db_merge.imported_annotations import *


def check_fts5_installed():
    with sqlite3.connect(':memory:') as con:
        cur = con.cursor()
        cur.execute('pragma compile_options;')
        available_pragmas = cur.fetchall()
    if ('ENABLE_FTS5',) in available_pragmas:
        return True
    else:
        return False


def _make_sql_statement(word_query: Optional[Text],
                        date_start: Union[int, None],
                        date_stop: Union[int, None]
                        ) -> Union[Text, Iterable[Text]]:
    """ Returns prepared SQL statements and bindings for queries with and without dates.
    If no args provided, returns a search query which will select all records.
        Optional: word_query, date_start and date_stop.
    """
    if not word_query:
        sql_query = (
            ' SELECT *'
            ' FROM search_table'
            ' WHERE last_visit BETWEEN ? AND ?'
        )
        query_bindings = [date_start, date_stop]
    else:
        sql_query = (
                ' SELECT * FROM search_table'
                ' WHERE last_visit BETWEEN ? AND ?'
                ' AND search_table'
                ' MATCH ? ORDER BY bm25(search_table, 0, 0, 7, 9, 0, 0, 0, 0, 0)'
        )
        query_bindings = [date_start, date_stop, word_query, ]
    return sql_query, query_bindings


def _run_search(db_ref: PathInfo, sql_query: Text, query_bindings: Iterable[Text]
                ) -> Iterable[NamedTuple]:
    """ Returns the search results as a list of NamedTuples of records.
    Accepts --
    db_path: database file path,
    sql_query: a formed SQL query,
    query_bindings: list of attributes for the query.
    """
    try:
        query_results = db_ref.execute(sql_query, query_bindings)
    except AttributeError:
        with sqlite3.connect(str(db_ref)) as sink_conn:
            sink_conn.row_factory = sqlite3.Row
            query_results = sink_conn.execute(sql_query, query_bindings)
    return query_results


def search(db_path: PathInfo,
           word_query: Optional[Text]='',
           date_start: Optional[Text]=None,
           date_stop: Optional[Text]=None,
           ) -> Iterable[NamedTuple]:
    """ Returns the search result as a list of NamedTuple of records.
    Accepts database file path and optionally, keywords and date range.

    Optional:
        word_query: if None (default), not included in search filter.
        date_start: if None(default), the earliest date is used.
        date_stop: if None (default), the present date is used.
    """
    if not date_start:
        date_start = int(dt.timestamp(dt.strptime('1970-01-02', '%Y-%m-%d')) * 10**6)
    else:
        date_start = int(dt.timestamp(dt.strptime(date_start, '%Y-%m-%d')) * 10**6)
    if not date_stop:
        date_stop = int(dt.utcnow().timestamp() * 10 ** 6)
    else:
        date_stop = int(dt.timestamp(dt.strptime(date_stop, '%Y-%m-%d')) * 10**6)
    word_query = helpers.query_sanitizer(word_query, allowed_chars=[' ', '%', '(', ')', '_'])
    sql_query, query_bindings = _make_sql_statement(word_query, date_start, date_stop)
    search_results = _run_search(db_path, sql_query, query_bindings)
    return search_results
