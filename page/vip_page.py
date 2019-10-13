import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class VipPage(BaseAction):
    # 邀请码输入框
    invite_text=By.XPATH,"//input[@type='tel']"
    # 立即成为会员按钮
    be_vip=By.XPATH,"//input[@value='立即成为会员']"

    invite_text2=By.XPATH,"//android.widget.EditText"
    # "//android.webkit.WebView[@content-desc='百年奥莱']/android.view.View/android.widget.EditText"
    be_vip2=By.XPATH,"//android.widget.Button[@content-desc='立即成为会员']"

    def input_invite(self,text):
        self.input(self.invite_text,text)
    def click_bevip(self):
        self.click(self.be_vip)

    def input_invite2(self, text):
        el = self.find_element(self.invite_text2)
        el.click()
        el.send_keys(text)

    def click_bevip2(self):
        self.click(self.be_vip2)
