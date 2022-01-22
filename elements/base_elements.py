class BaseElements:

    @staticmethod
    def _find_element(browser, locator, element):
        return browser.find_element(locator, element)

    @staticmethod
    def _click(element):
        return element.click()

    @staticmethod
    def _get_to_attribute(element, attribute):
        return element.get_attribute(attribute)

    @staticmethod
    def _get_text(element):
        return element.text
