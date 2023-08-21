from io import BytesIO

import pytest
from contextlib import contextmanager
from unittest.mock import patch
from kintone.http_request import HttpRequest

# 認証情報と期待されるヘッダー
auth_params = [
    ({'user': 'username', 'password': 'password'}, {'X-Cybozu-Authorization': 'dXNlcm5hbWU6cGFzc3dvcmQ='}),
    ({'token': 'xxxxxx'}, {'X-Cybozu-API-Token': 'xxxxxx'}),
    ({'token': ['xxxxxx', 'yyyyyy', 'zzzzzz']}, {'X-Cybozu-API-Token': 'xxxxxx,yyyyyy,zzzzzz'}),
]


@contextmanager
def mock_file_content(*args, **kwargs):
    file_content = b'file_content'
    yield BytesIO(file_content)


@pytest.mark.parametrize("auth,expected_header", auth_params)
@patch('kintone.http_request.urllib3.PoolManager')
def test_get(mock_pool_manager, auth, expected_header):
    http_instance = mock_pool_manager.return_value
    http_instance.request.return_value.data.decode.return_value = '{"success": true}'
    client = HttpRequest(domain='example.kintone.com', **auth)
    response = client.get('/test')
    http_instance.request.assert_called_with('GET', 'https://example.kintone.com/test', headers=expected_header,
                                             fields=None)
    assert response == {'success': True}


@pytest.mark.parametrize("auth,expected_header", auth_params)
@pytest.mark.parametrize("method_name,http_verb,kwargs,expected_kwargs", [
    ('post', 'POST', {'body': {'key': 'value'}}, {'body': {'key': 'value'}}),
    ('delete', 'DELETE', {'params': {'id': 1}}, {'fields': {'id': 1}})  # paramsをfieldsに変更
])
@patch('kintone.http_request.urllib3.PoolManager')
def test_post_and_delete(mock_pool_manager, method_name, http_verb, auth, expected_header, kwargs, expected_kwargs):
    http_instance = mock_pool_manager.return_value
    http_instance.request.return_value.data.decode.return_value = '{"success": true}'
    client = HttpRequest(domain='example.kintone.com', **auth)
    method = getattr(client, method_name)
    response = method('/test', **kwargs)
    http_instance.request.assert_called_with(http_verb, 'https://example.kintone.com/test', headers=expected_header,
                                             **expected_kwargs)  # expected_kwargsを使用
    assert response == {'success': True}


@pytest.mark.parametrize("auth,expected_header", auth_params)
@patch('kintone.http_request.urllib3.PoolManager')
def test_post_file(mock_pool_manager, auth, expected_header):
    with patch('builtins.open', mock_file_content, create=True):
        http_instance = mock_pool_manager.return_value
        http_instance.request.return_value.data.decode.return_value = '{"success": true}'
        client = HttpRequest(domain='example.kintone.com', **auth)
        response = client.post_file('/test', file_path='path/to/file.txt')
        http_instance.request.assert_called_with('POST', 'https://example.kintone.com/test', headers=expected_header,
                                                 body=b'file_content')
        assert response == {'success': True}
