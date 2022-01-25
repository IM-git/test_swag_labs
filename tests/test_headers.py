import requests
import allure
from locators import Login
from src.enums import LoginPageErrorMessages


@allure.feature("Login page.")
@allure.link(url=Login.LINK, name='Login_LINK')
def test_headers():
    """Checking status code, url, cookies, on the page.
    Compare values in the headers."""
    response = requests.get(url=Login.LINK)
    check_url = response.url
    check_cookies = response.cookies.values()
    check_status_code = response.status_code
    get_list_headers = response.headers

    assert check_status_code == 200, LoginPageErrorMessages.WRONG_PAGE.value
    assert check_url == Login.LINK, LoginPageErrorMessages.WRONG_PAGE.value
    assert check_cookies == [], LoginPageErrorMessages.LOGIN_COOKIE.value
    assert len(get_list_headers['X-Fastly-Request-ID']) == 40, \
           LoginPageErrorMessages.MISMATCH.value
    assert get_list_headers['Last-Modified'] == \
           Login.CHECK_LIST_FOR_HEADERS['Last-Modified'], \
           LoginPageErrorMessages.MISMATCH.value

