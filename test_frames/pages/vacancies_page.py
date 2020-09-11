import logging
from selenium.webdriver.common.by import By
from test_frames.pages.base_page import BasePage, update_locator_with_data


class VacanciesPage(BasePage):

    SEARCH_INPUT = (By.XPATH, "//input[@id='autocomplete']")
    SEARCH_BUTTON = (By.XPATH, "//i[@class='icon-search']")
    ACTIVE_FILTER = (By.XPATH, "//ul[@id='list-active-filter']")
    VACANCY = (By.XPATH, "//*[@class='vacancies-card__title']/a")
    CHECKBOX = (By.XPATH, "//form[@id='vacancies-filter']/*[contains(.,'location')]//label[contains(.,'{}')]/input")
    VACANCY_RESULT_BLOCK = (By.XPATH, "//div[@id='vacancies-block']")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def fill_search_input(self, text, clear=True):
        """
        Fills the search filed with text
        :param text: text to fill
        :param clear: Should the field be cleared?
        """
        search_input = self.wait_till_element_is_displayed(self.SEARCH_INPUT)
        self.scroll_to_element(search_input)
        if clear:
            search_input.clear()
        search_input.send_keys(text)

    def check_is_vacancy_present(self, vacancy):
        """
        Checks if certain vacancy is present
        :param vacancy: vacancy name
        :return: True/False
        """
        self.fill_search_input(vacancy)
        self.click_on_element_with_any_locator(self.SEARCH_BUTTON, check_is_displayed=False)
        return self.check_are_any_vacancies_present()

    def check_checkbox(self, data):
        """
        Checks the checkbox
        :param data: checkbox name
        """
        logging.info(f"Pick the '{data.upper()}' checkbox")
        checkbox_locator = update_locator_with_data(self.CHECKBOX, data)
        self.click_on_element_with_any_locator(checkbox_locator, check_is_displayed=False)

    def check_are_any_vacancies_present(self):
        """
        Checks if any vacancies are present
        :return:
        """
        result_block = self.wait_till_element_is_displayed(self.SEARCH_INPUT)
        self.scroll_to_element(result_block)
        return self.driver.find_elements_by_xpath(self.VACANCY[1])
