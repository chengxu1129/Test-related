from lib.Public import Public
from lib import Element
from selenium.webdriver.common.action_chains import ActionChains



class Help(Public):

    def ClickHelp(self):
        """
        点击帮助按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Help)
        self.GetElementClick('xpath&&%s' % Element.Help)

    def ClickCodeBooks(self):
        """
        点击源码图鉴
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Helps)
        OneDriver = self.GetElement('xpath&&%s' % Element.Helps)
        TwoDeiver = self.GetElement('css&&%s' % Element.CodeBooks)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDeiver).perform()

    def ClickJoinQQ(self):
        """
        点击加入QQ
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Helps)
        OneDriver = self.GetElement('xpath&&%s' % Element.Helps)
        TwoDeiver = self.GetElement('css&&%s' % Element.JoinQQ)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDeiver).perform()

    def CloseQQPage(self):
        """
        关闭QQ页面
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseQQPage)
        self.GetElementClick('xpath&&%s' % Element.CloseQQPage)

    def Tool(self):
        """
        等待Tool方法
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Tool)
        OneDriver = self.GetElement('xpath&&%s' % Element.Tool)
        return OneDriver

    def ClickBlockPicture(self):
        """
        点击积木图片
        :return:
        """
        OneDriver = self.Tool()
        TwoDeiver = self.GetElement('css&&%s' % Element.BlockPicture)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDeiver).perform()

    def CloseBPPage(self):
        """
        关闭积木图片介绍页面
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseBlockPicturePage)
        self.GetElementClick('xpath&&%s' % Element.CloseBlockPicturePage)

    def ClickHardwareAssistant(self):
        """
        点击硬件助手
        :return:
        """
        OneDriver = self.Tool()
        TwoDeiver = self.GetElement('css&&%s' % Element.HardwareAssistant)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDeiver).perform()

    def DLHardware(self):
        """
        下载硬件助手
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.DownloadHAC)
        self.GetElementClick('css&&%s' % Element.DownloadHAC)

    def CloseHAPage(self):
        """
        关闭硬件助手页面
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseHAPage)
        self.GetElementClick('xpath&&%s' % Element.CloseHAPage)

    def ClickScratch(self):
        """
        点击Scratch
        :return:
        """
        OneDriver = self.Tool()
        TwoDeiver = self.GetElement('css&&%s' % Element.Scratch)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDeiver).perform()

    def CloseScratchPage(self):
        """
        关闭Scratch页面
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseScratchPage)
        self.GetElementClick('xpath&&%s' % Element.CloseScratchPage)
