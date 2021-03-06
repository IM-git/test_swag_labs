from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as SChrome
from selenium.webdriver.chrome.options import Options as OChrome
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as SFirefox
from selenium.webdriver.firefox.options import Options as OFirefox
from selenoid import capabilities


class Factory:

    @staticmethod
    def get_browser(configuration):
        config = configuration
        if config['browser'] == 'chrome':
            return Factory.chrome_browser()
        elif config['browser'] == 'firefox':
            return Factory.firefox_browser()
        elif config['browser'] == 'chrome_selenoid':
            return Factory.chrome_browser_selenoid()
        elif config['browser'] == 'firefox_selenoid':
            return Factory.firefox_browser_selenoid()
        else:
            raise Exception(f' We are not use the "{Factory.config_browser(config)}".')

    @staticmethod
    def chrome_browser():
        option = OChrome()
        chrome_service = SChrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=option)
        return driver

    @staticmethod
    def firefox_browser():
        option = OFirefox()
        firefox_service = SFirefox(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service, options=option)
        return driver

    @staticmethod
    def chrome_browser_selenoid():
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.ChromeOptions()
        )
        return driver

    @ staticmethod
    def firefox_browser_selenoid():
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.FirefoxOptions()
        )
        return driver

    # @staticmethod
    # def any_browser_selenoid():
    #     """Instead of to use several methods,
    #      can use one unique method for all browsers.
    #      Will need to change the values in 'capabilities'. """
    #     driver = webdriver.Remote(
    #         command_executor="127.0.0.1:4444/wd/hub",
    #         desired_capabilities=capabilities)
    #     return driver

    @staticmethod
    def config_browser(config):
        if 'browser' not in config:
            print('The config file does not contain "browser"')
        elif config['browser'] not in ['chrome', 'firefox']:
            print(f' We are not use the "{config["browser"]}".')
        return config['browser']
