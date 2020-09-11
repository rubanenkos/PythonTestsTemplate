import logging

import allure

from test_frames.pages.home_page import HomePage
from test_frames.pages.vacancies_page import VacanciesPage
from tests.base_test import BaseTest
from utils.utils import retrieve_node_value_from_json, compare_lists_entities
from delayed_assert import delayed_assert


class MainFlow(BaseTest):

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.vacancies = VacanciesPage(self.driver)

    def get_test_data(self, data_source, node):
        """
        Gets test data
        :param data_source: source of data
        :param node: node of data
        :return: data
        """
        logging.info(f"Get test data for user: '{node}'")
        user_scenarios = self.get_data_scenario(data_source)
        data = retrieve_node_value_from_json(user_scenarios, node)
        return data

    def validate_is_logo_displayed(self):
        """Validates if there is a correct logo
        """
        logging.info("Validate is logo displayed")
        assert self.home_page.check_is_logo_displayed()

    def validate_are_sections_present(self, sections):
        """
        Validates if there are sections
        :param sections: section name
        :return: True/False
        """
        actual_main_menu_sections = self.home_page.get_main_menu_sections()
        expected_main_menu_sections = list(sections.keys())
        logging.info("Validate are sections present")
        result = compare_lists_entities(actual_main_menu_sections, expected_main_menu_sections)
        error_message = f"The items do not match:\n  Expected:{expected_main_menu_sections} \n  Actual  :{actual_main_menu_sections}"
        assert len(result) == 0, error_message

    def go_to_section(self, section_name):
        """
        Go to certain section
        :param section_name: section name
        """
        logging.info(f"Go to section '{section_name.upper()}'")
        self.home_page.open_section(section_name)

    def validate_given_vacancies(self, expected_vacations):
        """
        Validates if there are given vacations
        :param expected_vacations: expected vacations
        :return: True/False
        """
        for vacation in expected_vacations:
            logging.info(f"Verify is vacancy '{vacation.upper()}' present into search results")
            result = self.vacancies.check_is_vacancy_present(vacation)
            delayed_assert.expect(len(result) > 0, f"Vacancy {vacation} is not found")
        delayed_assert.assert_expectations()

    def validate_vacancy_for_city(self, city):
        """
        Validates if there are vacations for certain city
        :param city: name of city
        :return: True/False
        """
        self.vacancies.check_checkbox(city)
        logging.info(f"Verify the vacancies are available for city '{city.upper()}'")
        result = self.vacancies.check_are_any_vacancies_present()
        assert len(result) > 0, f"Vacancies for {city} are not found"
