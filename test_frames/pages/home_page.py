import logging

from selenium.webdriver.common.by import By
from test_frames.pages.base_page import BasePage, update_locator_with_data


class HomePage(BasePage):

    MAIN_LOGO = (By.XPATH, "//header//img[@alt='CHI Software']")
    MAIN_MENU = (By.XPATH, "//ul[@id='menu']")
    MAIN_MENU_ITEM = (By.XPATH, "//ul[@id='menu']//a")
    SECTION_NAME = (By.XPATH, "//ul[@id='menu']//a[contains(.,'{}')]")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def open_url(self, url):
        """
        Opens url
        :param url: ulr
        """
        self.driver.get(url)

    def check_is_logo_displayed(self):
        """
        Сhecks if the logo is displayed
        :return: True/False
        """
        return self.wait_till_element_is_displayed(self.MAIN_LOGO)

    def get_main_menu_sections(self):
        """
        Gets names of the main menu sections
        :return: list of sections
        """
        logging.info("Get titles of the main menu")
        if self.wait_till_element_is_displayed(self.MAIN_LOGO):
            list_of_object = self.driver.find_elements(*self.MAIN_MENU_ITEM)
            if list_of_object:
                result = []
                for i in list_of_object:
                    item = i.get_attribute("outerText")
                    result.append(item.capitalize())
                return result

    def open_section(self, section_name):
        """
        Opens certain section of main menu
        :param section_name: section name
        """
        section_locator = update_locator_with_data(self.SECTION_NAME, section_name)
        self.click_on_element_with_any_locator(section_locator, check_is_displayed=False)
