# coding:utf-8

import unittest
import time

from page.loginpage import *
from page.detailpage import *

driver = webdriver.Firefox()
login = LoginPage(driver)
rpt = Open_Report(driver)
url = "https://demo.jintelhealth.com/Analytics/#!/login"
username = "lz_admin"
psw = "Ghc2018!"

class Test_Detail(unittest.TestCase):
    '''明细表测试'''

    @classmethod
    def setUpClass(cls):
        '''登录'''
        login.login_process(url,username,psw)

    @classmethod
    def tearDownClass(cls):
        login.logout()
        driver.quit()

    def setUp(self):
        '''打开明细表'''
        rpt.open_steps(report_name="Detail0808")
        time.sleep(3)

    def test_01(self):
        '''测试能成功添加快速过滤器'''
        qk_filter = Add_Quick_Filter(driver)
        qk_filter.quick_filter_steps()
        result = qk_filter.get_filter_value()
        self.assertEqual("2", result)

    def test_02(self):
        '''测试能成功添加Basic过滤器'''
        Bsc_filter = Add_Basic_Filter(driver)
        Bsc_filter.basic_filter_steps()
        result = Bsc_filter.get_filter_value()
        self.assertEqual("0006981",result)

    def test_03(self):
        '''测试收藏报表'''
        fav_rpt = Favorite_Report(driver)
        fav_rpt.favorite_steps()
        time.sleep(3)  # 此处如果不等待就获取不到正确的report title元素
        result = fav_rpt.get_favorite_title()
        self.assertEqual("my detail",result)

    def test_04(self):
        '''测试弹出报表'''
        pop_rpt = Pop_out(driver)
        pop_rpt.pop_btn()
        result = len(pop_rpt.get_handles())
        self.assertEqual(2,result)

    def test_05(self):
        '''测试导出报表'''
        ept = Export_Report(driver)
        ept.ept_steps()
        result = ept.download_info()
        self.assertEqual("Download",result)
        ept.close_btn()

    def test_06(self):
        '''测试排序'''
        sort_rpt = Sort_Column(driver)
        sort_rpt.sort_steps()
        result = sort_rpt.sort_result()
        self.assertEqual("1", result)

    def test_07(self):
        '''测试分组'''
        group_rpt = Group_Column(driver)
        group_rpt.group_steps()
        result = group_rpt.group_result()
        self.assertEqual("4611",result)

    def test_08(self):
        '''测试从分组排序中隐藏一列'''
        to_left = Rearrange_Columns_to_left(driver)
        to_left.rearrane_column_to_left_steps()
        result = to_left.column_to_left_result()
        self.assertEqual("",result)

    def test_09(self):
        '''测试从分组排序中隐藏所有字段'''
        all_to_left = Rearrange_all_columns_to_left(driver)
        all_to_left.all_column_to_left_steps()
        result = all_to_left.warning_show()
        self.assertEqual("Please keep at least one column", result)
        all_to_left.close_btn()

    def test_10(self):
        '''测试从分组排序中选择字段显示在报表中'''
        to_right = Rearrange_Columns_to_right(driver)
        to_right.rearrane_column_to_right_steps()
        result = to_right.column_to_right_result()
        self.assertEqual("claim_line_number",result)

    def test_11(self):
        '''测试分组排序显示所有列'''
        all_columns = Rearrange_all_columns_to_right(driver)
        all_columns.all_columns_to_right_steps()
        result = all_columns.all_to_right_result()
        self.assertEqual("member_id",result)

    def test_12(self):
        '''测试取消分组排序'''
        cancel_re = Rearrange_cancel(driver)
        cancel_re.cancel_rearrange_steps()
        result = cancel_re.cancel_rearrange_result()
        self.assertEqual("member_id",result)


if __name__ == "__main__":
    unittest.main()
