from kintone.commands.space import Space
from unittest.mock import Mock


def test_get_space():
    space_id = 456
    expected_response = {'name': 'Test Space'}
    http_request_mock = Mock()
    http_request_mock.get.return_value = expected_response

    space_instance = Space(http_request=http_request_mock)
    response = space_instance.get(space_id)

    http_request_mock.get.assert_called_with('/k/v1/space.json', {'id': space_id})
    assert response == expected_response
