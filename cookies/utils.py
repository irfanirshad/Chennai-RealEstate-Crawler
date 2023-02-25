import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By

class CookiesService:
    """
    Handles all the cookies service methods
    """
    def save_cookie(driver):
        """Saves the cookies of the driver"""
        create_cookie_button = driver.find_element(By.ID, "createCookie")
        create_cookie_button.click()

        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))


    def load_cookie(driver):
        """Loads the cookies of the driver"""
        with open("cookies.pkl", "rb") as f:
            cookie = pickle.load(f)[0]

        driver.add_cookie(
            {'expiry': cookie["expiry"], 'name': cookie["name"], 'value': cookie["value"]})
        
    
    def check_for_cookies(driver):
        """Checks if the driver has cookies"""
        return len(driver.get_cookies()) > 0