import unittest
from unittest.mock import MagicMock
from kintone.commands.record import Record


class TestRecord(unittest.TestCase):
    def setUp(self):
        self.http_request = MagicMock()
        self.record = Record(self.http_request)

    def test_get(self):
        app_id = 123
        record_id = 456
        self.http_request.get.return_value = {'success': True}
        response = self.record.get(app_id, record_id)
        self.http_request.get.assert_called_with('/k/v1/record.json', {'app': app_id, 'id': record_id})
        self.assertEqual(response, {'success': True})

    def test_create(self):
        app_id = 123
        record_data = {'field1': 'value1'}
        self.http_request.post.return_value = {'id': 789}
        response = self.record.create(app_id, record_data)
        self.http_request.post.assert_called_with('/k/v1/record.json', {'app': app_id, 'record': record_data})
        self.assertEqual(response, {'id': 789})

    def test_register(self):
        app_id = 123
        record_data = {'field2': 'value2'}
        self.http_request.post.return_value = {'id': 890}
        response = self.record.register(app_id, record_data)
        self.http_request.post.assert_called_with('/k/v1/record.json', {'app': app_id, 'record': record_data})
        self.assertEqual(response, {'id': 890})

    def test_update(self):
        app_id = 123
        record_id = 456
        record_data = {'field3': 'value3'}
        self.http_request.put.return_value = {'revision': 2}
        response = self.record.update(app_id, record_id, record_data)
        self.http_request.put.assert_called_with('/k/v1/record.json',
                                                 {'app': app_id, 'id': record_id, 'record': record_data})
        self.assertEqual(response, {'revision': 2})
