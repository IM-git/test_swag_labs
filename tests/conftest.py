import pytest
from patterns.factory import Factory
from tools.read_file import ReadFile


IMPLICITLY_WAIT_TIME = 10
CONFIG_PATH = "tests/config.json"


@pytest.fixture(scope='session')
def browser():
    data = ReadFile.read_file(CONFIG_PATH)
    driver = Factory().get_browser(data)
    driver.implicitly_wait(IMPLICITLY_WAIT_TIME)
    driver.maximize_window()
    yield driver
    driver.quit()


