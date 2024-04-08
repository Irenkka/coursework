import unittest
from server import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_health(self):
        response = self.app.get('/health_check')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '"Server Running"\n')

    def test_birthday_success(self):
        months = ["January", "February", "March"]
        department = 'Finance'
        for month in months:
            response = self.app.get(f'/birthdays?month={month}&department={department}')
            self.assertEqual(response.status_code, 200)
            response_str: str = response.data.decode()
            self.assertTrue("employees" in response_str)
            self.assertTrue("total" in response_str)
    
    def test_birthday_no_month(self):
        response = self.app.get(f'/birthdays?department=Finance')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Missing 'month' parameter")

    def test_birthday_no_department(self):
        response = self.app.get(f'/birthdays?month=January')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Missing 'department' parameter")

    def test_birthday_no_correct_params(self):
        response = self.app.get(f'/birthdays')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Missing 'department' and 'month' parameter")

    def test_anniversary_success(self):
        months = ["January", "February", "March"]
        department = 'Finance'
        for month in months:
            response = self.app.get(f'/anniversaries?month={month}&department={department}')
            self.assertEqual(response.status_code, 200)
            response_str: str = response.data.decode()
            self.assertTrue("employees" in response_str)
            self.assertTrue("total" in response_str)
    
    def test_anniversary_no_month(self):
        response = self.app.get(f'/anniversaries?department=Finance')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Missing 'month' parameter")

    def test_anniversary_no_department(self):
        response = self.app.get(f'/anniversaries?month=January')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Missing 'department' parameter")

    def test_anniversary_no_correct_params(self):
        response = self.app.get(f'/anniversaries')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.decode(), "Missing 'department' and 'month' parameter")


if __name__ == '__main__':
    unittest.main()