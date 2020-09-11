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


    # def check_is_jobs_displayed(self):
    #     return self.wait_till_element_is_displayed(self.JOBS_CONTENT)

    # def press_next(self):
    #     next_button = (By.XPATH, self.ACTIVE_TAB_PANEL + self.BUTTON.format("Next"))
    #     self.click_on_element(next_button)

    # def press_button_on_active_tab(self, button_name):
    #     next_button = (By.XPATH, self.ACTIVE_TAB_PANEL + self.BUTTON.format(button_name))
    #     self.click_on_element(next_button)
    #
    # def press_new_job(self):
    #     add_new_job_button = (By.XPATH, self.BUTTON.format("Add New Job"))
    #     self.click_on_element(add_new_job_button)
    #
    # def select_retailer(self, retailer):
    #     retailer_button = (By.XPATH, self.BUTTON.format(retailer))
    #     self.click_on_element(retailer_button)
    #
    # def fill_job_name(self, job_name):
    #     job_name_field = self.wait_till_element_is_displayed(self.JOB_NAME_FIELD)
    #     job_name_field.send_keys(job_name)
    #
    # def enter_skus(self, skus_id):
    #     job_name_field = self.wait_till_element_is_displayed(self.TEXTAREA)
    #     job_name_field.send_keys(skus_id)
    #
    # def approve_submit(self):
    #
    #     # turned_off = self.driver.find_elements_by_xpath(self.map_locators.filter_clickable, 1)
    #     # if turned_off and len(turned_off) > 0:
    #     #     for item in turned_off:
    #     #         self.click_by_execute_script_on_element(item)
    #     #
    #     # options = [x for x in self.driver.find_elements_by_xpath(dropdown_items)]
    #     # for element in options:
    #     #     list_items.append(element.get_attribute("outerText"))
    #
    #     approve_checkbox = self.ACTIVE_TAB_PANEL+"//input"
    #     checkbox_list = [x for x in self.driver.find_elements_by_xpath(approve_checkbox)]
    #     for checkbox in checkbox_list:
    #         self.click_by_execute_script_on_element(checkbox)
    #
    # def accept_alert(self):
    #     # close_button = (By.XPATH, self.ALERT_CLOSE_BUTTON)
    #     self.click_on_element(self.ALERT_CLOSE_BUTTON)
    #     # elem = self.driver.find_elements_by_xpath(self.incident_locators.ok_button)
    #     # # logging.debug(len(elem))
    #     # if len(elem) > 0:
    #     #     elem[0].click()
    #
    # def check_are_link_present(self, expected_vacations):
    #     '''logging.info(f"Validate the file does not have error action\n")
    #     find_error_action = self._find_record_with_action(results, 'ERROR')
    #     delayed_assert.expect(find_error_action is False, f"Clean file {file_name} should not have ERROR action")
    #
    #     delayed_assert.assert_expectations()'''
    #     for link in expected_vacations:
    #         result = self.wait_till_element_is_displayed(self.SECTION_LINK, timeout=5)
    #         delayed_assert.expect(result is True, f"Link is not found")
    #
    #     a = delayed_assert.assert_expectations()
    #     print(a)

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
