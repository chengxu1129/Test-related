from lib import Public,TestData,Element
from Module import Screen
from selenium import webdriver




class TestScreen():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.Screen = Screen.Screen(cls.driver)

    def test_CopyScreen(self):
        """
        复制屏幕
        :return:
        """
        self.Public.CloseGP()
        self.Screen.CopyScreen()
        Result = self.Public.ShowWaitVisibility('id&&%s' % Element.TwoScreen)
        assert Result != False

    def test_DelScreen(self):
        """
        删除屏幕
        :return:
        """
        self.Screen.DelScreen()
        YD = 'div[data-report-click="屏幕-确认删除"]'
        self.Public.ShowWaitVisibility('css&&%s' % YD)
        self.Public.GetElementClick('css&&%s' % YD)
        Result = self.Public.ShowWaitV_until_not('id&&%s' % Element.TwoScreen)
        assert Result != False

    def test_SRename(self):
        """
        展开屏幕，查看右键是否能修改名字
        :return:
        """
        self.Screen.UnfoldScreen()
        self.Screen.CSRename()
        self.Screen.SRename(TestData.SRN)
        name = self.Public.GetElement('css&&%s' % Element.ipt).get_attribute('value')
        assert name == TestData.SRN

    def test_CSRN(self):
        """
        展开屏幕，查看点击名称是否能修改名字
        :return:
        """
        self.Public.GetElementClick('css&&%s' % Element.Aimg)
        self.Screen.ClickSN()
        self.Screen.SRename('Screen')
        name = self.Public.GetElement('css&&%s' % Element.ipt).get_attribute('value')
        assert name == 'Screen'

    def test_CS(self):
        """
        展开复制屏幕
        :return:
        """
        self.Screen.CS()

        self.driver.quit()