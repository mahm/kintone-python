import unittest
from unittest.mock import MagicMock
from kintone.commands.records import Records


class TestRecords(unittest.TestCase):
    def setUp(self):
        self.http_request = MagicMock()
        self.records = Records(self.http_request)

    def test_get(self):
        app_id = 123
        query = "field = value"
        fields = ['field1', 'field2']
        self.http_request.get.return_value = {'success': True}
        response = self.records.get(app_id, query, fields, True)
        self.http_request.get.assert_called_with('/k/v1/records.json', {'app': app_id, 'query': query, 'fields': fields,
                                                                        'totalCount': 'true'})
        self.assertEqual(response, {'success': True})

    def test_create(self):
        app_id = 123
        records_data = [{'field': 'value'}]
        self.http_request.post.return_value = {'ids': [456]}
        response = self.records.create(app_id, records_data)
        self.http_request.post.assert_called_with('/k/v1/records.json', {'app': app_id, 'records': records_data})
        self.assertEqual(response, {'ids': [456]})

    def test_register(self):
        app_id = 123
        records_data = [{'field': 'value2'}]
        self.http_request.post.return_value = {'ids': [789]}
        response = self.records.register(app_id, records_data)
        self.http_request.post.assert_called_with('/k/v1/records.json', {'app': app_id, 'records': records_data})
        self.assertEqual(response, {'ids': [789]})

    def test_update(self):
        app_id = 123
        records_data = [{'id': 1, 'field': 'value3'}]
        self.http_request.put.return_value = {'records': [1]}
        response = self.records.update(app_id, records_data)
        self.http_request.put.assert_called_with('/k/v1/records.json', {'app': app_id, 'records': records_data})
        self.assertEqual(response, {'records': [1]})

    def test_delete(self):
        app_id = 123
        ids = [1, 2]
        revisions = [3, 4]
        self.http_request.delete.return_value = {'success': True}
        response = self.records.delete(app_id, ids, revisions)
        self.http_request.delete.assert_called_with('/k/v1/records.json',
                                                    {'app': app_id, 'ids': ids, 'revisions': revisions})
        self.assertEqual(response, {'success': True})
