import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))
        return element

    def find_elements(self, feature, timeout=10, poll=1.0):

        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*feature))
        return element

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, content):
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        self.find_element(feature).clear()
    def is_toast_exist(self, message):
        """
        根据 部分内容，判断toast是否存在
        :param message: 部分内容
        :return: 是否存在
        """
        message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
        try:
            self.find_element(message_xpath, 5, 0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        """
        根据 部分内容，获取toast上的所有内容
        :param message: 部分内容
        :return: 所有内容
        """
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")


    def scroll_page_one_time(self, direction="up"):

        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        center_x = width / 2
        center_y = height / 2

        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y

        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    def find_element_with_scroll(self, feature, direction="up"):

        page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception:

                self.scroll_page_one_time(direction)

                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source

    def is_keyword_inpage(self,keyword,timeout=10,poll=0.1):
        end_time=time.time()+timeout
        while True:
            if end_time<time.time():
                return False
            if keyword in self.driver.page_source:
                return True
            time.sleep(poll)

