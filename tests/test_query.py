import pytest
from kintone.query import Query


def test_query_with_field_equal():
    query = Query().field('status').equal('test').build()
    assert query == "status = \"test\""


def test_query_with_field_not_equal():
    query = Query().field('status').not_equal('test').build()
    assert query == "status != \"test\""


def test_query_with_field_greater_than():
    query = Query().field('status').greater_than('test').build()
    assert query == "status > \"test\""


def test_query_with_field_less_than():
    query = Query().field('status').less_than('test').build()
    assert query == "status < \"test\""


def test_query_with_field_greater_than_or_equal():
    query = Query().field('status').greater_than_or_equal('test').build()
    assert query == "status >= \"test\""


def test_query_with_field_less_than_or_equal():
    query = Query().field('status').less_than_or_equal('test').build()
    assert query == "status <= \"test\""


def test_query_with_field_in():
    query = Query().field('status').in_(['test1', 'test2']).build()
    assert query == "status in (\"test1\", \"test2\")"


def test_query_with_field_not_in():
    query = Query().field('status').not_in(['test1', 'test2']).build()
    assert query == "status not in (\"test1\", \"test2\")"


def test_query_with_field_like():
    query = Query().field('status').like('test').build()
    assert query == "status like \"test\""


def test_query_with_field_not_like():
    query = Query().field('status').not_like('test').build()
    assert query == "status not like \"test\""


def test_query_with_logical_and():
    query = Query().field('status').equal('test').and_().field('type').equal('bug').build()
    assert query == "status = \"test\" and type = \"bug\""


def test_query_with_logical_or():
    query = Query().field('status').equal('test').or_().field('type').equal('bug').build()
    assert query == "status = \"test\" or type = \"bug\""


def test_query_with_precede():
    query = Query().precede(
        Query().field('status').equal('test').and_().field('type').equal('bug')
    ).build()
    assert query == "(status = \"test\" and type = \"bug\")"


def test_query_with_function():
    query = Query().field('created_time').greater_than_or_equal(Query.now()).build()
    assert query == "created_time >= NOW()"


def test_query_with_order_by():
    query = Query().order_by('status', 'desc').build()
    assert query == "order by status desc"


def test_query_with_limit():
    query = Query().limit(10).build()
    assert query == "limit 10"


def test_query_with_offset():
    query = Query().offset(20).build()
    assert query == "offset 20"
