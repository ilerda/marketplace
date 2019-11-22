'''
Unit testing script for post and delete methods
Make sure you run:
python3 app.py
first!!
'''

import unittest
from subprocess import check_output

class GetRequestMethod(unittest.TestCase):

    def test_ok_create(self):

        full_response = check_output(['curl', '-i',
            '-X', 'POST', '-H', 'Content-Type: application/json',
            '-d', '{"name": "test_item", "price": "100.75"}',
            'http://127.0.0.1:5000/v1/product/7'])
        resp_code = str(full_response)[11:14]
        self.assertEqual(resp_code, '200')

    def test_ok_delete(self):

        full_response = check_output(['curl', '-i',
            '-X', 'DELETE',
            'http://127.0.0.1:5000/v1/product/7'])
        resp_code = str(full_response)[11:14]
        self.assertEqual(resp_code, '200')

if __name__ == '__main__':
    unittest.main()
