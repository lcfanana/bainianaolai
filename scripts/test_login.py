import time
from base.base_driver import init_rivder

class TestLogin:
    def setup(self):
        self.driver=init_rivder()

    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    def test_login(self):
        print("hello")