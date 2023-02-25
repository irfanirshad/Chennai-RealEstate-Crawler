import unittest
from utils import *


class SearchElements(unittest.TestCase):
    def setUp(self):
        self.driver = initiate_chrome_driver()
        self.driver.get("http://localhost:3000/")
        self.driver.delete_all_cookies()

    def test_create_cookie_button(self):
        """
        Checks if the create cookie button is present.
        """
        create_cookie_button = self.driver.find_element(By.ID, "createCookie")
        self.assertTrue(create_cookie_button.is_displayed())

    def test_delete_cookie_button(self):
        """
        Checks if the delete cookie button is present.
        """
        delete_cookie_button = self.driver.find_element(By.ID, "deleteCookie")
        self.assertTrue(delete_cookie_button.is_displayed())

    def test_check_initial_cookie_status(self):
        """
        Checks if the initial status is correct.
        """
        status = self.driver.find_element(By.ID, "statusText")
        self.assertEqual(status.text, "You are NOT authenticated")

    def test_cookie_status_after_create(self):
        """
        Checks if the status is correct after creating a cookie.
        """
        create_cookie_button = self.driver.find_element(By.ID, "createCookie")
        create_cookie_button.click()
        status = self.driver.find_element(By.ID, "statusText")
        self.assertEqual(status.text, "You are authenticated!")

    def test_cookie_status_after_delete(self):
        """
        Checks if the status is correct after deleting a cookie.
        """
        create_cookie_button = self.driver.find_element(By.ID, "createCookie")
        create_cookie_button.click()
        status = self.driver.find_element(By.ID, "statusText")
        self.assertEqual(status.text, "You are authenticated!")

        delete_cookie_button = self.driver.find_element(By.ID, "deleteCookie")
        delete_cookie_button.click()
        status = self.driver.find_element(By.ID, "statusText")
        self.assertEqual(status.text, "You are NOT authenticated")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)