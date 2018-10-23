# coding:utf-8

import unittest
import time

from page.loginpage import *
from page.favpage import *

driver = webdriver.Firefox()
login = LoginPage(driver)
url = "https://demo.jintelhealth.com/Analytics/#!/login"
username = "lz_admin"
psw = "Ghc2018!"

class Test_Fav(unittest.TestCase):
    '''收藏报表框测试'''

    # @classmethod
    def setUp(self):
        '''登录'''
        login.login_process(url,username,psw)

    # @classmethod
    def tearDownClas(self):
        login.logout()
        driver.quit()

    def test_01(self):
        '''测试删除收藏报表'''
        del_fav = Delete_Favorite(driver)
        del_fav.delete_fav_steps()
        time.sleep(3)
        result = del_fav.delete_result()
        self.assertEqual(1,result)

if __name__ == "__main__":
    unittest.main()