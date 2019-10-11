import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):
    # 昵称
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    # 设置按钮
    setting_button=By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
    # 加入超级VIP
    vip_button=By.XPATH,"//*[@text='加入超级VIP']"

    def get_nick_name_text(self):
        return self.find_element(self.nick_name_text_view).text
    def click_setting(self):
        # 点击设置按钮
        self.click(self.setting_button)
        # 点击加入VIP
    def click_vip(self):
        self.find_element_with_scroll(self.vip_button).click()
        time.sleep(3)