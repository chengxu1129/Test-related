# -*- encoding: utf-8 -*-
"""
@File    : base001.py
@Time    : 2020/7/9 19:11
@Author  : Never.cheng
@Email   : chengxu@hst.com
@Software: PyCharm
"""


from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.quit()