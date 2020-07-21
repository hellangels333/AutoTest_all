# -*- coding: utf-8 -*-
# __author__ = "maple"

import pytest
import allure
from lib.ExcelHandler import ExcelHandler
from lib.RequestHandler import RequestHandler
from lib.AllureHandler import AllureHandler
from lib.EmailHandler import EmailHandler

'''
这是一个测试套

1. 拿到Excel数据
2. 发请求
3. 生成测试用例报告
4. 发邮件
5. 断言

'''


class Test_case(object):
    @pytest.mark.parametrize('case', ExcelHandler().get_excel_data)
    def test_case(self, case):
        """  执行断言 """
        # print(case)
        # 发请求
        response = RequestHandler(case).get_response

        # 制作 allure 报告
        allure.dynamic.title(case['case_project'])
        allure.dynamic.description('<font color="red">请求URL：</font>{}<br />'
                                   '<font color="red">期望值：</font>{}'.format(case['case_url'], case['case_description']))
        allure.dynamic.feature(case['case_project'])
        allure.dynamic.story(case['case_method'])
        assert response[0] == response[1]
        # print("-"*30)
        # print(response)
        # print(response[0])
        # print(response[1])
        # print("-"*30)

    def teardown_class(self):
        """  执行alllure命令 """

        AllureHandler().execute_command()
        # 发邮件
        EmailHandler().send_email()

# a = Test_case()
# a.test_case()