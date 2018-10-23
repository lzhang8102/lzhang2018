# coding:utf-8

from common.base import *


class LoginPage(BasePage):
    '''登录页面'''
    user_loc = ("id", "username")       # 用户名
    psw_loc = ("id", "password")        # 密码
    login_btn_loc = ("id", "loginBtn")  # 登录按钮
    result_loc = ("css selector", ".box-title.container__title.ng-binding")  # 登录结果

    def open_login_page(self,url):
        '''打开平台url'''
        self.open(url)

    def logout(self):
        '''登出'''
        self.driver.delete_all_cookies()  # 删除所有cookies
        self.driver.refresh()

    def input_username(self,username):
        '''输入用户名'''
        self.send_keys(self.user_loc,username)

    def input_psw(self,psw):
        '''输入密码'''
        self.send_keys(self.psw_loc,psw)

    def submit_btn(self):
        '''点击登录按钮'''
        self.click(self.login_btn_loc)

    def login_process(self,url,username = "admin",psw = "root123"):
        '''登录流程'''
        self.open_login_page(url)
        self.input_username(username)
        self.input_psw(psw)
        self.submit_btn()

    def get_result(self):
        '''获取登录结果'''
        try:
            t = self.find_element(self.result_loc).text
            return t
        except:
            print("登录失败，返回空字符")
            return ""


if __name__ == "__main__":
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    url = "https://demo.jintelhealth.com/Analytics/#!/login"
    username = "lz_admin"
    psw = "Ghc2018!"
    login.login_process(url,username,psw)
    login.get_result()
    login.logout()
    result = login.get_result()
    print(result)
    driver.quit()
