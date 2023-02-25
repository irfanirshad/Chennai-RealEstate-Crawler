## Soumil Shah version of undetectable selenium
## takes care of $cdc

__author__ = "Irfan"
__email__ = "irfansnechennai@gmail.com"
try:

    import sys
    import os
    from fp.fp import FreeProxy
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver import Chrome
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    import time
    import threading
    print('all module are loaded ')

except Exception as e:

    print("Error ->>>: {} ".format(e))


class Spoofer(object):

    def __init__(self, country_id=['India'], rand=True, anonym=True):
        self.country_id = country_id
        self.rand = rand
        self.anonym = anonym
        self.userAgent, self.ip = self.get()

    def get(self):
        ua = UserAgent()
        proxy = FreeProxy(country_id=self.country_id, rand=self.rand, anonym=self.anonym).get()
        ip = proxy.split("://")[1]
        # replace ip with real? eg . ip = '172.31.x.x'
        return ua.random, ip


class DriverOptions(object):

    def __init__(self):
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--incognito")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-infobars")


        #self.options.add_argument('--deny-permission-prompts')
        self.helperSpoofer = Spoofer()
        #self.options.add_extension('/Users/aaaii/playGROUND/WORK_SNE/MB_selenium_labz/webrtc__extension.crx')
        self.options.add_argument('user-agent={}'.format(self.helperSpoofer.userAgent))
        self.options.add_argument('--proxy-server=%s' % self.helperSpoofer.ip)


class WebDriver(DriverOptions):

    def __init__(self, path=''):
        DriverOptions.__init__(self)
        self.driver_instance = self.get_driver()

    def get_driver(self):

        print("""
        IP:{}
        UserAgent: {}
        """.format(self.helperSpoofer.ip, self.helperSpoofer.userAgent))

        PROXY = self.helperSpoofer.ip
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy":PROXY,
            "ftpProxy":PROXY,
            "sslProxy":PROXY,
            "noProxy":None,
            "proxyType":"MANUAL",
            "autodetect":False
        }
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

        #path = os.path.join(os.getcwd(), '/usr/local/Caskroom/chromedriver/99.0.4844.51/chromedriver')
        path = '/usr/local/Caskroom/chromedriver/99.0.4844.51/chromedriver'
        driver = webdriver.Chrome(executable_path=path, options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })

        #driver.get("chrome://extensions/?id=fjkmabmdepjfammlpliljpnbhleegehm")
        #driver.execute_script(
        #    "return document.querySelector('extensions-manager').shadowRoot.querySelector('#viewManager > extensions-detail-view.active').shadowRoot.querySelector('div#container.page-container > div.page-content > div#options-section extensions-toggle-row#allow-incognito').shadowRoot.querySelector('label#label input').click()");

        return driver


'''
def routines():
    driver = WebDriver()
    driverinstance = driver.driver_instance
    # driverinstance.get("https://www.expressvpn.com/what-is-my-ip")
    driverinstance.get('https://webbrowsertools.com/test-webrtc-leak/')
    time.sleep(10)
    driverinstance.get('https://www.magicbricks.com')
    time.sleep(10)
    print("done")
'''


def main():
    driver = WebDriver()
    driverinstance = driver.driver_instance
    driverinstance.get("https://www.expressvpn.com/what-is-my-ip")
    time.sleep(5)
    
    driverinstance.get('https://webbrowsertools.com/test-webrtc-leak/')
    time.sleep(10)

    #driver.get("chrome://extensions/?id=fjkmabmdepjfammlpliljpnbhleegehm")
    #time.sleep(5)
    #driver.execute_script(
    #    "return document.querySelector('extensions-manager').shadowRoot.querySelector('#viewManager > extensions-detail-view.active').shadowRoot.querySelector('div#container.page-container > div.page-content > div#options-section extensions-toggle-row#allow-incognito').shadowRoot.querySelector('label#label input').click()");
    #time.sleep(5)


    driverinstance.get('https://www.magicbricks.com')
    time.sleep(15)

    driverinstance.get('https://accounts.magicbricks.com/userauth/login')
    time.sleep(5)

    print("done")








if __name__ == "__main__":
    main()


#def __init__(self, country_id=['US'], rand=False, anonym=False):