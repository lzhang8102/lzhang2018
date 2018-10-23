# coding:utf-8

from common.base import *
from page.loginpage import *

class Delete_Favorite(BasePage):
    '''删除收藏报表'''
    fav_icon_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[1]/header/div[3]/div[1]/i")
    rpt_checkbox_loc = ("css selector",".jstree-icon.jstree-checkbox")
    del_btn_loc = ("css selector",".btn.btn-danger.fav-bth.delete")
    ok_cancel_btn_loc = ("css selector",".btn.btn-danger.ok-btn.ng-binding")

    def fav_icon(self):
        '''点击已收藏图标'''
        self.click(self.fav_icon_loc)

    def rpt_chechbox(self):
        '''点击删除报表的复选框'''
        element = self.find_elements(self.rpt_checkbox_loc)[1].click()
        # element.click(self)

    def del_btn(self):
        '''点击删除按钮'''
        self.click(self.del_btn_loc)

    def ok_cancel_btn(self):
        '''点击ok或cancel按钮'''
        self.click(self.ok_cancel_btn_loc)

    def delete_fav_steps(self):
        '''删除收藏报表流程'''
        self.fav_icon()
        self.rpt_chechbox()
        self.del_btn()
        time.sleep(3) # 不等待定位不到下一个元素
        self.ok_cancel_btn()

    def delete_result(self):
        '''删除后的结果'''
        try:
            t = len(self.find_elements(self.rpt_checkbox_loc))
            if t<2:
                return t
        except:
            print("删除收藏报表失败，返回空字符")
            return ""

if __name__ == "__main__":
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    del_fav = Delete_Favorite(driver)
    url = "https://demo.jintelhealth.com/Analytics/#!/login"
    username = "lz_admin"
    psw = "Ghc2018!"
    login.login_process(url,username,psw)
    del_fav.delete_fav_steps()