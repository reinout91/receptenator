import requests
import unittest

class SimpleTest(unittest.TestCase):

    def test_title(self):
        self.assertEqual('Receptenator', requests.get('http://127.0.0.1:8000').json())

    def test_recepten(self):
        self.assertEqual(200, requests.get('http://127.0.0.1:8000/recepten').status_code)

    def test_randomrecept(self):
        self.assertEqual(200, requests.get('http://127.0.0.1:8000/randomrecept').status_code)

if __name__ == '__main__':
    unittest.main()