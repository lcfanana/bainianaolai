import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    #提示更新按钮
    close_button=By.ID,"com.yunmall.lc:id/img_close"
    # 我按钮
    my_button=By.ID,"com.yunmall.lc:id/tab_me"
    def click_my(self):
        # 点击关闭更新按钮
        self.click(self.close_button)
        time.sleep(3)
        # 点击我按钮
        self.click(self.my_button)
