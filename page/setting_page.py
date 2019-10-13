import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):
    # 关于百年奥莱 按钮
    about_button = By.XPATH, "//*[@text='关于百年奥莱']"

    # 清理缓存 按钮
    clear_cache_button = By.XPATH, "//*[@text='清理缓存']"
    # 地址管理按钮
    address_button=By.XPATH,"//*[@text='地址管理']"
    def click_about(self):
       self.find_element_with_scroll(self.about_button).click()
    def click_clear(self):
        self.find_element_with_scroll(self.clear_cache_button).click()
    def click_address(self):
        self.find_element_with_scroll(self.address_button).click()
