from tokenize import String
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pandas as pd
from collections import defaultdict
import re
import time 
import xlsxwriter
import os

COUNT_PRIME = 0

URL_MAP = {
    'url_login': "https://accounts.magicbricks.com/userauth/login",
    'url_main': "https://www.magicbricks.com/property-for-rent/commercial-real-estate?bedroom=&proptype=Commercial-Office-Space,Office-ITPark-SEZ&cityName=West-area-Chennai"
}

class MagicBricksService(object):
    """MagicBricksService Scraping Service"""
    def __init__(self):
        self.driver = None
        self.listing_list1= defaultdict(list)
        self.final_listing_list = []
        self.prime_set = set(String)

    def set_options(self):
        """Options for selenium.webdriver"""
        option = webdriver.ChromeOptions()
        chrome_prefs = {}
        option.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = { "popups": 1 }

    def launch_driver(self):
        """Spawns the webdriver and returns the object"""
        self.driver = webdriver.Chrome('/usr/local/Caskroom/chromedriver/99.0.4844.51/chromedriver', chrome_options=self.set_options())
        return self.driver

    def login_page_redirect(self):
        """Goes to MB login page"""
        self.driver.get(URL_MAP["url_login"])
        time.sleep(4)
        self.driver.implicitly_wait(4)

    def login_complete(self):
        """
        Completes the whole login process which consists of:
            1) Visiting the login specified URL 
            2) Filling in the login details
            3) Clicking the login button
        """
        self.login_page_redirect()
        
        username = os.environ.get('USERNAME')
        password = os.environ.get('PASS')
        user_button = self.driver.find_element(By.XPATH, '//*[@id="emailOrMobile"]')
        user_button.send_keys(username)
        time.sleep(1)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="btnStep1"]')
        next_button.click()
        time.sleep(2)
        passwd_button = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        passwd_button.send_keys(password)
        time.sleep(2)
        self.driver.implicitly_wait(2)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="btnLogin"]')
        login_button.click()
        time.sleep(2)
        self.driver.implicitly_wait(2)

    def setup_filters(self):
        """Fills in the filters on the specified url"""
        self.driver.get(URL_MAP['url_main'])
        self.driver.implicitly_wait(3)
        time.sleep(4)
        link = self.driver.find_element(By.XPATH, '//*[@id="body"]/div[1]/div/div[2]/div[5]/div/div[1]')
        link.click()
        time.sleep(4)  
        link1 = self.driver.find_element(By.XPATH, '//*[@id="moreFilter_11"]/div[2]/div[1]/label')
        link1.click()
        time.sleep(2)
        self.driver.implicitly_wait(2)

    def adjust_sqft_slider(self):
        """Adjust slider"""
        min_btn = self.driver.find_element(By.XPATH, '//*[@id="moreFilter_0"]/div[2]/div/div/div/div[1]/div[1]/select')
        select = Select(min_btn)
        time.sleep(1)
        try:
            select.select_by_visible_text("500")
        except NoSuchElementException:
            print("ERROR EXCEPTION-Drop Down doesnt exist") # TODO: use logger instead
        time.sleep(2)

    def view_properties(self):
        """Clicks view properties"""
        view_button = self.driver.find_element(By.XPATH, '//*[@id="moreRefined"]/div[3]/div/div[2]')
        view_button.click()
        time.sleep(3)
        self.driver.implicitly_wait(3)

    def bot_minimize(self):
        """Minimizes the chat bot popup window before scrolling else it glitches out"""
        bot_minimize = self.driver.find_element(By.XPATH, '//*[@id="bot-container"]/div[1]/a[1]')
        bot_minimize.click()
        time.sleep(2)
        self.driver.implicitly_wait(2)

    def scroll_till_end(self):
        """Scrolls till end of page. Be patient here."""
        previous_height = self.driver.execute_script('return document.body.scrollHeight')
        while True:
            time.sleep(5)
            self.driver.implicitly_wait(7)
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(7)
            self.driver.implicitly_wait(7)
            new_height = self.driver.execute_script('return document.body.scrollHeight')
            time.sleep(7)
            self.driver.implicitly_wait(7)
            try:
                self.bot_minimize()
            except:
                pass
            if new_height == previous_height:
                break 
            time.sleep(7)
            self.driver.implicitly_wait(7)
            previous_height = new_height
            time.sleep(7)
            self.driver.implicitly_wait(7)
        print("End of scroll reached") # TODO: use logger instead
        self.driver.implicitly_wait(7)
        time.sleep(3)

    def select_all_cards(self):
        """Selects all listing cards in the page to be processed"""
        self.total_mb_srp__lists = self.driver.find_elements(By.CLASS_NAME, 'mb-srp__list')
        time.sleep(8)
        self.driver.implicitly_wait(10)

    def prime_seperator(self, list, card_id):
        """Seperates the prime cards from the total list of cards"""
        #text = list.find_element(By.XPATH, '//*[@id="{0}"]/div/div[2]/div[2]/a').format(card_id)
        #mb-srp__card__pe-info
        self.driver.implicitly_wait(2)
        try:
            self.driver.implicitly_wait(2)
            if(list.find_element(By.CLASS_NAME, "mb-srp__card__exclusive-prop")) != 0:
                self.driver.implicitly_wait(2)
                self.prime_set.add(card_id)
                self.driver.implicitly_wait(3)
                COUNT_PRIME = COUNT_PRIME + 1
        except:
            self.driver.implicitly_wait(3)
            print("not a prime")
            self.driver.implicitly_wait(2)
        self.driver.implicitly_wait(2)

    def process_card_chunks(self, list, len_list, card_id):
        """Processes the card into chunks and returns them as a list"""
        self.driver.implicitly_wait(2)
        r = re.findall('(\d+)', card_id)
        r1 = r[0]
        owner_name = list.find_element(By.XPATH, f'//*[@id="{card_id}"]/div/div[1]/div[1]/div[2]/div').text
        self.driver.implicitly_wait(2)
        price = list.find_element(By.XPATH, f'//*[@id="{card_id}"]/div/div[2]/div[1]/div[1]').text
        self.driver.implicitly_wait(2)
        address = list.find_element(By.XPATH, f'//*[@id="{card_id}"]/div/div[1]/div[2]/h2').text 
        self.driver.implicitly_wait(2)
        #description = list.find_element(By.XPATH, f'//*[@id="{card_id}"]/div/div[1]/div[2]/div[6]/div').text 
        self.driver.implicitly_wait(2)
        info_1 = {
            'CARD_ID': card_id
        }
        info_2 = {
            'OWNER' : owner_name
        }
        info_3 = {
            'PRICE': price
        }
        info_4 = {
            'ADDRESS': address
        }

        # find if "Read more" button exists. If it does, click and extract info. Else, just extract the raw text and ignore all else.
        # Check if the said property isn't a MB-prime . If it is , it will open pop up windows
        self.driver.implicitly_wait(2)
        
        try:
            if(list.find_element(By.CLASS_NAME, "mb-srp__card--desc--readmore")) != 0:
                self.driver.implicitly_wait(2)
                if card_id in self.prime_set:
                    self.driver.implicitly_wait(2)
                    description = list.find_element(By.CLASS_NAME, "mb-srp__card--desc--text").text
                    info_5 = {
                        'Description-MB-prime': description
                    }
                else:
                    self.driver.implicitly_wait(2)
                    read_more = list.find_element(By.CLASS_NAME, "mb-srp__card--desc--readmore") 
                    read_more.click() # click READ MORE first
                    description = list.find_element(By.CLASS_NAME, "mb-srp__card--desc--text").text # now extract the description
                    info_5 = {
                    'DESCRIPTION_full': description
                    }   
        except:
            description = list.find_element(By.CLASS_NAME, "mb-srp__card--desc--text").text
            info_5 = {
                'Description_less': description
            }
        
        # Check is MB-prime or not first b4 clicking on "Read More".
        #if(prime_seperator(list)) is False: 
        
        listing_list1= defaultdict(list)
        self.driver.implicitly_wait(2)
        listing_list1[card_id].append(info_1)
        self.driver.implicitly_wait(2)
        listing_list1[card_id].append(info_2)
        self.driver.implicitly_wait(2)
        listing_list1[card_id].append(info_3)
        self.driver.implicitly_wait(2)
        listing_list1[card_id].append(info_4)
        self.driver.implicitly_wait(2)
        listing_list1[card_id].append(info_5)
        self.driver.implicitly_wait(2)
        for i in range(1,len_list+1):
            self.driver.implicitly_wait(2)
            title = list.find_element(By.XPATH,f'//*[@id="propertiesAction{r1}"]/div/div[{i}]/div[1]').text
            self.driver.implicitly_wait(2)
            text = list.find_element(By.XPATH,f'//*[@id="propertiesAction{r1}"]/div/div[{i}]/div[2]').text
            self.driver.implicitly_wait(2)
            #print(title, text)
            listing_item = {
                title: text
            }
            self.driver.implicitly_wait(1)
            listing_list1[card_id].append(listing_item.copy())
            self.driver.implicitly_wait(1)
            #assemble(title, text) # goto function which assembles data to be stored
            #store_csv(title, text) # Use this function to store into a xls format
        self.driver.implicitly_wait(2)
        self.final_listing_list.append(listing_list1[card_id])
        self.driver.implicitly_wait(2)

    def process_all_cards(self):
        """Processes all the cards one by one and returns a final dictionary"""
        for list in self.total_mb_srp__lists:
            card_id = list.get_attribute('id')
        print(card_id)
        self.driver.implicitly_wait(2)
        self.prime_seperator(list, card_id)
        self.driver.implicitly_wait(4)
        
        try:
            self.driver.implicitly_wait(2)
            how_many = list.find_elements(By.CLASS_NAME, 'mb-srp__card__summary-commercial__list--item')
            self.driver.implicitly_wait(2)
            len_list = len(how_many)
            self.driver.implicitly_wait(2)
            self.process_card_chunks(list, len_list, card_id)
            self.driver.implicitly_wait(2)
        except:
            print("Error...Moving on..") # TODO use a logger instead here
            self.driver.implicitly_wait(2)
        self.driver.implicitly_wait(1)

    def LoggingDriver(self, logger=None):
        """Saves all logging information to loggers before terminating the driver"""
        print("COUNT of PRIME IS ===>", COUNT_PRIME) # TODO: use a logger instead here
        # try:
        #     logger.save()
        # except:
        #     pass

    def export_data_to_excel(self):
        """Exports the data into a dataframe"""
        df = pd.DataFrame(self.final_listing_list)
        df.to_excel('Chennai_WEST__data_Fri_Apr_22_2022.xlsx')

    def driver_close(self):
        time.sleep(3)
        self.driver.close()
