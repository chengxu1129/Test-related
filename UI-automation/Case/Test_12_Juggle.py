#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Never.cheng
@file:Test_12_Juggle.py.py
@time:2020/09/15
"""
import sys

sys.path.append("..")
from lib import Public, TestData, Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Module import Juggle
import time
from functools import wraps
import allure

chancebutton001 = '//div/input[@placeholder="搜索积木"]'

music_true = '//div[contains(text(), "愉悦的时刻")]'
music_huaben = '//div[contains(text(), "新音乐")]'
luyin = '//div[contains(text(), "music")]'
show01 = '//*[@id="audio_widget"]/div[2]/div/div/div[2]'

show001 = '//div[contains(text(), "ab")]'

variable001 = '//div[contains(text(), "变量")]'
variable006 = '//*[@id="variable_widget"]/div[2]/div[2]/div[2]/div/div[2]/div[2]'
variable00 = '//div[contains(text(), "全局变量")]'

# 主界面的列表
list001 = '//div[contains(text(), "列表")]'
list003 = '//div[contains(text(), "名称")]'
# 新增的列表
list005 = '//div[contains(text(), "list")]'
list006 = '//div[contains(text(), "编辑列表")]'
list0013 = '//div[contains(text(), "全局列表")]'

ch_options = Options()


# ch_options.add_argument("--headless")


@allure.feature("积木模块")
class TestML():
    driver = None

    def demo(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            start = time.time()
            result = func(self, *args, **kwargs)
            end = time.time()
            print('测试时间为', end - start)
            return result

        return wrapper

    @staticmethod
    def get_grid_driver():
        """获取 grid driver"""
        hub_url = 'http://118.25.50.68:5001/wd/hub'
        caps = {'browserName': 'chrome'}
        driver = webdriver.Remote(
            command_executor=hub_url,
            desired_capabilities=caps
        )
        return driver

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        cls.driver = webdriver.Chrome()
        # cls.driver = webdriver.Chrome(chrome_options=options)
        #cls.driver = cls.get_grid_driver()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.JL = Juggle.Juggle(cls.driver)

    '''
        处理浏览器
    '''

    @allure.title('首次提示和登录账号')
    def test_first(self):
        with allure.step('点击首页'):
            self.Public.CloseGP()
        with allure.step('登录账号'):
            self.Public.SuccessLogin(TestData.chengxu, TestData.cxps)

    # -----------------------------------------------------------------------------------用例开始-------------------------------------------------------

    '''
        搜索积木
    '''

    @demo
    @allure.title('搜索积木')
    def test_001(self):
        try:
            with allure.step('点击搜索图标(放大镜按钮)'):
                self.JL.findJimu()
            time.sleep(1)
            with allure.step('选择输入框'):
                self.JL.chancebutton001()
            with allure.step('点击翻译'):
                self.JL.fanyi()
            number = self.JL.showInputValue(chancebutton001)
            assert number
        except BaseException as e:
            raise BaseException(e, '用例[搜索积木]执行失败')

    '''
        素材库添加声音
    '''

    @allure.title('素材库添加声音')
    def test_002(self):
        try:
            with allure.step('点击主界面声音按钮'):
                self.JL.music001()
            with allure.step('点击+声音'):
                self.JL.music002()
            with allure.step('点击素材库'):
                self.JL.music003()
            with allure.step('声音全部界面下拉到底'):
                self.JL.music004()
            with allure.step('点击【愉快的时刻】'):
                self.JL.music005()
            with allure.step('点击确认添加'):
                self.JL.music006()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % music_true)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[素材库添加声音]执行失败')

    '''
        音乐画板添加
    '''

    @allure.title('音乐画板添加')
    def test_003(self):
        try:
            with allure.step('点击+声音'):
                self.JL.music002()
            with allure.step('点击音乐画板'):
                self.JL.music007()
            with allure.step('点击画布'):
                self.JL.music008()
            with allure.step('点击保存'):
                self.JL.music009()
            try:
                with allure.step('等待弹窗出现'):
                    self.JL.musicend()
            except Exception:
                pass
            time.sleep(1)
            with allure.step('点击离开'):
                self.JL.music0010()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % music_huaben)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[音乐画板添加]执行失败')

    '''
        录音
    '''

    @allure.title('录音')
    def test_004(self):
        try:
            with allure.step('点击+声音'):
                self.JL.music002()
            with allure.step('点击录音'):
                self.JL.music0011()
            with allure.step('点击开始录音'):
                self.JL.music0012()
            result = self.JL.music0013()
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[录音]执行失败')

    '''
        删除素材音乐
    '''

    @allure.title('删除素材音乐')
    def test_delete001(self):
        try:
            with allure.step('点击【愉快的时刻】'):
                self.JL.music005()
            with allure.step('删除音乐'):
                self.JL.delete_music()
        except BaseException as e:
            raise BaseException(e, '用例[录音]执行失败')

    '''
        删除画板音乐
    '''

    @allure.title('删除画板音乐')
    def test_delete002(self):
        try:
            with allure.step('点击录音'):
                self.JL.click_music()
            with allure.step('删除音乐'):
                self.JL.delete_music()
        except BaseException as e:
            raise BaseException(e, '用例[录音]执行失败')

    '''
        上传声音
    '''

    @allure.title('上传声音')
    def test_005(self):
        try:
            with allure.step('点击+声音'):
                self.JL.music002()
            with allure.step('上传音乐'):
                self.JL.music0014()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % luyin)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[上传声音]执行失败')

    '''
        播放音乐
    '''

    @allure.title('播放音乐')
    def test_006(self):
        try:
            with allure.step('点击music'):
                self.JL.show001()
            with allure.step('点击播放按钮'):
                self.JL.show002()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % '//div[contains(text(), "music")]')
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[播放音乐]执行失败')

    '''
        点击﹀
    '''

    @allure.title('点击﹀')
    def test_007(self):
        try:
            with allure.step('点击﹀'):
                self.JL.show003()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % show01)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[点击﹀]执行失败')

    '''
        调节音量
    '''

    @allure.title('调节音量')
    def test_008(self):
        try:
            with allure.step('调节音量到任意大小'):
                self.JL.show004()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % show01)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[调节音量]执行失败')

    '''
        调节快慢
    '''

    @allure.title('调节快慢')
    def test_009(self):
        try:
            with allure.step('调节快慢到任意位置'):
                self.JL.show005()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % show01)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[调节快慢]执行失败')

    '''
        修改名字
    '''

    @allure.title('修改名字')
    def test_0010(self):
        try:
            with allure.step('点击﹀'):
                self.JL.show003()
            with allure.step('点击右键'):
                self.JL.show006()
            with allure.step('点击修改名称'):
                self.JL.show007()
            with allure.step('输入新名称'):
                self.JL.show008()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % show001)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[修改名字]执行失败')

    '''
        删除音乐文件
    '''
    @allure.title('删除音乐文件')
    def test_0011(self):
        try:
            with allure.step('删除音乐文件'):
                self.JL.show009()
            result = self.Public.ShowWaitP_until_not('xpath&&%s' % show001)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[删除音乐文件]执行失败')

    '''
        点击主界面变量，新建变量
    '''
    @allure.title('点击主界面变量，新建变量')
    def test_0012(self):
        try:
            with allure.step('点击主界面变量'):
                self.JL.variable001()
            with allure.step('点击+变量'):
                self.JL.variable002()
            with allure.step('输入变量名'):
                self.JL.variable003(TestData.name)
            with allure.step('点击确定按钮'):
                self.JL.variable004()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % variable001)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[点击主界面变量]执行失败')

    '''
        隐藏变量
    '''

    @allure.title('隐藏变量')
    def test_0013(self):
        try:
            with allure.step('点击新增的元素'):
                self.JL.variable005()
            with allure.step('点击隐藏变量'):
                self.JL.variable006()
            time.sleep(0.5)
            result = self.Public.ShowWaitVisibility('xpath&&%s' % variable006)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[隐藏变量]执行失败')

    '''
        出现变量
    '''
    @allure.title('出现变量')
    def test_0014(self):
        try:
            with allure.step('点击出现变量'):
                self.JL.variable006()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % variable006)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[出现变量]执行失败')

    '''
        重命名变量
    '''
    @allure.title('重命名变量')
    def test_0015(self):
        try:
            with allure.step('点击﹀按钮'):
                self.JL.variable007()
            with allure.step('重命名'):
                self.JL.variable008(49, 50, 51)
            result = self.Public.ShowWaitVisibility('xpath&&%s' % variable00)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[重命名变量]执行失败')

    '''
        输入初始值
    '''

    @allure.title('输入初始值')
    def test_0016(self):
        try:
            with allure.step('输入初始值123'):
                self.JL.variable009(49, 50, 51)
            result = self.Public.ShowWaitVisibility('xpath&&%s' % variable00)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[输入初始值]执行失败')

    '''
        删除变量
    '''

    @allure.title('删除变量')
    def test_0017(self):
        try:
            with allure.step('点击﹀按钮'):
                self.JL.variable007()
            with allure.step('删除变量'):
                self.JL.variable0010()
            result = self.Public.ShowWaitP_until_not('xpath&&%s' % variable00)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[输入初始值]执行失败')

    # -------------------------------------------------列表------------------------------------------------------
    '''
        点击列表
    '''

    @allure.title('点击列表')
    def test_0018(self):
        try:
            with allure.step('点击主界面列表'):
                self.JL.list001()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list001)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[点击列表]执行失败')

    '''
        点击+号
    '''
    @allure.title('点击+号')
    def test_0019(self):
        try:
            with allure.step('点击+列表'):
                self.JL.list002()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list003)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[点击+号]执行失败')

    '''
        输入列表名称
    '''

    @allure.title('输入列表名称')
    def test_0020(self):
        try:
            with allure.step('输入列表名称list'):
                self.JL.list003(TestData.list_str)
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list003)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[输入列表名称]执行失败')

    '''
        点击确定
    '''

    @allure.title('点击确定')
    def test_0021(self):
        try:
            with allure.step('点击确定按钮'):
                self.JL.list004()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list005)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[点击确定]执行失败')

    '''
        点击新建的列表
    '''

    @allure.title('点击新建的列表')
    def test_0022(self):
        try:
            with allure.step('点击新增的列表'):
                self.JL.list005()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list005)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[点击新建的列表]执行失败')

    '''
        隐藏
    '''

    @allure.title('隐藏列表')
    def test_0023(self):
        try:
            with allure.step('点击隐藏按钮'):
                self.JL.list006()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list005)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[隐藏]执行失败')

    '''
        显示
    '''

    @allure.title('显示列表')
    def test_0024(self):
        try:
            with allure.step('点击显示按钮'):
                self.JL.list006()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list005)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[显示]执行失败')

    '''
        点击更多
    '''

    @allure.title('点击更多按钮')
    def test_0025(self):
        try:
            with allure.step('点击更多按钮'):
                self.JL.list007()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list006)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[点击更多]执行失败')

    '''
        点击+
    '''
    @allure.title('点击+')
    def test_0026(self):
        try:
            with allure.step('点击+'):
                self.JL.list008()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list006)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[点击+]执行失败')

    '''
        输入第一个列表的值
    '''

    @allure.title('列表第一个元素的值')
    def test_0027(self):
        try:
            with allure.step('输入name'):
                self.JL.list009('name')
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list006)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[输入第一个列表的值+]执行失败')

    '''
        点击保存
    '''

    @allure.title('点击保存')
    def test_0028(self):
        try:
            with allure.step('点击保存'):
                self.JL.list0010()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list0013)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[点击保存]执行失败')

    '''
        重命名
    '''

    @allure.title('点击保存')
    def test_0029(self):
        try:
            with allure.step('点击右键'):
                self.JL.list0011()
            with allure.step('点击修改'):
                self.JL.list0012()
            with allure.step('输入新名称repeat'):
                self.JL.list0013('repeat')
            with allure.step('点击全局列表'):
                self.JL.list0014()
            result = self.Public.ShowWaitVisibility('xpath&&%s' % list0013)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[重命名]执行失败')

    '''
        删除列表
    '''

    @allure.title('删除列表')
    def test_0030(self):
        try:
            with allure.step('点击删除列表'):
                self.JL.list0015()
            result = self.Public.ShowWaitP_until_not('xpath&&%s' % list0013)
            assert result
        except BaseException as e:
            raise BaseException(e, '用例[重命名]执行失败')

    '''
        退出网页
    '''

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pass
