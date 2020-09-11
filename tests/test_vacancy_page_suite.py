import pytest

from test_frames.flow.main_flow import MainFlow
from tests.base_test import BaseTest
from utils.const_params import CITIES
from utils.utils import get_random_string, capture_screenshot


@pytest.mark.vacancy_page
class TestVacancyPageSuite(BaseTest):

    @pytest.mark.vacancy
    @pytest.mark.parametrize("scenario", ["test_vacancies.json"])
    def test_vacancies(self, scenario):
        """
        The test checks whether there are vacancies for specialists of a certain level
        :param scenario: json file that contains params with the levels of specialist
        """
        self.create_instance_of_browser(self.driver)
        test = MainFlow(self.driver)
        try:
            test.go_to_section("Вакансии")
            expected_vacations = test.get_test_data(scenario, "vacancies")
            test.validate_given_vacancies(expected_vacations)
        except Exception:
            capture_screenshot(self.driver, get_random_string())
            raise

    @pytest.mark.draft
    @pytest.mark.vacancy
    @pytest.mark.parametrize("city", [*CITIES])
    def test_cities(self, city):
        """
        The test checks if there are vacancies for specialists from certain cities
        :param city: the list of certain cities
        """
        self.create_instance_of_browser(self.driver)
        test = MainFlow(self.driver)
        try:
            test.go_to_section("Вакансии")
            test.validate_vacancy_for_city(city)
        except Exception:
            capture_screenshot(self.driver, get_random_string())
            raise

