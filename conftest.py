import pytest

from utils.selenium_instance import SeleniumInstance
from utils.const_params import ENVIRONMENTS
from utils.utils import set_key, get_key, get_env_settings


def pytest_addoption(parser):
    parser.addoption('--environment', action="store", help='environment name', default="DEV")
    parser.addoption('--headless', action="store", help='mode to runt test', default="NO")


@pytest.fixture(autouse=True, scope="session")
def set_settings(pytestconfig):
    required_environment, settings = None, None
    if pytestconfig.getoption("environment"):
        required_environment = '{}'.format(pytestconfig.getoption("environment"))
    for env in ENVIRONMENTS:
        if env.upper() == required_environment.upper():
            settings = get_env_settings(required_environment.upper())
            break
    set_key("env_settings", settings)
    set_key("headless", pytestconfig.getoption("headless"))


@pytest.fixture()
def get_settings():
    return get_key("env_settings")


@pytest.fixture(scope="function")
def driver_init(request):
    instance = SeleniumInstance()
    browser = instance.get_browser()
    request.cls.driver = browser
    yield
    instance.close_browser()
