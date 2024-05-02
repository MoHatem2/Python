import unittest
import requests 

class TestAPIValidation(unittest.TestCase):

    def test_index_route(self):
        response = requests.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    # Add more API validation test cases for other routes as needed

if __name__ == '_main_':
    unittest.main()