import datetime
import logging
from selenium import webdriver
from utils.const_params import ProjectPaths
from os.path import dirname
from selenium.webdriver.chrome.options import Options
from utils import utils


class SeleniumInstance:

    def __init__(self):
        chrome_options = Options()
        main_directory = dirname(dirname(__file__))
        headless = utils.get_key("headless")
        try:
            if headless == 'YES':
                chrome_options.add_argument("--headless")
                #allow notifications the argument 1 to allow and 2 to block

            chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
            self.browser = webdriver.Chrome(options=chrome_options,
                                            executable_path=main_directory + "/" + ProjectPaths.CHROME_DRIVER.value)
            logging.info(f"Chromedriver is set up at: {str(datetime.datetime.now())}")
            if headless == 'YES':
                window_weight = 1920
                window_height = 1080
                self.browser.set_window_size(window_weight, window_height)
            else:
                self.browser.maximize_window()
        except Exception as e:
            logging.error('Failed to do something: ' + str(e))

    def get_browser(self):
        return self.browser

    def close_browser(self):
        self.browser.close()
