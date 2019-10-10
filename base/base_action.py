from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=20, poll=1):
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))
        return element

    def find_elements(self, feature, timeout=10, poll=1):

        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*feature))
        return element

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, content):
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        self.find_element(feature).clear()