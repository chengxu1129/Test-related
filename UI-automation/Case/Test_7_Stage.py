from lib import Public,Element,TestData
from Module import Stage,Screen
from selenium import webdriver


RunStatus = '//span[contains(text(), "积木运行中，点击停止")]'




class TestStage():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.Stage = Stage.Stage(cls.driver)
        cls.Screen = Screen.Screen(cls.driver)

    def test_Run(self):
        """
        查看是否可以正常运行作品
        :return:
        """
        self.Public.CloseGP()
        self.Public.SuccessLogin()
        self.Stage.ClickRun()
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % RunStatus)
        assert Result != False

    def test_ScreenRun(self):
        """
        在指定屏幕运行
        :return:
        """
        self.Screen.UnfoldScreen()
        self.Screen.AddScreen()
        self.Stage.RunStatus('now')
        self.Stage.ClickRun()
        One = self.Public.GetElement('id&&%s' % Element.OneScreen).get_attribute('class')
        Two = self.Public.GetElement('id&&%s' % Element.TwoScreen).get_attribute('class')
        assert len(Two) > len(One)

    def test_Ratio(self):
        """
        切换屏幕比例运行，查看是否异常
        False
        :return:
        """
        W = 'canvas[width="620"][height="900"]'
        Vertical = self.Public.GetElement('css&&%s' % W).get_attribute('width')
        self.Stage.Proportion(2)
        WL= 'canvas[width="960"][height="720"]'
        Horizontal = self.Public.GetElement('css&&%s' % WL).get_attribute('width')
        self.Stage.ClickRun()
        self.Public.ShowWaitVisibility('xpath&&%s' % RunStatus)
        assert Horizontal != Vertical

    def test_Grid(self):
        """
        查看网格开关是否正常
        :return:
        """
        self.Stage.Grid(1)
        Result = self.Public.ShowWaitVisibility('css&&%s' % Element.CloseGrid)
        assert Result != False

    def test_FullScreen(self):
        """
        查看全屏功能是否正常
        :return:
        """
        self.Stage.FullScreen()
        Result = self.Public.ShowWaitV_until_not('css&&%s' % Element.FullScreen)
        self.Stage.CloseFS()
        assert Result != False

    def test_PhoneCheck(self):
        """
        查看手机预览功能是否正常
        :return:
        """
        self.Stage.PhoneCheck()
        Result = self.Public.ShowWaitVisibility('css&&%s' % Element.PhoneUrl)
        assert Result != False


        self.driver.quit()