class BaseElements:

    @staticmethod
    def find_element(browser, locator, element):
        return browser.find_element(locator, element)

    @staticmethod
    def click(element):
        return element.click()

    @staticmethod
    def get_to_attribute(element, attribute):
        return element.get_attribute(attribute)

    @staticmethod
    def get_text(element):
        return element.text
