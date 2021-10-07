#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test1.py
# @Time      :2021/10/5 14:17
# @Author    :never.cheng


from selenium import webdriver
import pytest


USDC='//*[@id="app"]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[4]'
Trade='//*[@id="app"]/div[1]/div/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[7]/div/button'
Buy='//div[contains(text(), "Buy")]'
class TestUI:

    def setup_class(self):
        print(1)
        self.driver=webdriver.Chrome()
        self.driver.get('https://crypto.com/exchange')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)



    def test_a(self):
        self.driver.find_element_by_xpath(USDC).click()
        self.driver.find_element_by_xpath(Trade).click()
        buy=self.driver.find_element_by_xpath(Buy)
        assert buy=='Buy'

    def teardown_class(self):
        print("---finish---")


if __name__ == '__main__':
    pytest.main(["-s", "test1.py"])


