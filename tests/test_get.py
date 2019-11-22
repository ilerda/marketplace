'''
Unit testing script for get method
Make sure you run:
python3 app.py
first!!
'''

import unittest
from subprocess import check_output

class GetRequestMethod(unittest.TestCase):

    def test_ok_response(self):

        full_response = check_output(['curl', '-i',
            '-X', 'GET', 'http://127.0.0.1:5000/v1/products'])
        resp_code = str(full_response)[11:14]
        self.assertEqual(resp_code, '200')

if __name__ == '__main__':
    unittest.main()
