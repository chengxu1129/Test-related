#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :weather.py
# @Time      :2021/10/5 16:11
# @Author    :never.cheng
import demjson
import requests
import json



def achieveWeather(url):
    resp=requests.get(url)
    resp.encoding='utf-8'
    text=resp.json()
    maxRH,minRH =text['DYN_DAT_MINDS_FND']['Day3MaxRH'],text['DYN_DAT_MINDS_FND']['Day3MinRH']
    return f'相对湿度{minRH["Val_Chi"]}-{maxRH["Val_Chi"]}%'


if __name__ == '__main__':
    url = 'https://www.hko.gov.hk/json/DYN_DAT_MINDS_FND.json?1633586278199'
    RH=achieveWeather(url)
    print(RH)


