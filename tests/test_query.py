import pytest
from kintone.query import Query

query_with_field_equal = [
    (Query().field('text').equal('test').build(), "text = \"test\""),
    (Query().field('作成日時').equal(Query.now()).build(), "作成日時 = NOW()"),
    (Query().field('作成日時').equal(Query.today()).build(), "作成日時 = TODAY()"),
    (Query().field('作成日時').equal(Query.this_year()).build(), "作成日時 = THIS_YEAR()"),
    (Query().field('作成日時').equal(Query.this_month()).build(), "作成日時 = THIS_MONTH()"),
    (Query().field('作成日時').equal(Query.last_month()).build(), "作成日時 = LAST_MONTH()"),
    (Query().field('number').equal(100).build(), "number = 100"),
]


@pytest.mark.parametrize("query, expected", query_with_field_equal)
def test_query_with_field_equal(query, expected):
    assert query == expected


query_with_field_not_equal = [
    (Query().field('text').not_equal('test').build(), "text != \"test\""),
    (Query().field('作成日時').not_equal(Query.now()).build(), "作成日時 != NOW()"),
    (Query().field('作成日時').not_equal(Query.today()).build(), "作成日時 != TODAY()"),
    (Query().field('作成日時').not_equal(Query.this_year()).build(), "作成日時 != THIS_YEAR()"),
    (Query().field('作成日時').not_equal(Query.this_month()).build(), "作成日時 != THIS_MONTH()"),
    (Query().field('作成日時').not_equal(Query.last_month()).build(), "作成日時 != LAST_MONTH()"),
    (Query().field('number').not_equal(100).build(), "number != 100"),
]


@pytest.mark.parametrize("query, expected", query_with_field_not_equal)
def test_query_with_field_not_equal(query, expected):
    assert query == expected


query_with_field_greater_than = [
    (Query().field('text').greater_than('test').build(), "text > \"test\""),
    (Query().field('作成日時').greater_than(Query.now()).build(), "作成日時 > NOW()"),
    (Query().field('作成日時').greater_than(Query.today()).build(), "作成日時 > TODAY()"),
    (Query().field('作成日時').greater_than(Query.this_year()).build(), "作成日時 > THIS_YEAR()"),
    (Query().field('作成日時').greater_than(Query.this_month()).build(), "作成日時 > THIS_MONTH()"),
    (Query().field('作成日時').greater_than(Query.last_month()).build(), "作成日時 > LAST_MONTH()"),
    (Query().field('number').greater_than(100).build(), "number > 100"),
]


@pytest.mark.parametrize("query, expected", query_with_field_greater_than)
def test_query_with_field_greater_than(query, expected):
    assert query == expected


query_with_field_less_than = [
    (Query().field('text').less_than('test').build(), "text < \"test\""),
    (Query().field('作成日時').less_than(Query.now()).build(), "作成日時 < NOW()"),
    (Query().field('作成日時').less_than(Query.today()).build(), "作成日時 < TODAY()"),
    (Query().field('作成日時').less_than(Query.this_year()).build(), "作成日時 < THIS_YEAR()"),
    (Query().field('作成日時').less_than(Query.this_month()).build(), "作成日時 < THIS_MONTH()"),
    (Query().field('作成日時').less_than(Query.last_month()).build(), "作成日時 < LAST_MONTH()"),
    (Query().field('number').less_than(100).build(), "number < 100"),
]


@pytest.mark.parametrize("query, expected", query_with_field_less_than)
def test_query_with_field_less_than(query, expected):
    assert query == expected


query_with_field_greater_than_or_equal = [
    (Query().field('text').greater_than_or_equal('test').build(), "text >= \"test\""),
    (Query().field('作成日時').greater_than_or_equal(Query.now()).build(), "作成日時 >= NOW()"),
    (Query().field('作成日時').greater_than_or_equal(Query.today()).build(), "作成日時 >= TODAY()"),
    (Query().field('作成日時').greater_than_or_equal(Query.this_year()).build(), "作成日時 >= THIS_YEAR()"),
    (Query().field('作成日時').greater_than_or_equal(Query.this_month()).build(), "作成日時 >= THIS_MONTH()"),
    (Query().field('作成日時').greater_than_or_equal(Query.last_month()).build(), "作成日時 >= LAST_MONTH()"),
    (Query().field('number').greater_than_or_equal(100).build(), "number >= 100"),
]


@pytest.mark.parametrize("query, expected", query_with_field_greater_than_or_equal)
def test_query_with_field_greater_than_or_equal(query, expected):
    assert query == expected


query_with_field_less_than_or_equal = [
    (Query().field('text').less_than_or_equal('test').build(), "text <= \"test\""),
    (Query().field('作成日時').less_than_or_equal(Query.now()).build(), "作成日時 <= NOW()"),
    (Query().field('作成日時').less_than_or_equal(Query.today()).build(), "作成日時 <= TODAY()"),
    (Query().field('作成日時').less_than_or_equal(Query.this_year()).build(), "作成日時 <= THIS_YEAR()"),
    (Query().field('作成日時').less_than_or_equal(Query.this_month()).build(), "作成日時 <= THIS_MONTH()"),
    (Query().field('作成日時').less_than_or_equal(Query.last_month()).build(), "作成日時 <= LAST_MONTH()"),
    (Query().field('number').less_than_or_equal(100).build(), "number <= 100"),
]


@pytest.mark.parametrize("query, expected", query_with_field_less_than_or_equal)
def test_query_with_field_less_than_or_equal(query, expected):
    assert query == expected


query_with_field_in = [
    (Query().field('dropdown').in_(['test1', 'test2']).build(), 'dropdown in ("test1", "test2")'),
    (Query().field('dropdown').in_([100, 'test2']).build(), 'dropdown in (100, "test2")'),
    (Query().field('dropdown').in_([100]).build(), 'dropdown in (100)'),
    (Query().field('作成者').in_([Query.login_user()]).build(), '作成者 in (LOGINUSER())'),
]


@pytest.mark.parametrize("query, expected", query_with_field_in)
def test_query_with_field_in(query, expected):
    assert query == expected


query_with_field_not_in = [
    (Query().field('dropdown').not_in(['test1', 'test2']).build(), 'dropdown not in ("test1", "test2")'),
    (Query().field('dropdown').not_in([100, 'test2']).build(), 'dropdown not in (100, "test2")'),
    (Query().field('dropdown').not_in([100]).build(), 'dropdown not in (100)'),
    (Query().field('作成者').not_in([Query.login_user()]).build(), '作成者 not in (LOGINUSER())'),
]


@pytest.mark.parametrize("query, expected", query_with_field_not_in)
def test_query_with_field_not_in(query, expected):
    assert query == expected


query_with_field_like = [
    (Query().field('status').like('test').build(), 'status like "test"'),
]


@pytest.mark.parametrize("query, expected", query_with_field_like)
def test_query_with_field_like(query, expected):
    assert query == expected


query_with_field_not_like = [
    (Query().field('status').not_like('test').build(), 'status not like "test"'),
]


@pytest.mark.parametrize("query, expected", query_with_field_not_like)
def test_query_with_field_not_like(query, expected):
    assert query == expected


def test_query_with_logical_and():
    query = Query().field('status').equal('test').and_().field('type').equal('bug').build()
    assert query == "status = \"test\" and type = \"bug\""


def test_query_with_logical_or():
    query = Query().field('status').equal('test').or_().field('type').equal('bug').build()
    assert query == "status = \"test\" or type = \"bug\""


def test_query_with_precede():
    query = Query().precede(
        Query().field('status').equal('test').and_().field('type').equal('bug')
    ).or_().precede(
        Query().field('status').equal('development')
    ).build()
    assert query == "(status = \"test\" and type = \"bug\") or (status = \"development\")"


def test_query_with_function():
    query = Query().field('created_time').greater_than_or_equal(Query.now()).build()
    assert query == "created_time >= NOW()"


query_with_order_by = [
    (Query().order_by('status').build(), "order by status asc"),
    (Query().order_by('status', 'asc').build(), "order by status asc"),
    (Query().order_by('status', 'desc').build(), "order by status desc"),
]


@pytest.mark.parametrize("query, expected", query_with_order_by)
def test_query_with_order_by(query, expected):
    assert query == expected


query_with_limit = [
    (Query().limit(10).build(), "limit 10"),
    (Query().limit("10").build(), "limit 10"),
]


@pytest.mark.parametrize("query, expected", query_with_limit)
def test_query_with_limit(query, expected):
    assert query == expected


query_with_offset = [
    (Query().offset(20).build(), "offset 20"),
    (Query().offset("20").build(), "offset 20"),
]


@pytest.mark.parametrize("query, expected", query_with_offset)
def test_query_with_offset(query, expected):
    assert query == expected
