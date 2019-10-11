import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 我按钮
    my_button=By.ID,"com.yunmall.lc:id/tab_me"

    def click_my(self):
        # 点击我按钮
        self.click(self.my_button)

    def login_if_not(self,page):
        # 判断登录状态
        self.click_my()
        if self.driver.current_activity!="com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
#       没有登录就去登录
#         点击已有账号
        page.register.click_login()
#         输入用户名
        page.login.input_username("lcfnana")
#         输入密码
        page.login.input_password("nanana")
#         点击登录
        page.login.click_login()
#
