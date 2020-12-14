from Module import KittenSet,UserFeedback
from selenium import webdriver
from lib import Element,TestData,Public




class TestHelp():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.Set = KittenSet.KittenSet(cls.driver)
        cls.UFB = UserFeedback.UserFeedback(cls.driver)

    def test_TCNSet(self):
        """
        中文繁体设置
        :return:
        """
        self.Public.CloseGP()
        self.Public.SuccessLogin()
        self.Set.ClickSet()
        self.Set.ClickComplexChinese()
        Result = self.Public.GetElement('css&&%s' % Element.Release).text
        assert '發布' == Result

    def test_ENSet(self):
        """
        英文设置
        :return:
        """
        self.Set.ClickSet()
        self.Set.ClickEnglish()
        Result = self.Public.GetElement('css&&%s' % Element.Release).text
        assert 'Publish' == Result

    def test_SCNSet(self):
        """
        中文简体设置
        :return:
        """
        self.Set.ClickSet()
        self.Set.ClickSimpleChinese()
        Result = self.Public.GetElement('css&&%s' % Element.Release).text
        assert '发布' == Result

    def test_Colour(self):
        """
        切换主题颜色
        :return:
        """
        self.Set.ClickSet()
        self.Set.ColourSet('Blue')
        self.Public.ShowWaitV_until_not('css&&%s' % Element.Yellow)
        self.Set.ClickSet()
        self.Set.ColourSet('Green')
        self.Public.ShowWaitV_until_not('css&&%s' % Element.Blue)
        self.Set.ClickSet()
        self.Set.ColourSet('Orange')
        self.Public.ShowWaitV_until_not('css&&%s' % Element.Green)
        self.Set.ClickSet()
        self.Set.ColourSet('Violet')
        self.Public.ShowWaitV_until_not('css&&%s' % Element.Orange)
        self.Set.ClickSet()
        self.Set.ColourSet('Gules')
        self.Public.ShowWaitV_until_not('css&&%s' % Element.Violet)
        self.Set.ClickSet()
        self.Set.ColourSet('Yellow')
        Gules = 'header[style="height: 52px; z-index: 1; box-shadow: rgba(255, 41, 112, 0.5) 0px 2px 4px 0px;"]'
        Result = self.Public.ShowWaitV_until_not('css&&%s' % Gules)
        assert Result != False

    def test_BS(self):
        """
        积木样式切换
        :return:
        """
        MagnetStyle = '//*[@id="header-setting-btn"]/div[2]/div[4]/div[3]/div[1]/div/span/div/svg'
        ClassicStyle = '//*[@id="header-setting-btn"]/div[2]/div[4]/div[3]/div[2]/div/span/div/svg'
        self.Set.ClickSet()
        self.Set.BlockStyleSet('ClassicStyle')
        self.Public.ShowWaitV_until_not('xpath&&%s' % MagnetStyle)
        self.Set.ClickSet()
        self.Set.BlockStyleSet('MagnetStyle')
        Result = self.Public.ShowWaitV_until_not('xpath&&%s' % ClassicStyle)
        assert Result != False

    def test_Feedback(self):
        """
        查看是否可跳转用户反馈
        :return:
        """
        self.Set.ClickSet()
        self.Set.ClickUserFeedback()
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[-1])
        FBurl = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(all_h[0])
        assert FBurl == TestData.Feedback

    def test_NemoWin(self):
        """
        查看是否能打开Nemo的弹窗
        :return:
        """
        self.Set.ClickSet()
        self.Set.CliskNemoProgramming()
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.CloseNemoPage)
        assert Result != False
        self.Set.CloseNemoPage()

    def test_AK(self):
        """
        查看关于KItten这个功能是否正常
        :return:
        """
        self.Set.ClickSet()
        self.Set.ClickAboutkitten()
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.CloseAboutKitten)
        assert Result != False
        self.Set.CloseAboutKitten()

    def test_GS(self):
        """
        查看积木栏是否可以切换模式
        :return:
        """
        self.Set.ClickSet()
        # 切换到常驻模式
        self.Set.BlockGroupStyleSet('Fixed')
        Fixed = '//*[@id="header-setting-btn"]/div[2]/div[5]/div[3]/div[2]/div/span/div'
        self.Public.ShowWaitPresence('xpath&&%s' % Fixed)
        self.Set.ClickSet()
        # 切换到收起模式
        self.Set.BlockGroupStyleSet('Collect')
        Collect = '//*[@id="header-setting-btn"]/div[2]/div[5]/div[3]/div[1]/div/span/div'
        Result = self.Public.ShowWaitPresence('xpath&&%s' % Collect)
        assert Result != False

    def test_TB(self):
        """
        顶部问题反馈
        :return:
        """
        self.UFB.ClickUFB()
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[-1])
        FBurl = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(all_h[0])
        assert FBurl == TestData.Feedback




        self.driver.quit()