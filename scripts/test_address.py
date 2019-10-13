import time

from selenium.webdriver.common.by import By

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page
import pytest

class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    def test_address(self):
        self.page.home.login_if_not(self.page)
        self.page.me.click_setting()
        self.page.setting.click_address()
        self.page.address_list.click_address_list()
        self.page.edit_address.send_name("hehe")
        self.page.edit_address.send_phone("11111111111")
        self.page.edit_address.send_info("民族大道203号")
        self.page.edit_address.send_post("435000")
        self.page.edit_address.choose_region()
        self.page.edit_address.click_default()
        self.page.edit_address.click_save()







