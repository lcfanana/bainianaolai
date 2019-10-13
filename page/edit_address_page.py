import random
import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAdressPage(BaseAction):
    # 姓名
    name_text=By.ID,"com.yunmall.lc:id/address_receipt_name"
    # 电话
    phone_text=By.ID,"com.yunmall.lc:id/address_add_phone"
    # 详细地址
    info_text=By.ID,"com.yunmall.lc:id/address_detail_addr_info"
    # 邮编
    post_code=By.ID,"com.yunmall.lc:id/address_post_code"
    # 保存按钮
    save_button=By.ID,"com.yunmall.lc:id/button_send"
    # 默认按钮
    default_button=By.ID,"com.yunmall.lc:id/address_default"

    region_button=By.ID,"com.yunmall.lc:id/address_province"
    all_area=By.ID,"com.yunmall.lc:id/area_title"

    def send_name(self,text):
        self.input(self.name_text,text)
    def send_phone(self,phone):
        self.input(self.phone_text,phone)
    def send_info(self,info):
        self.input(self.info_text,info)
    def send_post(self,post):
        self.input(self.post_code,post)
    def click_default(self):
        self.click(self.default_button)
    def click_save(self):
        self.click(self.save_button)
    def click_region(self):
        self.click(self.region_button)


    def choose_region(self):
        self.click_region()
        time.sleep(2)
        while True:
            if self.driver.current_activity!="com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            # 所有城市
            areas=self.find_elements(self.all_area)
            # 总数
            areas_count=len(areas)
            # 随机数下标
            areas_index=random.randint(0,areas_count-1)
            # 获取随机城市
            areas[areas_index].click()
            time.sleep(2)