#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Never.cheng
@file:Juggle.py
@time:2020/09/15
"""
from lib.Public import Public
from lib import Element, path
from selenium.webdriver.common.action_chains import ActionChains  # 拓展其他的行为
from time import sleep

import time

import win32api   #模拟键盘事件
import win32con   #控制键盘
import pyperclip  #拷贝粘贴字符串

'''
//*[@id="search_widget"]/div[1]/div/input
'''

#搜索按钮
sousuobutton001='//*[@id="workspace"]/div/div/div[2]/div[1]'
chancebutton001 = '//div/input[@placeholder="搜索积木"]'
fanyi = '//div[contains(text(), "翻译")]'

#全部声音我的素材
musicsucai='document.querySelector("#material-dialog > div.th1-bg-9.material-content-wrap--2j9qP").scrollTop=10000'
#主界面的声音按钮
music001 = '//div[contains(text(), "声音")]'
#+声音按钮
music002='//div[@data-report-click="声音-添加声音"]'
#素材库按钮
music003='//div[@data-report-click="声音-素材库添加"]'
#全部我的素材库
music004='//*[@id="material-dialog"]/div[3]'
#愉快的时刻=
music005='//div[contains(text(), "愉悦的时刻")]'
#删除愉快的音乐
delete_music='//div[@data-report-click="声音-删除"]'
#新音乐
newmusic='//div[contains(text(), "新音乐")]'
#确认添加
music006='//div[contains(text(), "确认添加(1)")]'
#声音-音乐画板添加
music007='//div[@data-report-click="声音-音乐画板添加"]'
#画布
music008='//*[@id="music-painter"]/div/div[2]/div[1]/div[1]/div[5]/canvas[2]'
#保存
music009='//*[@id="music-painter"]/div/div[2]/div[2]/div[2]/button[1]'

musicend='//div/h6[contains(text(), "已保存到声音栏")]'

#离开
music0010='//*[@id="music-painter"]/div/div[2]/div[2]/div[2]/button[2]'

#录音
music0011='//div[@data-report-click="声音-录音添加"]'
#点击录制
music0012='//div[@data-report-click="声音-开始录音"]'
#关闭录音
music0013='//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[2]'
#导入声音
music0014='//div[@data-report-click="声音-本地导入"]'

'''
    音量的起始 763 293
    音量最大位置 941 293
'''

#添加的music
show001='//div[contains(text(), "music")]'
#删除声音按钮
show002='//div[@data-report-click="声音-删除"]'
#声音播放按钮
show003='//div[@data-report-click="声音-播放"]'
#向下更多按钮
show004='//div[@data-report-click="声音-播放"]/following-sibling::div[1]'
#音乐文件名字
show005='//input[@type="text" and @maxlength="20"]'
#修改名称
show006='//div[@data-report-click="声音-右键改名"]'




#主界面变量
variable001='//div[contains(text(), "变量")]'
#+变量
variable002='//div/span[contains(text(), "变量")]'
#输入变量名
variable003='//input[@placeholder="请输入变量名称"]'
#确定按钮
variable004='//div[@data-report-click="变量-确认新建"]'
#新增的变量
variable005='//div[contains(text(), "name")]'
#隐藏/显示按钮
variable006='//*[@id="variable_widget"]/div[2]/div[2]/div[2]/div/div[2]/div[2]'
#﹀按钮
variable007='//*[@id="variable_widget"]/div[2]/div[2]/div[2]/div/div[2]/div[3]'
#修改变量名
variable008='//input[@type="text" and @maxlength="20"]'
#删除
variable0010='//*[@id="variable_widget"]/div[2]/div[2]/div[2]/div/div[2]/div[1]'

#主界面的列表
list001='//div[contains(text(), "列表")]'
#+列表
list002='//div/span[contains(text(), "列表")]'
#请输入列表名称
list003='//input[@placeholder="请输入列表名称"]'
#确定按钮
list004='//div[@data-report-click="列表-确认新建"]'
#新增的列表
list005='//div[contains(text(), "list")]'
#显示/隐藏
list006='//*[@id="list_widget"]/div[2]/div[2]/div[2]/div/div[2]/div[2]'
#更多
list007='//*[@id="list_widget"]/div[2]/div[2]/div[2]/div/div[2]/div[3]'
#+号
list008='//div[@data-report-click="列表-添加列表项"]'
#列表
list009='//input[@data-report-click="列表-输入值"]'
#点击保存
list0010='//div[@data-report-click="列表-保存"]'
#修改名称
list0011='//div[@data-report-click="列表-改名"]'
#列表名称输入框
# list0012='//div[contains(text(), "list")]/following-sibling::div[1]'
list0012='//*[@id="list_widget"]/div[2]/div[2]/div[2]/div/div[1]/div[2]/input'
#全局列表
list0013='//div[contains(text(), "全局列表")]'
#删除变量按钮
list0014='//*[@id="list_widget"]/div[2]/div[2]/div[2]/div/div[2]/div[1]'
class Juggle(Public):
    '''
        搜索积木
    '''
    def findJimu(self):
        self.ShowWaitVisibility('xpath&&%s' % sousuobutton001)
        self.GetElementClick('xpath&&%s' % sousuobutton001)

    '''
        选择输入框(搜索积木)
    '''
    def chancebutton001(self):
        self.ShowWaitVisibility('xpath&&%s' % chancebutton001)
        self.GetElementClick('xpath&&%s' % chancebutton001)


        sleep(0.5)
        js='document.getElementsByClassName("common_input--cRtuO")[6].type="text";'
        self.driver.execute_script(js)
        js1='document.getElementsByClassName("common_input--cRtuO")[6].setAttribute("class","");'
        self.driver.execute_script(js1)
        js2='document.getElementsByClassName("common_input--cRtuO")[6].value="1";'
        self.driver.execute_script(js2)

    '''
        点击翻译
    '''
    def fanyi(self):
        self.ShowWaitVisibility('xpath&&%s' % fanyi)
        self.GetElementClick('xpath&&%s' % fanyi)


    #得到input中的值
    def showInputValue(self,value):
        return self.GetElement('xpath&&%s' % value).get_attribute('value')

    '''
        点击主界面声音按钮
    '''
    def music001(self):
        self.ShowWaitVisibility('xpath&&%s' % music001)
        self.GetElementClick('xpath&&%s' % music001)

    '''
        点击+声音
    '''
    def music002(self):
        self.ShowWaitVisibility('xpath&&%s' % music002)
        self.GetElementClick('xpath&&%s' % music002)
    '''
        点击素材库
    '''
    def music003(self):
        self.ShowWaitVisibility('xpath&&%s' % music003)
        self.GetElementClick('xpath&&%s' % music003)
    '''
        声音全部界面下拉到底
    '''
    def music004(self):
        js = musicsucai
        self.driver.execute_script(js)
    '''
        点击【愉快的时刻】
    '''
    def music005(self):
        self.ShowWaitVisibility('xpath&&%s' % music005)
        self.GetElementClick('xpath&&%s' % music005)

    '''
        确认添加
    '''
    def music006(self):
        self.ShowWaitVisibility('xpath&&%s' % music006)
        self.GetElementClick('xpath&&%s' % music006)
    '''
        点击音乐画板
    '''
    def music007(self):
        self.ShowWaitVisibility('xpath&&%s' % music007)
        self.GetElementClick('xpath&&%s' % music007)
    '''
        点击画布
    '''
    def music008(self):
        self.ShowWaitVisibility('xpath&&%s' % music008)
        self.GetElementClick('xpath&&%s' % music008)
    '''
        等待弹窗出现
    '''
    def musicend(self):
        self.ShowWaitVisibility('xpath&&%s' % musicend)

    '''
        点击保存
    '''
    def music009(self):
        self.ShowWaitVisibility('xpath&&%s' % music009)
        self.GetElementClick('xpath&&%s' % music009)
    '''
        点击离开
    '''
    def music0010(self):
        self.ShowWaitVisibility('xpath&&%s' % music0010)
        self.GetElementClick('xpath&&%s' % music0010)
    '''
        点击录音
    '''
    def music0011(self):
        self.ShowWaitVisibility('xpath&&%s' % music0011)
        self.GetElementClick('xpath&&%s' % music0011)

    '''
        点击开始录音
    '''

    def music0012(self):
        self.ShowWaitVisibility('xpath&&%s' % music0012)
        self.GetElementClick('xpath&&%s' % music0012)
        sleep(1)

    '''
        关闭录音
    '''
    def music0013(self):
        self.ShowWaitVisibility('xpath&&%s' % music0013)
        self.GetElementClick('xpath&&%s' % music0013)
        return True
    '''
        上传音乐
    '''
    def music0014(self):
        self.ShowWaitVisibility('xpath&&%s' % music0014)
        pyperclip.copy(path.music)#复制文件路径到剪切板
        self.GetElementClick('xpath&&%s' % music0014)
        sleep(0.5)
        win32api.keybd_event(17, 0, 0, 0)
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        win32api.keybd_event(13, 0, 0, 0)  # (回车)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        time.sleep(2)
        return True

    '''
        点击录音
    '''
    def click_music(self):
        self.ShowWaitVisibility('xpath&&%s' % newmusic)
        self.GetElementClick('xpath&&%s' % newmusic)

    '''
        删除音乐
    '''
    def delete_music(self):
        self.ShowWaitVisibility('xpath&&%s' % delete_music)
        self.GetElementClick('xpath&&%s' % delete_music)



    '''
        点击music
    '''
    def show001(self):
        self.ShowWaitVisibility('xpath&&%s' % show001)
        self.GetElementClick('xpath&&%s' % show001)
    '''
        点击播放按钮
    '''
    def show002(self):
        self.ShowWaitVisibility('xpath&&%s' % show003)
        self.GetElementClick('xpath&&%s' % show003)
        sleep(3)
    '''
        点击﹀
    '''
    def show003(self):
        self.ShowWaitVisibility('xpath&&%s' % show004)
        self.GetElementClick('xpath&&%s' % show004)
    '''
        调节音量  867, 274 23.8  
    '''
    def show004(self):
        button001 = win32api.GetCursorPos()
        win32api.SetCursorPos((910, 275))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 910, 275, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 910, 275, 0, 0)


    '''
        调节速度 900, 304
    '''
    def show005(self):
        button001 = win32api.GetCursorPos()
        win32api.SetCursorPos((937, 305))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 937, 305, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 937, 305, 0, 0)
    '''
        点击右键
    '''
    def show006(self):
        self.ShowWaitVisibility('xpath&&%s' % show001)
        ActionChains(self.driver).context_click(self.GetElement('xpath&&%s' % show001)).perform()
    '''
        点击修改名称
    '''
    def show007(self):
        self.ShowWaitVisibility('xpath&&%s' % show006)
        self.GetElementClick('xpath&&%s' % show006)
    '''
        输入新名称
    '''
    def show008(self):
        win32api.keybd_event(65, 0, 0, 0)
        win32api.keybd_event(66, 0, 0, 0)
        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        win32api.keybd_event(66, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)
        win32api.keybd_event(13, 0, 0, 0)  # (回车)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        time.sleep(2)
        win32api.keybd_event(13, 0, 0, 0)  # (回车)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键

    '''
        删除音乐文件
    '''
    def show009(self):
        self.ShowWaitVisibility('xpath&&%s' % show002)
        self.GetElementClick('xpath&&%s' % show002)
    '''
        点击主界面变量
    '''
    def variable001(self):
        self.ShowWaitVisibility('xpath&&%s' % variable001)
        self.GetElementClick('xpath&&%s' % variable001)
    '''
        点击+变量
    '''
    def variable002(self):
        self.ShowWaitVisibility('xpath&&%s' % variable002)
        self.GetElementClick('xpath&&%s' % variable002)
    '''
        输入变量名
    '''
    def variable003(self,name):
        self.ShowWaitVisibility('xpath&&%s' % variable003)
        self.GetElementSendKeys('xpath&&%s' % variable003,name)
    '''
        点击确定按钮
    '''
    def variable004(self):
        self.ShowWaitVisibility('xpath&&%s' % variable004)
        self.GetElementClick('xpath&&%s' % variable004)
    '''
        点击新增的元素
    '''
    def variable005(self):
        self.ShowWaitVisibility('xpath&&%s' % variable005)
        self.GetElementClick('xpath&&%s' % variable005)
    '''
        点击隐藏/出现
    '''
    def variable006(self):
        self.ShowWaitVisibility('xpath&&%s' % variable006)
        self.GetElementClick('xpath&&%s' % variable006)
    '''
        点击﹀按钮
    '''
    def variable007(self):
        self.ShowWaitVisibility('xpath&&%s' % variable007)
        self.GetElementClick('xpath&&%s' % variable007)


    def mouse(self,x,y):
        '''
            win系统操作鼠标

        :param x: x坐标
        :param y: y坐标
        :return: None
        '''
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def keyword(self,args):
        '''
            win系统键盘事件
        :param args: 要输入的按钮依次输入就可以
        :return:
        '''
        for i in range(len(args)):
            win32api.keybd_event(args[i], 0, 0, 0)
        win32api.keybd_event(args[-1], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)
        win32api.keybd_event(13, 0, 0, 0)  # (回车)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    '''
        重命名
    '''
    def variable008(self,*args):
        self.ShowWaitVisibility('xpath&&%s' % variable008)
        self.mouse(834,257)
        self.keyword(args)

    '''
        输入初始值
    '''
    def variable009(self,*args):
        sleep(0.5)
        self.mouse(834, 297)
        self.keyword(args)

    '''
        删除变量
    '''
    def variable0010(self):
        self.ShowWaitVisibility('xpath&&%s' % variable0010)
        self.GetElementClick('xpath&&%s' % variable0010)


    #----------------------------------------------------------------------列表--------------------------------------------------------------------
    '''
        点击主界面列表
    '''
    def list001(self):
        self.ShowWaitVisibility('xpath&&%s' % list001)
        self.GetElementClick('xpath&&%s' % list001)
    '''
        点击+列表
    '''
    def list002(self):
        self.ShowWaitVisibility('xpath&&%s' % list002)
        self.GetElementClick('xpath&&%s' % list002)
    '''
        输入列表名称
    '''
    def list003(self,list_str):
        self.ShowWaitVisibility('xpath&&%s' % list003)
        self.GetElementSendKeys('xpath&&%s' % list003, list_str)
    '''
        确认按钮
    '''
    def list004(self):
        self.ShowWaitVisibility('xpath&&%s' % list004)
        self.GetElementClick('xpath&&%s' % list004)
    '''
        点击新增的列表
    '''
    def list005(self):
        self.ShowWaitVisibility('xpath&&%s' % list005)
        self.GetElementClick('xpath&&%s' % list005)
    '''
        显示\隐藏
    '''
    def list006(self):
        self.ShowWaitVisibility('xpath&&%s' % list006)
        self.GetElementClick('xpath&&%s' % list006)
    '''
        点击更多按钮
    '''
    def list007(self):
        self.ShowWaitVisibility('xpath&&%s' % list007)
        self.GetElementClick('xpath&&%s' % list007)
    '''
        点击+号
    '''
    def list008(self):
        self.ShowWaitVisibility('xpath&&%s' % list008)
        self.GetElementClick('xpath&&%s' % list008)
    '''
        列表第一个元素的值
    '''
    def list009(self,value):
        self.ShowWaitVisibility('xpath&&%s' % list009)
        self.GetElementSendKeys('xpath&&%s' % list009, value)
    '''
        点击保存
    '''
    def list0010(self):
        self.ShowWaitVisibility('xpath&&%s' % list0010)
        self.GetElementClick('xpath&&%s' % list0010)
    '''
        点击右键
    '''
    def list0011(self):
        ActionChains(self.driver).context_click(self.GetElement('xpath&&%s' % list005)).perform()
    '''
        点击修改
    '''
    def list0012(self):
        self.ShowWaitVisibility('xpath&&%s' % list0011)
        self.GetElementClick('xpath&&%s' % list0011)
    '''
        输入新名称
    '''
    def list0013(self, value):
        self.ShowWaitVisibility('xpath&&%s' % list0012)
        self.GetElementSendKeys('xpath&&%s' % list0012, value)
    '''
        点击全局列表
    '''
    def list0014(self):
        self.ShowWaitVisibility('xpath&&%s' % list0013)
        self.GetElementClick('xpath&&%s' % list0013)
    '''
        点击删除列表
    '''
    def list0015(self):
        self.ShowWaitVisibility('xpath&&%s' % list0014)
        self.GetElementClick('xpath&&%s' % list0014)





if __name__ == '__main__':
    pass
