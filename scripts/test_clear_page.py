import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestClear:
    def setup(self):
        self.driver=init_driver(no_reset=False)
        self.page=Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    def test_clear(self):
        self.page.home.login_if_not(self.page)
        self.page.me.click_setting()
        self.page.setting.click_clear()
        assert self.page.setting.is_toast_exist("清理成功")
