import allure
import logging
import os.path
import json
import pytest

from test_frames.pages.home_page import HomePage
from utils.utils import concat_project_root
from utils.const_params import ProjectPaths
from utils import utils


def open_url(browser, url=None):
    if not url:
        env = utils.get_key("env_settings")
        link = env.get("env_url")
    else:
        link = url
    logging.info(f"Open: '{link}'")
    start = HomePage(browser)
    start.open_url(link)


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    scenario_dict = {}

    def create_instance_of_browser(self, browser):
        if browser:
            open_url(browser)
            return True
        else:
            return None

    # @allure.step('get data scenario')
    def get_data_scenario(self, scenario_name):
        dict_scenario = self.initialize_scenario(scenario_name)
        if dict_scenario:
            return dict_scenario
        else:
            return None

    # @allure.step
    def initialize_scenario(self, scenario):
        scenario_path = concat_project_root(ProjectPaths.FLOW_SCENARIO.value) + scenario
        if os.path.exists(scenario_path):
            with open(scenario_path, 'r') as flow:
                self.scenario_dict = json.load(flow)
                return self.scenario_dict
        else:
            return False
