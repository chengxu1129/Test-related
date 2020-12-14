from Module import Help
from selenium import webdriver
from lib import Element,TestData,path,Public
import time
import os



class TestHelp():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.Help = Help.Help(cls.driver)

    def test_JPBooks(self):
        """
        跳转到源码图鉴
        :return:
        """
        self.Public.CloseGP()
        self.Public.SuccessLogin()
        self.Help.ClickHelp()
        self.Help.ClickCodeBooks()
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[-1])
        CBurl = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(all_h[0])
        assert CBurl == TestData.CBurl

    def test_JoinQQ(self):
        """
        加入QQ群
        :return:
        """
        self.Help.ClickHelp()
        self.Help.ClickJoinQQ()
        self.Help.CloseQQPage()
        Result = self.Public.ShowWaitV_until_not('xpath&&%s' % Element.CloseQQPage)
        assert Result != False

    def test_BlockPict(self):
        """
        积木图片
        :return:
        """
        self.Help.ClickHelp()
        self.Help.ClickBlockPicture()
        self.Help.CloseBPPage()
        Result = self.Public.ShowWaitV_until_not('xpath&&%s' % Element.CloseBlockPicturePage)
        assert Result != False

    def test_DownloadH(self):
        """
        下载硬件助手
        :return:
        """
        self.Help.ClickHelp()
        self.Help.ClickHardwareAssistant()
        oldL = len(os.listdir(path.DownloadP))
        self.Help.DLHardware()
        time.sleep(1)
        newL = len(os.listdir(path.DownloadP))
        assert oldL != newL
        self.driver.quit()
        os.remove(path.HL)

