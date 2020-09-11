import pytest

from test_frames.flow.main_flow import MainFlow
from tests.base_test import BaseTest
from utils.const_params import SITE_SECTIONS
from utils.utils import capture_screenshot, get_random_string


@pytest.mark.home_page
class TestHomePageSuite(BaseTest):

    def test_logo(self):
        """
        User story that validates the main logo is displayed on the Home page
        """
        self.create_instance_of_browser(self.driver)
        test = MainFlow(self.driver)
        try:
            test.validate_is_logo_displayed()
        except Exception:
            capture_screenshot(self.driver, get_random_string())
            raise

    # @pytest.mark.draft
    def test_sections(self):
        """
        User story that validates the sections are displayed on the Home page
        """
        self.create_instance_of_browser(self.driver)
        test = MainFlow(self.driver)
        try:
            test.validate_are_sections_present(SITE_SECTIONS)
        except Exception:
            capture_screenshot(self.driver, get_random_string())
            raise

