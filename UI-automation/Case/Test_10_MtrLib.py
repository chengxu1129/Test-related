import sys

import pyperclip

sys.path.append("..")
from lib import Public,TestData,Element,path
from selenium import webdriver
from Module import MtrLib
import time
from time import sleep
import allure
import win32api,win32gui,win32con
from Module import Juggle
r5 = '//div[contains(text(),"烟花")]'
r1 = '//div[contains(text(),"编程猫")]'
r4 = '//div[contains(text(),"球")]'
r3 = '//div[contains(text(),"开始游戏")]'

bg1 = '//div[contains(text(), "编程猫的房间")]'
bg2 = '//div[contains(text(), "操场")]'
bg3 = '//div[contains(text(), "草原")]'

ag1 = '//div[contains(text(), "上发条声")]'
ag2 = '//div[contains(text(), "暗中行事")]'

test_fenzuname='//div[contains(text(),"test")]'
test_fenzuname1='//div[contains(text(),"test999")]'
sucai='//*[@id="material-items-wrap"]/div[2]/div[1]'
#//*[@id="material-items-wrap"]/div[2]/div[1]

sucaistore='//*[@id="material-dialog"]/div[3]/div/div[2]'
           #//*[@id="material-dialog"]/div[3]/div/div[2]

class TestML():



    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.ML = MtrLib.MtrLib(cls.driver)






    def test_JumpML(self):
        """
        角色区跳转到素材库
        :return:
        """
        self.Public.CloseGP()
        self.Public.SuccessLogin(TestData.chengxu,TestData.cxps)
        # self.ML.AddRole()
    #     self.ML.MLAdd()
    #     Result = self.Public.ShowWaitVisibility('css&&%s' % Element.Search)
    #     assert Result != False
    #     self.Public.GetElementClick('xpath&&%s' % Element.CloseS)
    #
    # def test_RJumpML(self):
    #     """
    #     造型栏跳转到素材库
    #     :return:
    #     """
    #     self.ML.ClickOR()
    #     self.ML.ClickRS()
    #     self.ML.ClickSSlc()
    #     Result = self.Public.ShowWaitVisibility('css&&%s' % Element.Search)
    #     assert Result != False
    #     self.Public.GetElementClick('xpath&&%s' % Element.CloseS)

    def test_AJumpML(self):
        """
        声音盒子跳转到素材库
        :return:
        """
        self.ML.Audio()
        self.ML.Audios()
        self.ML.AudioSc()
        Result = self.Public.ShowWaitVisibility('css&&%s' % Element.Search)
        assert Result != False

    def test_CheckML(self):
        """
        素材库角色显示
        :return:
        """
        self.ML.ClickSR()
        self.Public.ShowWaitVisibility('xpath&&%s' % Element.RoleS1)
        self.ML.ClickSRS(5)
        self.Public.ShowWaitVisibility('xpath&&%s' % r5)
        self.ML.ClickSRS(1)
        self.Public.ShowWaitVisibility('xpath&&%s' % r1)
        self.ML.ClickSRS(4)
        self.Public.ShowWaitVisibility('xpath&&%s' % r4)
        self.ML.ClickSRS(2)
        self.Public.ShowWaitVisibility('xpath&&%s' % r1)
        self.ML.ClickSRS(3)
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % r3)
        assert Result != False

    def test_CheckBG(self):
        """
        素材库背景显示
        :return:
        """
        self.ML.ClickBG()
        self.Public.ShowWaitVisibility('xpath&&%s' % bg1)
        self.ML.ClickSBG(4)
        self.Public.ShowWaitVisibility('xpath&&%s' % bg3)
        self.ML.ClickSBG(1)
        self.Public.ShowWaitVisibility('xpath&&%s' % bg1)
        self.ML.ClickSBG(3)
        self.Public.ShowWaitVisibility('xpath&&%s' % bg2)
        self.ML.ClickSBG(2)
        Result = self.Public.ShowWaitV_until_not('xpath&&%s' % bg2)
        assert Result != False

    def test_CheckAG(self):
        """
        素材库背景显示
        :return:
        """
        self.ML.ClickAG()
        self.Public.ShowWaitVisibility('xpath&&%s' % ag1)
        self.ML.ClickSAG(3)
        self.Public.ShowWaitVisibility('xpath&&%s' % ag2)
        self.ML.ClickSAG(1)
        self.Public.ShowWaitVisibility('xpath&&%s' % ag1)
        self.ML.ClickSAG(2)
        Result = self.Public.ShowWaitV_until_not('xpath&&%s' % ag2)
        assert Result != False

    # ----------------------------------------------------------------续写素材库用例----------------------------------------------------------
    '''
        名称:创建分组
    '''

    @allure.title('创建分组')
    def test_createfenzu(self):
        try:
            with allure.step('点击+号，创建分组'):
                self.ML.cerateFenZu()
            with allure.step('输入分组名字test'):
                self.ML.shurufenzuname('test')
            with allure.step('点击确定按钮'):
                self.ML.quedingfenzu()
            with allure.step('点击新创建的分组'):
                self.ML.rename00()
        except Exception as e:
            raise BaseException(e,'用例【创建分组】失败')
        finally:
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % test_fenzuname)
            assert Result

    '''
        名称:重命名分组
    '''
    @allure.title('重命名分组')
    def test_rename(self):
        try:
            with allure.step('点击鼠标右键'):
                self.ML.rename0(self.driver)
            with allure.step('点击重命名'):
                self.ML.rename002()
            with allure.step('输入新名字test999'):
                self.ML.shurufenzuname('test999')
            with allure.step('点击确定按钮'):
                self.ML.quedingfenzu()
            time.sleep(1)
        except Exception as e:
            raise BaseException(e,'用例【重命名分组】失败')
        finally:
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % test_fenzuname)
            assert Result
    '''
        名称:删除分组
    '''
    @allure.title('删除分组')
    def test_fenzuDelete(self):
        try:
            with allure.step('点击鼠标右键'):
                self.ML.rename0(self.driver)
            with allure.step('点击删除'):
                self.ML.delete001()
            with allure.step('点击保留'):
                self.ML.rename004()
            time.sleep(1)
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % test_fenzuname)
            assert Result
        except Exception as e:
            raise BaseException(e,'用例【删除分组】失败')
    '''
        素材移动到分组
    '''
    # def test_move(self):
    #     try:
    #         self.ML.rename000(self.driver)
    #         self.ML.move002()
    #         self.ML.move003()
    #         self.ML.move004()
    #         self.ML.move005()
    #         time.sleep(1)
    #         Result = self.Public.ShowWaitV_until_not('xpath&&%s' % sucai)
    #         assert Result
    #     except Exception as e:
    #         raise BaseException(e,'用例【素材移动到分组】失败')

    '''
        删除素材
    '''
    # def test_deletesucai(self):
    #     try:
    #         self.ML.move001()
    #         self.ML.move002()
    #         self.ML.move006()
    #         time.sleep(1)
    #         Result = self.Public.ShowWaitVisibility('xpath&&%s' % sucai)
    #         assert Result
    #     except Exception as e:
    #         raise BaseException(e,'用例【删除素材】失败')
    '''
        本地上传角色
    '''
    @allure.title('本地上传角色')
    def test_shangchuanrole(self):
        try:
            with allure.step('点击test999'):
                self.ML.chancefenzu()
            with allure.step('点击角色'):
                self.ML.role()
            time.sleep(2)
            with allure.step('点击本地上传并点击上传按钮'):
                pyperclip.copy(path.role)
                js='document.querySelector("#material-items-wrap > div > div.th1-border-impt-2.th1-bg-hover-9.upload-item--EoO9m > form > input").click()'
                self.driver.execute_script(js)
                self.ML.shangchuan002()
                # self.ML.shangchaun001()
            with allure.step('点击清除按钮'):
                self.ML.clear_button()
            time.sleep(1)
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % sucai)
            assert Result
        except Exception as e:
            raise BaseException(e,'用例【本地上传角色】失败')
    '''
        本地上传背景
    '''

    @allure.title('本地上传背景')
    def test_shangchuanbackground(self):
        try:
            with allure.step('点击背景'):
                self.ML.background()
            with allure.step('点击本地上传并点击上传按钮'):
                pyperclip.copy(path.background)
                js = 'document.querySelector("#material-items-wrap > div > div.th1-border-impt-2.th1-bg-hover-9.upload-item--EoO9m > form > input").click()'
                self.driver.execute_script(js)
                self.ML.shangchuan002()
            with allure.step('点击清除按钮'):
                self.ML.clear_button()
            time.sleep(1)
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % sucai)
            assert Result
            sleep(1)
        except Exception as e:
            raise BaseException(e,'用例【本地上传背景】失败')
    '''
        本地上传声音
    '''

    @allure.title('本地上传声音')
    def test_shangchuanmusic(self):
        try:
            with allure.step('点击背景'):
                self.ML.background()
            with allure.step('点击本地上传并点击上传按钮'):
                pyperclip.copy(path.music)
                js = 'document.querySelector("#material-items-wrap > div > div.th1-border-impt-2.th1-bg-hover-9.upload-item--EoO9m > form > input").click()'
                '''
                      document.querySelector("#material-items-wrap > div > div.th1-border-impt-2.th1-bg-hover-9.upload-item--EoO9m > form > input")
                '''
                self.driver.execute_script(js)
                self.ML.shangchuanmusic()
            with allure.step('点击清除按钮'):
                self.ML.clear_button()
            time.sleep(1)
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % sucai)
            assert Result
        except Exception as e:
            raise BaseException(e,'用例【本地上传声音】失败')

    '''
        素材商店最新上架
    '''

    @allure.title('素材商店最新上架')
    def test_newsucai(self):
        try:
            with allure.step('点击素材商店'):
                self.ML.materialstoreClick()
            with allure.step('点击最新上架'):
                self.ML.newnewshangjiaClick()
            time.sleep(1)
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % sucaistore)
            assert Result
        except Exception as e:
            raise BaseException(e,'用例【最新上架】失败')

    '''
        最多使用
    '''

    @allure.title('点击最多使用')
    def test_moreshiyong(self):
        try:
            with allure.step('点击最多使用'):
                self.ML.moreshiyongClick()
            time.sleep(1)
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % sucaistore)
            assert Result
        except Exception as e:
            raise BaseException(e,'用例【最多使用】失败')

    '''
        点击仅显示未采集
    '''

    @allure.title('点击仅显示未采集')
    def test_weicaijiself(self):
        try:
            with allure.step('点击仅显示未采集'):
                self.ML.weicaijiClick()
            time.sleep(1)
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % sucaistore)
            assert Result
        except Exception as e:
            raise BaseException(e,'用例【仅显示未采集】失败')


    '''
        购买角色
    '''

    @allure.title('购买角色')
    def test_buyRole(self):
        try:
            with allure.step('点击购物车按钮'):
                self.ML.buysantoulongClick()
            with allure.step('点击采下来'):
                self.ML.caixilaiClick()
            with allure.step('点击清除按钮'):
                self.ML.clear_button()
            time.sleep(1)
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % sucaistore)
            assert Result
        except Exception as e:
            raise BaseException(e,'用例【购买角色】失败')

    '''
        金币显示
    '''

    @allure.title('金币显示')
    def test_cornShow(self):
        try:
            with allure.step('查看显示的金币数量'):
                number=self.ML.showcornNumber()
            assert number==0
            time.sleep(1)
        except Exception as e:
            raise BaseException(e,'用例【金币显示】失败')

    '''
        关键词搜索素材
    '''

    @allure.title('关键词搜索素材')
    def test_shucaiinputSend(self):
        try:
            with allure.step('输入贝塔'):
                th=self.ML.shucaiinputSend('贝塔')
            time.sleep(1)
            assert th
        except Exception as e:
            raise BaseException(e,'用例【关键词搜索素材】失败')

    @allure.title('删除分组')
    def test_fenzuDelete(self):
        try:
            self.ML.my_sucai()
            with allure.step('点击鼠标右键'):
                self.ML.rename0(self.driver)
            with allure.step('点击删除'):
                self.ML.delete001()
            with allure.step('点击保留'):
                self.ML.su()
            time.sleep(1)
            Result = self.Public.ShowWaitP_until_not('xpath&&%s' % test_fenzuname1)
            assert Result
        except Exception as e:
            raise BaseException(e, '用例【删除分组】失败')






    '''
        退出网页
    '''

    @allure.title('退出网页')
    def teardown_class(self):
        self.driver.quit()













if __name__ == '__main__':
    pass
