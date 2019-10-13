import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):
    # 新增地址按钮
    address_list_button=By.ID,"com.yunmall.lc:id/address_add_new_btn"
    def click_address_list(self):
        self.click(self.address_list_button)