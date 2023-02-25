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


option = webdriver.ChromeOptions()
chrome_prefs = {}
option.experimental_options["prefs"] = chrome_prefs

chrome_prefs["profile.default_content_settings"] = { "popups": 1 }




url_main = 'https://www.magicbricks.com/property-for-rent/commercial-real-estate?bedroom=&proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom&cityName=Chennai'

url_new = 'https://www.magicbricks.com/property-for-rent/commercial-real-estate?bedroom=&proptype=Commercial-Office-Space,Office-ITPark-SEZ&cityName=West-area-Chennai'

url = 'https://www.magicbricks.com/property-for-rent/commercial-real-estate?bedroom=&proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom,Commercial-Land,Industrial-Land,Co-working-Space,Warehouse-Godown,Industrial-Building,Industrial-Shed&cityName=Chennai'

# https://www.magicbricks.com/property-for-rent/commercial-real-estate?bedroom=&proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom,Commercial-Land,Industrial-Land,Co-working-Space,Warehouse-Godown,Industrial-Building,Industrial-Shed&cityName=Chennai

url_1 = 'https://www.magicbricks.com/property-for-rent/commercial-real-estate?bedroom=&proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom,Commercial-Land,Industrial-Land,Co-working-Space,Warehouse-Godown,Industrial-Building,Industrial-Shed&Locality=Guindy&cityName=Chennai'

url_2 = 'https://www.magicbricks.com/property-for-sale/commercial-real-estate?bedroom=&proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom,Commercial-Land,Industrial-Land,Warehouse-Godown,Industrial-Building,Industrial-Shed&Locality=Guindy&cityName=Chennai'

url_login = 'https://accounts.magicbricks.com/userauth/login'

driver = webdriver.Chrome('/usr/local/Caskroom/chromedriver/99.0.4844.51/chromedriver', chrome_options=option)
# /usr/local/bin/chromedriver
# /usr/local/Caskroom/chromedriver/99.0.4844.51/chromedriver

## Login form 
driver.get(url_login)

time.sleep(2)

# inpur username form
user_link = driver.find_element(By.XPATH, '//*[@id="emailOrMobile"]')
user_link.send_keys('vasxxxxxx@gmail.com')

# click on next button
next_button = driver.find_element(By.XPATH, '//*[@id="btnStep1"]')
next_button.click()


# input password form
passwd_link = driver.find_element(By.XPATH, '//*[@id="password"]')
passwd_link.send_keys('xxxxxxxx!')

#login button click
login_button = driver.find_element(By.XPATH, '//*[@id="btnLogin"]')
login_button.click()

time.sleep(2)

## Post Login Module -> GOTO property search page
driver.get(url_new)


driver.implicitly_wait(3)

time.sleep(4)

# //*[@id="moreFilter_0"]/div[2]/div/div/div/div[2]/input[1]
## MIN - //*[@id="moreFilter_0"]/div[2]/div/div/div/div[1]/div[1]/select


# //*[@id="body"]/div[1]/div/div[2]/div[2]/div/div[1]
# //*[@id="body"]/div[1]/div/div[2]/div[5]/div/div[1]
# //*[@id="body"]/div[1]/div/div[2]/div[5]

#'//*[@id="body"]/div[1]/div/div[2]/div[7]/div/div[1] -- last used b4 error

# Click on Specifications
# //*[@id="body"]/div[1]/div/div[2]/div[5]/div/div[1]
# //*[@id="body"]/div[1]/div/div[2]/div[5]/div/div[1]
link = driver.find_element(By.XPATH, '//*[@id="body"]/div[1]/div/div[2]/div[5]/div/div[1]')
#link = driver.find_element(By.CLASS_NAME, "filter__component topMoreFilters activeFilter")
link.click()


# click to remove "FreeHold" -> owner // weird shit that vasu id is doing
#time.sleep(2)
#link_x = driver.find_element(By.XPATH, '//*[@id="moreFilter_22"]/div[2]/div[1]/label')
#link_x.click()

## Click on following elements to uncheck them A.K.A ClickTwice_to_UnCheck
# Total 8 Uncheckings
time.sleep(2)


# Click on Owners
# //*[@id="moreFilter_11"]/div[2]/div[1]/label
# //*[@id="moreFilter_0"]/div[2]/div/div/div/div[2]/input[1]
time.sleep(2)
link1 = driver.find_element(By.XPATH, '//*[@id="moreFilter_11"]/div[2]/div[1]/label')
link1.click()
time.sleep(2)
driver.implicitly_wait(2)

'''
#Commercial Shop
link2 = driver.find_element(By.XPATH, '//*[@id="moreFilter_26"]/div[2]/div[3]/label')
link2.click()
time.sleep(1)
 
#Commercial Showroom
link3 = driver.find_element(By.XPATH, '//*[@id="moreFilter_26"]/div[2]/div[4]/label')
link3.click()
time.sleep(1)

#Commercial Land
link4 = driver.find_element(By.XPATH, '//*[@id="moreFilter_26"]/div[2]/div[5]/label')
link4.click()
time.sleep(1)

#Industrial Land
link5 = driver.find_element(By.XPATH, '//*[@id="moreFilter_26"]/div[2]/div[6]/label')
link5.click()
time.sleep(1)

#Co-working Space
link6 = driver.find_element(By.XPATH, '//*[@id="moreFilter_26"]/div[2]/div[7]/label')
link6.click()
time.sleep(1)

#Warehouse/ Godown
link7 = driver.find_element(By.XPATH, '//*[@id="moreFilter_26"]/div[2]/div[8]/label')
link7.click()
time.sleep(1)

#Industrial Building
link8 = driver.find_element(By.XPATH, '//*[@id="moreFilter_26"]/div[2]/div[9]/label')
link8.click()
time.sleep(1)

#Industrial Shed
link9 = driver.find_element(By.XPATH, '//*[@id="moreFilter_26"]/div[2]/div[10]/label')
link9.click()
time.sleep(1)

'''

# adjust sqft slider
time.sleep(2)
min_btn = driver.find_element(By.XPATH, '//*[@id="moreFilter_0"]/div[2]/div/div/div/div[1]/div[1]/select')
select = Select(min_btn)
time.sleep(1)

try:
    select.select_by_visible_text("500")
except NoSuchElementException:
    print("ERROR EXCEPTION-Drop Down doesnt exist")
time.sleep(2)

# //*[@id="moreFilter_0"]/div[2]/div/div/div/div[1]/div[1]/select

# //*[@id="moreRefined"]/div[3]/div/div[2]
## Click "View Properties"
view_button = driver.find_element(By.XPATH, '//*[@id="moreRefined"]/div[3]/div/div[2]')
view_button.click()
time.sleep(3)
driver.implicitly_wait(3)

# mb-srp__list && id='cardid48062915' 
    # mb-srp__card (normal )   
    # mb-srp__card card-mbprime (for MB_prime)

previous_height = driver.execute_script('return document.body.scrollHeight')

time.sleep(2)
bot_minimize = driver.find_element(By.XPATH, '//*[@id="bot-container"]/div[1]/a[1]')
bot_minimize.click()

# +
# Scroll to the bottom
while True:
    time.sleep(7)
    driver.implicitly_wait(7)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(7)
    driver.implicitly_wait(7)
    new_height = driver.execute_script('return document.body.scrollHeight')
    time.sleep(7)
    driver.implicitly_wait(7)
    if new_height == previous_height:
        break 
    time.sleep(7)
    driver.implicitly_wait(7)
    previous_height = new_height
    time.sleep(7)
    driver.implicitly_wait(7)

print("End of scroll reached")
driver.implicitly_wait(10)

# get_attribute('id') 

# get all elements of class name 
# mb-srp__card card-mbprime
time.sleep(3)
driver.implicitly_wait(10)

total_mb_srp__lists = driver.find_elements(By.CLASS_NAME, 'mb-srp__list')
time.sleep(6)
# filter_mb_srp_lists = total('mb-srp__card card-mbprime')
driver.implicitly_wait(10)

# ~
listing_list = []
listing_list1= defaultdict(list)

prime_listings = []

count = 0
count_prime = 0


# def prime_store_function(list):
#     how_many = list.find_elements(By.CLASS_NAME, 'mb-srp__card__summary-commercial__list--item')
#     print(len(how_many))
    

prime_set = set(String)

def prime_seperator(list, card_id):
    #text = list.find_element(By.XPATH, '//*[@id="{0}"]/div/div[2]/div[2]/a').format(card_id)
    #mb-srp__card__pe-info
    driver.implicitly_wait(2)
    try:
        driver.implicitly_wait(2)
        if(list.find_element(By.CLASS_NAME, "mb-srp__card__exclusive-prop")) != 0:
            driver.implicitly_wait(2)
            prime_set.add(card_id)
            driver.implicitly_wait(3)
            count_prime = count_prime + 1
    except:
        driver.implicitly_wait(3)
        print("not a prime")
        driver.implicitly_wait(2)
        
    driver.implicitly_wait(2)


def test_func(list, len_list, card_id):
    driver.implicitly_wait(2)
    r = re.findall('(\d+)', card_id)
    r1 = r[0]
    owner_name = list.find_element(By.XPATH, f'//*[@id="{card_id}"]/div/div[1]/div[1]/div[2]/div').text
    driver.implicitly_wait(2)
    price = list.find_element(By.XPATH, f'//*[@id="{card_id}"]/div/div[2]/div[1]/div[1]').text
    driver.implicitly_wait(2)
    address = list.find_element(By.XPATH, f'//*[@id="{card_id}"]/div/div[1]/div[2]/h2').text 
    driver.implicitly_wait(2)
    #description = list.find_element(By.XPATH, f'//*[@id="{card_id}"]/div/div[1]/div[2]/div[6]/div').text 
    driver.implicitly_wait(2)
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
    driver.implicitly_wait(2)
    
    try:
        if(list.find_element(By.CLASS_NAME, "mb-srp__card--desc--readmore")) != 0:
            driver.implicitly_wait(2)
            if card_id in prime_set:
                driver.implicitly_wait(2)
                description = list.find_element(By.CLASS_NAME, "mb-srp__card--desc--text").text
                info_5 = {
                    'Description-MB-prime': description
                }
            else:
                driver.implicitly_wait(2)
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
    
    driver.implicitly_wait(2)
    listing_list1[card_id].append(info_1)
    driver.implicitly_wait(2)
    listing_list1[card_id].append(info_2)
    driver.implicitly_wait(2)
    listing_list1[card_id].append(info_3)
    driver.implicitly_wait(2)
    listing_list1[card_id].append(info_4)
    driver.implicitly_wait(2)
    listing_list1[card_id].append(info_5)
    driver.implicitly_wait(2)
    for i in range(1,len_list+1):
        driver.implicitly_wait(2)
        title = list.find_element(By.XPATH,f'//*[@id="propertiesAction{r1}"]/div/div[{i}]/div[1]').text
        driver.implicitly_wait(2)
        text = list.find_element(By.XPATH,f'//*[@id="propertiesAction{r1}"]/div/div[{i}]/div[2]').text
        driver.implicitly_wait(2)
        #print(title, text)
        listing_item = {
            title: text
        }
        driver.implicitly_wait(1)
        listing_list1[card_id].append(listing_item.copy())
        driver.implicitly_wait(1)
        #assemble(title, text) # goto function which assembles data to be stored
        #store_csv(title, text) # Use this function to store into a xls format
    driver.implicitly_wait(2)
    listing_list.append(listing_list1[card_id])
    driver.implicitly_wait(2)

'''
else:  
# If it is, just extract whatever you can find.. DO NOT CLICK IT . inb4 POPUP HELL!!
description = list.find_element(By.CLASS_NAME, "mb-srp__card--desc--text").text
driver.implicitly_wait(2)
info_5 = {
'DESCRIPTION_MB_prime': description
}
'''

for list in total_mb_srp__lists:
    card_id = list.get_attribute('id')
    print(card_id)
    driver.implicitly_wait(2)
    prime_seperator(list, card_id)
    driver.implicitly_wait(4)
    
    try:
        driver.implicitly_wait(2)
        how_many = list.find_elements(By.CLASS_NAME, 'mb-srp__card__summary-commercial__list--item')
        driver.implicitly_wait(2)
        len_list = len(how_many)
        driver.implicitly_wait(2)
        test_func(list, len_list, card_id)
        driver.implicitly_wait(2)
    except:
        print("Error...Moving on")
        continue
        driver.implicitly_wait(2)
    driver.implicitly_wait(1)

#print("COUNT IS ===>", count) 

print("COUNT of PRIME IS ===>", count_prime)


driver.implicitly_wait(3)

#previous_height = driver.execute_script('return document.body.scrollHeight')

df = pd.DataFrame(listing_list)
df.to_excel('Chennai_WEST__data_Fri_Apr_22_2022.xlsx')
print(df)


time.sleep(3)

driver.close()