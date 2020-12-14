#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Never.cheng
@file:main.py
@time:2020/10/15
"""
import os
import sys
import time
import shutil
project_path=os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path)


def mk_report_dir():
    repoet=object()
    #创建测试报告目录
    report_path=os.path.join(project_path,'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    #每次的测试报告
    report_dir_path = os.path.abspath('{0}/{1}'.format(report_path, time.strftime("%Y-%m-%d", time.localtime())))
    if not os.path.exists(report_dir_path):
        os.mkdir(report_dir_path)
    #临时生成的文件
    xml_tmp_path = os.path.join(report_dir_path, "xml_tmp_dir")
    if not os.path.exists(xml_tmp_path):
        os.mkdir(xml_tmp_path)
    #html报告
    now_time = time.strftime("%H%M%S", time.localtime())
    allure_report_path = os.path.join(report_dir_path, "AllureReport{}".format(now_time))
    if not os.path.exists(allure_report_path):
        os.mkdir(allure_report_path)

    return xml_tmp_path,allure_report_path

#生成html报告
def mk_allure_report(xml_tmp_path,allure_report_path):
    #os.system(f"allure generate {xml_tmp_path} -o {allure_report_path} -c")
    os.system("allure generate {0} -o {1} -c".format(xml_tmp_path,allure_report_path))
    shutil.rmtree(xml_tmp_path)
    #os.system(f'allure open {allure_report_path}')

#生成json
def create_report_xml(xml_tmp_path):



    os.system("python -m  pytest Case --alluredir={}".format(xml_tmp_path))





#完整流程

def report_all():
    xml_tmp_path, allure_report_path = mk_report_dir()
    create_report_xml(xml_tmp_path)
    if os.listdir(xml_tmp_path):
        mk_allure_report(xml_tmp_path,allure_report_path)


if __name__ == '__main__':
    report_all()
