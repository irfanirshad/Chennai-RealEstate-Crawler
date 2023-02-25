import unittest
from utils import *


class CookieTest(unittest.TestCase):
    def setUp(self):
        self.driver = initiate_chrome_driver()
        self.driver.get("http://localhost:3000/")
        load_cookie(self.driver)
        self.driver.refresh()

    def test_load_cookie(self):
        """
        Checks if the status is correct after loading a cookie.
        """
        status = self.driver.find_element(By.ID, "statusText")
        self.assertEqual(status.text, "You are authenticated!")

    def test_delete_cookie(self):
        """
        Checks if the status is correct after deleting a cookie.
        """

        self.driver.delete_all_cookies()
        self.driver.refresh()
        status = self.driver.find_element(By.ID, "statusText")
        self.assertEqual(status.text, "You are NOT authenticated")

    def test_add_cookie_if_not_present(self):
        """
        Checks if the status is correct after adding a cookie.
        """
        self.driver.delete_all_cookies()
        self.driver.refresh()

        if not check_for_cookies(self.driver):
            load_cookie(self.driver)
            self.driver.refresh()

        status = self.driver.find_element(By.ID, "statusText")
        self.assertEqual(status.text, "You are authenticated!")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)