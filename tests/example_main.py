from selenium import webdriver
import time


capabilities = {
    "browserName": "chrome",
    "browserVersion": "97.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}


def test_main():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=webdriver.ChromeOptions()
    )

    try:
        print('Session ID is: %s' % driver.session_id)
        print('Opening the page...')
        driver.get('https://duckduckgo.com/')

        print('Taking screenshot...')
        driver.get_screenshot_as_file(driver.session_id + '.png')
    finally:
        driver.quit()
