# coding:utf-8

from common.base import *
from page.loginpage import *
from selenium.webdriver.common.keys import Keys

class Open_Report(BasePage):
    '''查找并打开报表'''
    input_loc = ("id", "topInput")
    search_icon_loc = ("id", "myI")
    report_title_loc = ("class", ".box-title.container__title.ng-binding")

    def input_name(self,report_name):
        '''输入表名'''
        self.send_keys(self.input_loc,report_name)

    def search_btn(self):
        '''点击查找按钮'''
        self.click(self.search_icon_loc)

    def open_steps(self,report_name="Detail0808"):
        '''打开报表流程'''
        self.input_name(report_name)
        self.search_btn()

    def get_report_title(self):
        '''获取表名称'''
        try:
            t = self.find_element(self.report_title_loc).text
            return t
        except:
            print("获取表名失败，返回空字符")
            return ""


class Add_Quick_Filter(BasePage):
    '''添加快速过滤器'''
    add_filter_loc = ("xpath", ".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[2]/basic-filter/div/div[1]/div[1]")
    quick_loc = ("xpath", ".//*[@id='collapse']/div/div[1]/ul/li[1]/a/uib-tab-heading")
    input_loc = ("xpath", ".//*[@id='collapse']/div/div[1]/div/div[1]/ul[2]/li/div[2]/div/div/div/textarea")
    operation_list_loc = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[1]/ul[2]/li/div[3]/div/div[1]")
    operation_loc = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[1]/div/ul[2]/li[1]/div[3]/div/div[2]/div/div/div[2]/div")
    apply_filter_loc = ("id", "refresh-filter")
    result_filter_loc = ("xpath", ".//*[@id='table']/tbody/tr[2]/td[4]")

    def add_filter_btn(self):
        '''点击过滤器按钮'''
        self.click(self.add_filter_loc)

    def quick_btn(self):
        '''点击过滤器中Quick按钮'''
        self.click(self.quick_loc)

    def input_filter_value(self,value):
        '''输入过滤值'''
        self.send_keys(self.input_loc,value)

    def operation_list_btn(self):
        '''点击操作下拉箭头'''
        self.click(self.operation_list_loc)

    def apply_btn(self):
        '''点击apply'''
        self.click(self.apply_filter_loc)

    def quick_filter_steps(self,value="2"):
        '''添加快速过滤器流程'''
        self.add_filter_btn()
        self.quick_btn()
        self.input_filter_value(value)
        self.operation_list_btn()
        self.apply_btn()

    def get_filter_value(self):
        '''获取过滤值'''
        try:
            t = self.find_element(self.result_filter_loc).text
            return t
        except:
            print("获取过滤值失败，返回空字符")
            return ""


class Add_Basic_Filter(BasePage):
    '''添加普通过滤器'''
    add_filter_loc = ("css selector", ".basic-filter__icon.iconfont.icon-dropdown")
    basic_loc = ("xpath",".//*[@id='collapse']/div/div[1]/ul/li[2]/a")
    add_btn_loc = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/div/div/button")
    field_list_loc = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[1]/div[2]/div/div[1]")
    field_loc = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[1]/div[2]/div/div[2]/div/div/div[2]/div")
    operation_list_loc = ("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[2]/div/div[1]")
    operation_loc =("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[2]/div/div[2]/div/div/div[2]/div/span")
    input_loc =("xpath",".//*[@id='collapse']/div/div[1]/div/div[2]/ul/li/div[3]/div/div/div/textarea")
    apply_filter_loc = ("id", "refresh-filter")
    result_filter_loc = ("xpath", ".//*[@id='table']/tbody/tr[1]/td[2]")

    def add_fitler_btn(self):
        '''点击过滤器按钮'''
        self.click(self.add_filter_loc)

    def basic_btn(self):
        '''点击过滤器中Basic按钮'''
        self.click(self.basic_loc)

    def add_btn(self):
        '''点击快速过滤器 +'''
        self.click(self.add_btn_loc)

    def select_a_field(self):
        '''点击字段选择下拉框'''
        self.click(self.field_list_loc)

    def field(self):
        '''选择字段'''
        self.click(self.field_loc)

    def select_an_operation(self):
        '''点击计算方式下拉框'''
        self.click(self.operation_list_loc)

    def operation(self):
        '''选择计算方式'''
        self.click(self.operation_loc)

    def input_filter_value(self,value):
        '''输入筛选值'''
        self.send_keys(self.input_loc,value)

    def apply_filter_btn(self):
        '''点击apply按钮'''
        self.click(self.apply_filter_loc)

    def basic_filter_steps(self,value="0006981"):
        '''添加普通过滤器流程'''
        self.add_fitler_btn()
        self.basic_btn()
        self.add_btn()
        self.select_a_field()
        self.field()
        self.select_an_operation()
        self.operation()
        self.input_filter_value(value)
        self.apply_filter_btn()

    def get_filter_value(self):
        '''获取过滤值'''
        try:
            t = self.find_element(self.result_filter_loc).text
            return t
        except:
            print("获取过滤值失败，返回空字符")
            return ""


class Favorite_Report(BasePage):
    '''收藏报表'''
    favorite_btn_loc = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[1]/div/div/div/button[1]")
    report_name_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/form/div[1]/input")
    OK_Cancel_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[2]")
    favorite_icon_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[1]/header/div[3]/div[1]/i")
    favorit_report_loc = ("xpath",".//*[text()='my detail']")
    favorit_report_title = ("css selector",".box-title.container__title.ng-binding.ng-scope")

    def favorite_btn(self):
        '''点击收藏按钮'''
        self.click(self.favorite_btn_loc)

    def input_rpt_name(self,text):
        '''填写收藏报表名称'''
        self.send_keys(self.report_name_loc,text)

    def OK_or_Cancel(self):
        '''点击OK或Cancel按钮'''
        self.click(self.OK_Cancel_btn_loc)

    def favorite_icon(self):
        '''点击已收藏图标'''
        self.click(self.favorite_icon_loc)

    def open_favorite_rpt(self):
        '''打开收藏报表'''
        self.click(self.favorit_report_loc)

    def favorite_steps(self,text = "my detail"):
        '''收藏报表流程'''
        self.favorite_btn()
        self.input_rpt_name(text)
        self.OK_or_Cancel()
        self.favorite_icon()
        self.open_favorite_rpt()

    def get_favorite_title(self):
        '''获取收藏报表名称'''
        try:
            t = self.find_element(self.favorit_report_title).text
            return t
        except:
            print("获取收藏报表名称失败，返回空字符")
            return ""


class Pop_out(BasePage):
    '''弹出报表'''
    pop_loc = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[1]/div/div/div/button[2]")

    def pop_btn(self):
        '''点击弹出按钮'''
        self.click(self.pop_loc)

    def handles(self):
        '''获取句柄'''
        self.get_handles()


class Export_Report(BasePage):
    '''导出报表'''
    exp_btn_loc = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[1]/div/div/div/button[3]")
    rpt_title_loc =("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div/div[2]/div[1]/input")
    file_type_list_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]")
    file_type_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div")
    exp_cancle_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div/div[3]/button[2]")
    exp_download_loc = ("xpath",".//*[@href='#Download']")
    close_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div/div[1]/button")

    def exp_btn(self):
        '''点击导出按钮'''
        self.click(self.exp_btn_loc)

    def input_rpt_title(self,text):
        '''输入导出标题'''
        self.send_keys(self.rpt_title_loc,text)

    def file_type_list(self):
        '''点击报表类型list'''
        self.click(self.file_type_list_loc)

    def select_file_type(self):
        '''选择导出报表类型'''
        self.click(self.file_type_loc)

    def exp_cancel_btn(self):
        '''点击导出或取消按钮'''
        self.click(self.exp_cancle_btn_loc)

    def ept_steps(self,text="my export report"):
        '''导出报表流程'''
        self.exp_btn()
        self.input_rpt_title(text)
        self.file_type_list()
        self.select_file_type()
        self.exp_cancel_btn()

    def download_info(self):
        '''获取下载信息'''
        try:
            t = self.find_element(self.exp_download_loc).text
            return t
        except:
            print("获取下载信息失败，返回空字符")
            return ""

    def close_btn(self):
        '''点击关闭按钮'''
        self.click(self.close_btn_loc)


class Sort_Column(BasePage):
    '''字段排序'''
    options_loc = ("css selector",".iconfont.icon-setting")
    sort_loc = ("xpath",".//*[text()='Sort']")
    column_name_list_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[2]/div/div[1]/div/div[1]")
    column_name_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[4]/div")
    # sort_order_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[2]/div/div[2]/label[2]/i")
    update_cancel_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[2]")
    sort_result_loc = ("xpath",".//*[@id='table']/tbody/tr[1]/td[4]")

    def options(self):
        '''点击options按钮'''
        self.click(self.options_loc)

    def select_sort(self):
        '''点击排序功能'''
        self.click(self.sort_loc)

    def column_name_list(self):
        '''点击列名list'''
        self.click(self.column_name_list_loc)

    def column_name(self):
        '''选择一个列名'''
        self.click(self.column_name_loc)

    #def sort_order(self):
        '''点击选择排序规则'''
        #self.click(self.sort_order_loc)

    def update_cancel_btn(self):
        '''点击更新或取消排序'''
        self.click(self.update_cancel_btn_loc)

    def sort_steps(self):
        '''排序流程'''
        self.options()
        self.select_sort()
        self.column_name_list()
        self.column_name()
        # self.sort_order()
        self.update_cancel_btn()

    def sort_result(self):
        '''获取排序结果'''
        try:
            t = self.find_element(self.sort_result_loc).text
            return t
        except:
            print("排序失败，返回空字符")
            return ""


class Group_Column(BasePage):
    '''字段分组'''
    options_loc = ("css selector",".iconfont.icon-setting")
    group_loc = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[1]/div/div/div/div/div/div[2]")
    column_name_list_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[2]/div/div/div/div[1]")
    column_name_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[4]/div")
    update_cancel_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[2]")
    group_result_loc = ("xpath",".//*[@id='table']/tbody/tr[1]/td[3]")

    def options(self):
        '''点击options按钮'''
        self.click(self.options_loc)

    def select_group(self):
        '''点击分组'''
        self.click(self.group_loc)

    def column_name_list(self):
        '''点击列名列表'''
        self.click(self.column_name_list_loc)

    def column_name(self):
        '''选择分组列名'''
        self.click(self.column_name_loc)

    def update_cancel_btn(self):
        '''点击更新或需取消分组'''
        self.click(self.update_cancel_btn_loc)

    def group_steps(self):
        '''分组流程'''
        self.options()
        self.select_group()
        self.column_name_list()
        self.column_name()
        self.update_cancel_btn()

    def group_result(self):
        '''分组结果'''
        try:
            t = self.find_element(self.group_result_loc).text
            return t
        except:
            print("分组失败，返回空字符")
            return ""


class Rearrange_Columns_to_left(BasePage):
    '''分组排序中隐藏一个字段'''
    options_loc = ("css selector",".iconfont.icon-setting")
    rearrange_columns_loc = ("xpath",".//*[text()='Re-Arrange Columns']")
    selected_columns_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[3]/div[3]/select/option[1]")
    to_left_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[2]/i[3]")
    cancel_update_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[2]")
    column_to_left_result_loc = ("xpath",".//*[text()='member_id']")

    def options(self):
        '''点击options'''
        self.click(self.options_loc)

    def rearrange_clolumns(self):
        '''点击分组排序'''
        self.click(self.rearrange_columns_loc)

    def select_columns(self):
        '''选择字段'''
        self.click(self.selected_columns_loc)

    def to_left(self):
        '''将选择的字段从右移到左侧'''
        self.click(self.to_left_loc)

    def update_cancel_btn(self):
        '''点击更新或取消分组排序'''
        self.click(self.cancel_update_btn_loc)

    def rearrane_column_to_left_steps(self):
        '''隐藏一个列'''
        self.options()
        self.rearrange_clolumns()
        self.select_columns()
        self.to_left()
        self.update_cancel_btn()

    def column_to_left_result(self):
        '''隐藏列之后的结果'''
        try:
            t = self.find_element(self.column_to_left_result_loc).text
            return t
        except:
            print("无法定位元素，列已成功被隐藏，返回空字符")
            return ""


class Rearrange_all_columns_to_left(BasePage):
    '''分组排序中隐藏所有字段'''
    options_loc = ("css selector",".iconfont.icon-setting")
    rearrange_columns_loc = ("xpath",".//*[text()='Re-Arrange Columns']")
    go_left_all_loc = ("xpath",".//*[@ng-click='go_left_all()']")
    cancel_update_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[2]")
    warning_loc = ("xpath",".//*[@id='toast-container']/div/div/div/div")
    close_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[1]/button")

    def options(self):
        '''点击options'''
        self.click(self.options_loc)

    def rearrange_clolumns(self):
        '''点击分组排序'''
        self.click(self.rearrange_columns_loc)

    def go_left_all(self):
        '''点击左移所有字段'''
        self.click(self.go_left_all_loc)

    def cancel_update_btn(self):
        '''点击更新或取消分组排序'''
        self.click(self.cancel_update_btn_loc)

    def all_column_to_left_steps(self):
        '''隐藏所有字段'''
        self.options()
        self.rearrange_clolumns()
        self.go_left_all()
        self.cancel_update_btn()

    def warning_show(self):
        '''提示必须选择一个字段'''
        try:
            t = self.find_element(self.warning_loc).text
            return t
        except:
            print("隐藏成功，返回空字符")
            return ""

    def close_btn(self):
        '''点击关闭按钮'''
        self.click(self.close_btn_loc)


class Rearrange_Columns_to_right(BasePage):
    '''分组排序从左往右移，报表只显示一个字段'''
    options_loc = ("css selector",".iconfont.icon-setting")
    rearrange_columns_loc = ("xpath",".//*[text()='Re-Arrange Columns']")
    go_left_all_loc = ("xpath",".//*[@ng-click='go_left_all()']")
    selected_columns_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[1]/div[3]/select/option[3]")
    to_right_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[2]/i[2]")
    cancel_update_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[2]")
    column_to_right_result_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[2]/div[1]/span")

    def options(self):
        '''点击options'''
        self.click(self.options_loc)

    def rearrange_clolumns(self):
        '''点击分组排序'''
        self.click(self.rearrange_columns_loc)

    def go_left_all(self):
        '''点击左移所有字段'''
        self.click(self.go_left_all_loc)

    def select_columns(self):
        '''选择字段'''
        self.click(self.selected_columns_loc)

    def to_right(self):
        '''将选择的字段从左往右移'''
        self.click(self.to_right_loc)

    def cancel_update_btn(self):
        '''点击应用或取消按钮'''
        self.click(self.cancel_update_btn_loc)

    def rearrane_column_to_right_steps(self):
        '''在报表中显示所选列的流程'''
        self.options()
        self.rearrange_clolumns()
        self.go_left_all()
        self.select_columns()
        self.to_right()
        self.cancel_update_btn()

    def column_to_right_result(self):
        '''显示所选列的结果'''
        try:
            t = self.find_element(self.column_to_right_result_loc).text
            return t
        except:
            print("显示列失败，返回空字符")
            return ""


class Rearrange_all_columns_to_right(BasePage):
    '''通过分组排序显示报表中的所有列'''
    options_loc = ("css selector",".iconfont.icon-setting")
    rearrange_columns_loc = ("xpath",".//*[text()='Re-Arrange Columns']")
    selected_columns_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[3]/div[3]/select/option[1]")
    to_left_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[2]/i[3]")
    cancel_update_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[2]")
    all_to_right_loc = ("xpath",".//*[@ng-click='go_right_all()']")
    all_columns_result_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[6]/div[1]/span")

    def options(self):
        '''点击options按钮'''
        self.click(self.options_loc)

    def rearrange_columns(self):
        '''点击分组排序'''
        self.click(self.rearrange_columns_loc)

    def select_columns(self):
        '''选择需要隐藏的字段'''
        self.click(self.selected_columns_loc)

    def to_left(self):
        '''将选择的字段从右移到左侧'''
        self.click(self.to_left_loc)

    def update_cancel_btn(self):
        '''点击更新或取消分组排序'''
        self.click(self.cancel_update_btn_loc)

    def all_to_right(self):
        '''分组排序中，报表中显示所有列'''
        self.click(self.all_to_right_loc)

    def all_columns_to_right_steps(self):
        '''分组排序显示所有列流程'''
        self.options()
        self.rearrange_columns()
        self.select_columns()
        self.to_left()
        self.update_cancel_btn()
        time.sleep(3)
        self.options()
        self.rearrange_columns()
        self.all_to_right()
        self.update_cancel_btn()

    def all_to_right_result(self):
        '''分组排序显示所有列之后的结果'''
        try:
            t = self.find_element(self.all_columns_result_loc).text
            return t
        except:
            print("显示所有列失败，返回空字符")
            return ""


class Rearrange_cancel(BasePage):
    '''取消分组排序'''
    options_loc = ("css selector",".iconfont.icon-setting")
    rearrange_columns_loc = ("xpath",".//*[text()='Re-Arrange Columns']")
    selected_columns_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[3]/div[3]/select/option[1]")
    to_left_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[2]/div[2]/i[3]")
    cancel_update_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[1]")
    cancel_rearrange_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[2]/div[1]/span")

    def options(self):
        '''点击options按钮'''
        self.click(self.options_loc)

    def rearrange_clolumns(self):
        '''点击分组排序'''
        self.click(self.rearrange_columns_loc)

    def select_columns(self):
        '''选择字段'''
        self.click(self.selected_columns_loc)

    def to_left(self):
        '''将选择的字段从右移到左侧'''
        self.click(self.to_left_loc)

    def cancel_update_btn(self):
        '''点击更新或取消分组排序'''
        self.click(self.cancel_update_btn_loc)

    def cancel_rearrange_steps(self):
        '''点击取消分组排序'''
        self.options()
        self.rearrange_clolumns()
        self.select_columns()
        self.to_left()
        self.cancel_update_btn()

    def cancel_rearrange_result(self):
        '''取消分组排序后的结果'''
        try:
            t = self.find_element(self.cancel_rearrange_loc).text
            return t
        except:
            print("取消分组排序失败，返回空字符")
            return ""


class Hide_Column(BasePage):
    '''隐藏列'''
    dropdown_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[2]/div[1]/i[3]")
    hide_loc = ("xpath",".//*[@class='ltHide']")
    hide_column_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[2]/div[1]/span")

    def move_to_hide_column(self):
        '''点击需要隐藏的列'''
        self.move_to_element(self.hide_column_loc)

    def click_dropdown_btn(self):
        '''点击下拉箭头'''
        js = 'document.getElementsByClassName("iconfont icon-arrow-down-radius-fill js_dropdown")[0].click();'
        self.driver.execute_script(js)

    def hide_btn(self):
        '''点击隐藏'''
        js = 'document.getElementsByClassName("ltHide")[0].click();'
        self.driver.execute_script(js)

    def hide_steps(self):
        '''隐藏列流程'''
        self.move_to_hide_column()
        self.click_dropdown_btn()
        self.hide_btn()

    def hide_result(self):
        '''获取隐藏后的结果'''
        try:
            t = self.find_element(self.hide_column_loc).text
            return t
        except:
            print("隐藏失败，返回空字符")
            return ""


class Group_cloumn_on_column(BasePage):
    '''从字段处分组'''
    column_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[2]/div[1]/span")
    dropdown_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[2]/div[1]/i[3]")
    group_loc = ("xpath",".//*[@id='group']/li/button[3]")
    update_cancel_btn_loc = ("xpath",".//*[@id='Aboard']/body/div[1]/div/div/div[3]/button[2]")
    group_result_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[2]/div[1]/span")

    def move_to_group_column(self):
        '''鼠标悬停至要分组的字段'''
        self.move_to_element(self.column_loc)

    def click_dropdown_btn(self):
        '''点击下拉箭头'''
        js = 'document.getElementsByClassName("iconfont icon-arrow-down-radius-fill js_dropdown")[0].click();'
        self.driver.execute_script(js)

    def group_btn(self):
        '''点击分组'''
        js = 'document.querySelectorAll("#group>li>button")[2].click();'
        self.driver.execute_script(js)

    def update_cancel_btn(self):
        '''点击更新或取消分组'''
        self.click(self.update_cancel_btn_loc)

    def group_field_steps(self):
        '''分组流程'''
        self.move_to_group_column()
        self.click_dropdown_btn()
        self.group_btn()
        self.update_cancel_btn()

    def group_result(self):
        '''获取分组结果'''
        try:
            t = self.find_element(self.group_result_loc).text
            return t
        except:
            print("分组失败，返回空字符")
            return ""


class Go_Next_Page(BasePage):
    '''跳转到下一页'''
    next_page_loc = ("css selector",".iconfont.icon-arrow-right-line")
    page_value_loc = ("xpath",".//*[@id='summary-div']/div/div/div[3]/div/span")

    def next_page(self):
        '''点击下一页'''
        self.click(self.next_page_loc)

    def next_page_result(self):
        '''获取下一页文本结果'''
        try:
            t = self.find_element(self.page_value_loc).text
            return t
        except:
            print("获取下一页文本结果失败，返回空字符")
            return ""


class Go_Last_Page(BasePage):
    '''跳转到最后一页'''
    last_page_loc = ("css selector",".iconfont.icon-pager-end")
    last_page_result_loc = ("xpath",".//*[@id='summary-div']/div/div/div[3]/div/span")

    def last_page(self):
        '''点击最后一页'''
        self.click(self.last_page_loc)

    def last_page_result(self):
        '''获取跳转最后一页结果'''
        try:
            t = self.find_element(self.last_page_result_loc).text
            return t
        except:
            print("获取跳转最后一页文本结果失败，返回空字符")
            return ""


class Go_Previous_Page(BasePage):
    '''跳转到前一页'''
    last_page_loc = ("css selector",".iconfont.icon-pager-end")
    previous_page_loc = ("css selector",".iconfont.icon-arrow-left-line")
    previous_page_result_loc = ("xpath",".//*[@id='summary-div']/div/div/div[3]/div/span")

    def last_page(self):
        '''跳转到最后一页'''
        self.click(self.last_page_loc)

    def previous_page(self):
        self.click(self.previous_page_loc)

    def go_previous_page_steps(self):
        '''跳转到前一页流程'''
        self.last_page()
        time.sleep(3)
        self.previous_page()

    def previous_page_result(self):
        '''跳转到前一页结果'''
        try:
            t = self.find_element(self.previous_page_result_loc).text
            return t
        except:
            print("获取跳转到前一页文本结果失败，返回空字符")
            return ""


class Go_First_Page(BasePage):
    '''跳转到第一页'''
    last_page_loc = ("css selector",".iconfont.icon-pager-end")
    first_page_loc = ("css selector",".iconfont.icon-pager-first")
    first_page_result_loc = ("xpath",".//*[@id='summary-div']/div/div/div[3]/div/span")

    def last_page(self):
        '''跳转到最后一页'''
        self.click(self.last_page_loc)

    def first_page(self):
        '''跳转到第一页'''
        self.click(self.first_page_loc)

    def go_first_page_steps(self):
        '''跳转到第一页流程'''
        self.last_page()
        time.sleep(3)
        self.first_page()

    def first_page_result(self):
        '''获取跳转到第一页结果'''
        try:
            t = self.find_element(self.first_page_result_loc).text
            return t
        except:
            print("获取跳转到第一页结果失败，返回空字符")
            return ""


class Go_Specified_Page(BasePage):
    '''跳转到指定页码'''
    go_page_loc=("css selector","#go")
    specified_page_result_loc=("xpath",".//*[@id='summary-div']/div/div/div[3]/div/span")

    def input_specified_page(self,text="2"):
        '''输入指定页码'''
        self.send_keys(self.go_page_loc,text)

    def enter_specified_page(self):
        '''进入指定页码'''
        self.find_element(self.go_page_loc).send_keys(Keys.ENTER)

    def go_to_specified_page_steps(self):
        '''跳转到指定页码流程'''
        self.input_specified_page()
        self.enter_specified_page()

    def specified_page_result(self):
        '''获取跳转指定页面结果'''
        try:
            t = self.find_element(self.specified_page_result_loc).text
            return t
        except:
            print("获取跳转指定页面结果失败，返回空字符")
            return ""


class Display_Rows_Per_Page(BasePage):
    '''每页显示数据行数'''
    down_arrow_loc = ("xpath",".//*[@id='summary-div']/div/div/div[5]/div[1]/ul/li/span/b")
    row_loc = ("xpath",".//*[@id='summary-div']/div/div/div[5]/div[1]/ul/li/ul/li[2]/a")
    display_rows_result_loc = ("xpath",".//*[@id='summary-div']/div/div/div[5]/div[1]/ul/li/span/i")

    def down_arrow(self):
        '''点击下拉框箭头'''
        self.click(self.down_arrow_loc)

    def select_row(self):
        '''选择数据行数'''
        self.click(self.row_loc)

    def display_rows_steps(self):
        '''显示数据行数流程'''
        self.down_arrow()
        self.select_row()

    def display_rows_result(self):
        '''获取显示数据行数结果'''
        try:
            t = self.find_element(self.display_rows_result_loc).text
            return t
        except:
            print("获取结果失败，返回空字符")
            return ""


class Display_Selected_Rows(BasePage):
    '''显示勾选行'''
    row_1_loc = ("xpath",".//*[@id='table']/tbody/tr[1]/td[1]/input")
    row_2_loc = ("xpath",".//*[@id='table']/tbody/tr[2]/td[1]/input")
    row_3_loc = ("xpath",".//*[@id='table']/tbody/tr[3]/td[1]/input")
    dropdown_arrow_loc = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[3]/div[1]/div/i")
    selected_rows_loc = ("xpath",".//*[text()='Only Selected Rows']")
    display_selected_result_loc = ("xpath",".//*[@id='table']/tbody/tr[4]/td[2]")

    def row_1_checkbox(self):
        '''勾选第一行'''
        self.click(self.row_1_loc)

    def row_2_checkbox(self):
        '''勾选第二行'''
        self.click(self.row_2_loc)

    def row_3_checkbox(self):
        '''勾选第三行'''
        self.click(self.row_3_loc)

    def dropdown_arrow(self):
        '''点击下拉框箭头'''
        self.click(self.dropdown_arrow_loc)

    def only_selected_rows(self):
        '''点击显示勾选行'''
        self.click(self.selected_rows_loc)

    def display_selected_steps(self):
        '''显示勾选行流程'''
        self.row_1_checkbox()
        self.row_2_checkbox()
        self.row_3_checkbox()
        self.dropdown_arrow()
        self.only_selected_rows()

    def display_selected_result(self):
        '''获取显示勾选行结果'''
        try:
            t = self.find_element(self.display_selected_result_loc).text
            return t
        except:
            print("获取结果失败，返回空字符")
            return ""


class Hide_Selected_Rows(BasePage):
    '''隐藏勾选行'''
    row_1_loc = ("xpath",".//*[@id='table']/tbody/tr[1]/td[1]/input")
    row_2_loc = ("xpath",".//*[@id='table']/tbody/tr[2]/td[1]/input")
    row_3_loc = ("xpath",".//*[@id='table']/tbody/tr[3]/td[1]/input")
    dropdown_arrow_loc = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[3]/div[1]/div/i")
    hide_selected_rows_loc = ("xpath",".//*[text()='Hide Selected Rows']")
    hide_selected_result_loc = ("xpath",".//*[@id='table']/tbody/tr[11]/td[2]")

    def row_1_checkbox(self):
        '''勾选第一行'''
        self.click(self.row_1_loc)

    def row_2_checkbox(self):
        '''勾选第二行'''
        self.click(self.row_2_loc)

    def row_3_checkbox(self):
        '''勾选第三行'''
        self.click(self.row_3_loc)

    def dropdown_arrow(self):
        '''点击下拉框箭头'''
        self.click(self.dropdown_arrow_loc)

    def hide_selected_rows(self):
        '''点击隐藏勾选行'''
        self.click(self.hide_selected_rows_loc)

    def hide_selected_steps(self):
        '''隐藏勾选行流程'''
        self.row_1_checkbox()
        self.row_2_checkbox()
        self.row_3_checkbox()
        self.dropdown_arrow()
        self.hide_selected_rows()

    def hide_selected_result(self):
        '''获取隐藏勾选行结果'''
        try:
            t = self.find_element(self.hide_selected_result_loc).text
            return t
        except:
            print("获取结果失败，返回空字符")
            return ""


class Display_All(BasePage):
    '''显示所有行'''
    row_1_loc = ("xpath",".//*[@id='table']/tbody/tr[1]/td[1]/input")
    row_2_loc = ("xpath",".//*[@id='table']/tbody/tr[2]/td[1]/input")
    row_3_loc = ("xpath",".//*[@id='table']/tbody/tr[3]/td[1]/input")
    dropdown_arrow_loc = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[3]/div[1]/div/i")
    hide_selected_rows_loc = ("xpath",".//*[text()='Hide Selected Rows']")
    display_all_loc = ("xpath",".//*[text()='Display All']")
    all_rows_result_loc = ("xpath",".//*[@id='table']/tbody/tr[11]/td[2]")

    def row_1_checkbox(self):
        '''勾选第一行'''
        self.click(self.row_1_loc)

    def row_2_checkbox(self):
        '''勾选第二行'''
        self.click(self.row_2_loc)

    def row_3_checkbox(self):
        '''勾选第三行'''
        self.click(self.row_3_loc)

    def dropdown_arrow(self):
        '''点击下拉框箭头'''
        self.click(self.dropdown_arrow_loc)

    def hide_selected_rows(self):
        '''点击隐藏勾选行'''
        self.click(self.hide_selected_rows_loc)

    def display_all(self):
        '''点击显示所有行'''
        self.click(self.display_all_loc)

    def display_all_steps(self):
        '''显示所有行流程'''
        self.row_1_checkbox()
        self.row_2_checkbox()
        self.row_3_checkbox()
        self.dropdown_arrow()
        self.hide_selected_rows()
        self.dropdown_arrow()
        self.display_all()

    def display_all_result(self):
        '''获取显示所有行结果'''
        try:
            t = self.find_element(self.all_rows_result_loc).text
            return t
        except:
            print("获取结果失败，返回空字符")
            return ""


class Sort_on_Cloumn_Asc(BasePage):
    '''在字段列升序排列'''
    column_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[2]/div[1]/span")
    update_btn_loc = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[2]/div/button")
    sort_asc_result_loc = ("xpath",".//*[@id='table']/tbody/tr[1]/td[2]")

    def column_name(self):
        '''点击字段名'''
        self.click(self.column_loc)

    def update_btn(self):
        '''点击更新按钮'''
        self.click(self.update_btn_loc)

    def sort_asc_steps(self):
        '''生序排列流程'''
        self.column_name()
        self.update_btn()

    def sort_asc_result(self):
        '''获取升序排列结果'''
        try:
            t = self.find_element(self.sort_asc_result_loc).text
            return t
        except:
            print("获取结果失败，返回空字符")
            return ""


class Sort_on_Cloumn_Dsc(BasePage):
    '''在字段处降序排列'''
    column_loc = ("xpath",".//*[@id='table-sticky-header']/tr/th[2]/div[1]/span")
    update_btn_loc = ("xpath",".//*[@id='inner-container']/div[2]/ng-switch/div/div/div/div[2]/div/button")
    sort_dsc_result_loc = ("xpath",".//*[@id='table']/tbody/tr[1]/td[2]")

    def column_name(self):
        '''点击字段名'''
        self.click(self.column_loc)

    def update_btn(self):
        '''点击更新按钮'''
        self.click(self.update_btn_loc)

    def sort_dsc_steps(self):
        '''生序排列流程'''
        self.column_name()
        self.column_name()
        self.update_btn()

    def sort_dsc_result(self):
        '''获取升序排列结果'''
        try:
            t = self.find_element(self.sort_dsc_result_loc).text
            return t
        except:
            print("获取结果失败，返回空字符")
            return ""


if __name__ == "__main__":
    driver = webdriver.Firefox()
    url = "https://demo.jintelhealth.com/Analytics/#!/login"
    username = "lz_admin"
    psw = "Ghc2018!"
    login = LoginPage(driver)
    login.login_process(url,username,psw)
    rpt = Open_Report(driver)
    rpt.open_steps()
    time.sleep(3)
    sort_dsc = Sort_on_Cloumn_Dsc(driver)
    sort_dsc.sort_dsc_steps()
    result = sort_dsc.sort_dsc_result()
    print(result)








