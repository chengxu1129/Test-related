from lib.Public import Public
from lib import Element
from selenium.webdriver.common.keys import Keys



class SRFeatures(Public):

    def ClickSave(self):
        """
        点击保存
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Save)
        self.GetElementClick('css&&%s' % Element.Save)

    def InputFileName(self,FileName):
        """
        作品名称修改
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.FileName)
        InputFileName = self.GetElement('css&&%s' % Element.FileName)
        # input全选操作
        InputFileName.send_keys(Keys.CONTROL+'a')
        # BackSpace操作
        InputFileName.send_keys(Keys.BACKSPACE)
        self.GetElementSendKeys('css&&%s' % Element.FileName,FileName)

    def ClickRelease(self):
        """
        点击发布按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Release)
        self.GetElementClick('css&&%s' % Element.Release)

    def InputReleaseName(self,BcmName):
        """
        发布页重命名
        :param BcmName:
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.ReleaseName)
        InputName = self.GetElement('css&&%s' % Element.ReleaseName)
        InputName.send_keys(Keys.CONTROL + 'a')
        InputName.send_keys(Keys.BACKSPACE)
        self.GetElementSendKeys('css&&%s' % Element.ReleaseName,BcmName)

    def ClickPurchase(self):
        """
        点击购买按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Purchase)
        self.GetElementClick('xpath&&%s' % Element.Purchase)

    def ClickNoPurchase(self):
        """
        点击不允许购买按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.NoPurchase)
        self.GetElementClick('xpath&&%s' % Element.NoPurchase)

    def InputIntroduce(self,Introduce):
        """
        作品介绍输入
        :param Introduce:
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.FileIntroduce)
        self.GetElementSendKeys('css&&%s' % Element.FileIntroduce,Introduce)

    def InputOperationGuide(self,OG):
        """
        操作指南
        :param Introduce:
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.OperationGuide)
        self.GetElementSendKeys('css&&%s' % Element.OperationGuide,OG)

    def ClickDtermRas(self):
        """
        发布页点击确认发布
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.DetermineRelease)
        self.GetElementClick('css&&%s' % Element.DetermineRelease)
