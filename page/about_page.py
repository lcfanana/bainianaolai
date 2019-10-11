import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AboutPage(BaseAction):
    update_button=By.ID,"com.yunmall.lc:id/about_version_update"
    def click_update(self):
        self.click(self.update_button)