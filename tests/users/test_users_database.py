import pytest
import allure
from locators import Login
from tools import Comparing
from tools import logger as Logger
from src.enums import *

SQL_REQUEST = "SELECT login, password FROM users"


@allure.feature("Checking values in SQL database.")
@Logger.logger.catch()
def test_users_database(database):
    """This test compares two lists,
    from database and locators file."""
    getting_list_with_logins_and_password = \
        database.execute(f'''{SQL_REQUEST}''').fetchall()
    get_only_keys = dict(getting_list_with_logins_and_password).keys()
    checking_for_match_lists = Comparing.comparing_lists(
        lists_one=get_only_keys, lists_two=Login.LIST_NAMES)
    assert checking_for_match_lists == True, SQLErrorMessages.NOT_MATCH.value
