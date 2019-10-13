import time

from selenium.webdriver.common.by import By

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page
import pytest

class TestVip:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("all_data.yaml","test_vip"))
    def test_vip(self,args):
        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 我 点击 加入vip
        self.page.me.click_vip()
        # print(self.driver.contexts)
        # # 切换 web环境
        # self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        # # vip 输入 邀请码
        # self.page.vip.input_invite(args["keyword"])
        # # vip 点击 加入会员
        # self.page.vip.click_bevip()
        time.sleep(5)
        self.page.vip.input_invite2(args["keyword"])
        time.sleep(5)
        self.page.vip.click_bevip2()
        # 断言
        assert self.page.vip.is_keyword_inpage(args["expect"]),"你输入的邀请码不在page_source中"
        # 切换 原生环境
        # self.driver.switch_to.context("NATIVE_APP")

