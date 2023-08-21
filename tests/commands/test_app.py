from kintone.commands.app import App
from unittest.mock import Mock


def test_get_app():
    app_id = 123
    expected_response = {'name': 'Test App'}
    http_request_mock = Mock()
    http_request_mock.get.return_value = expected_response

    app_instance = App(http_request=http_request_mock)
    response = app_instance.get(app_id)

    http_request_mock.get.assert_called_with('/k/v1/app.json', {'id': app_id})
    assert response == expected_response
