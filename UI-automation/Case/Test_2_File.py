from Module import Login,File,BcmPage,SaveAndRelease,HistoryVersion,NewBcmPage
from selenium import webdriver
from lib import TestData,Element,Public




class TestFile():

    @classmethod
    def setup_class(cls):
        # cls.driver = webdriver.Chrome(executable_path=DriverDir)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.Save = SaveAndRelease.SRFeatures(cls.driver)
        cls.HV = HistoryVersion.History(cls.driver)
        cls.Login = Login.Login(cls.driver)
        cls.BcmPage = BcmPage.BcmPage(cls.driver)
        cls.NBP = NewBcmPage.NewBP(cls.driver)
        cls.File = File.File(cls.driver)


    def test_NewBcm(self):
        """
        检查是否可跳转到新建页面
        :return:
        """
        self.Public.CloseGP()
        self.Public.SuccessLogin()
        self.File.ClickFilebutton()
        self.File.NewBcm()
        self.NBP.CreatNB()
        Result = self.Public.ShowWaitV_until_not('css&&%s' % Element.disappear)
        assert Result != False

    def test_SaveTips(self):
        """
        查看作品改动后，新建空白作品，是否有提示
        :return:
        """
        self.Save.InputFileName(TestData.BcmName)
        self.File.ClickFilebutton()
        self.File.NewBcm()
        self.NBP.CreatNB()
        Result = self.Public.ShowWaitVisibility('css&&%s' % Element.not_save)
        assert Result != False
        self.Public.GetElementClick('css&&%s' % Element.cancel)

    def test_OpenFile(self):
        """
        查看是否能进入作品页面
        :return:
        """
        self.File.ClickFilebutton()
        self.File.OpenFile()
        Result = self.Public.ShowWaitVisibility('css&&%s' % Element.release_yes)
        assert Result != False

    def test_ReleaseState(self):
        """
        已发布：发布在社区的作品
        未发布：保存但未发布的作品
        :return:
        """
        self.BcmPage.ClickReleaseBcm()
        OneName = self.Public.GetElement('xpath&&%s' % Element.RName).text
        self.BcmPage.ClickNoReleaseBcm()
        TwoName = self.Public.GetElement('xpath&&%s' % Element.RName).text
        assert OneName != TwoName

    def test_GrepBcmOne(self):
        """
        查看搜索作品是否区分已发布、未发布
        :return:
        """
        self.BcmPage.InputBcmName('神奇作品三十分钟')
        Result = self.Public.ShowWaitV_until_not('xpath&&%s' % Element.RName)
        assert Result != False

    def test_GrepBcmTwo(self):
        """
        查看搜索作品是否区分已发布、未发布
        :return:
        """
        self.BcmPage.ClickReleaseBcm()
        self.BcmPage.InputBcmName('TestFile')
        Result = self.Public.ShowWaitV_until_not('xpath&&%s' % Element.RName)
        assert Result != False
        self.BcmPage.CloseFilePage()

    def test_CheckHV(self):
        """
        保存作品后，查看是否有历史版本
        :return:
        """
        self.Save.ClickSave()
        self.File.ClickFilebutton()
        self.File.HistoryFile()
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.HistoryTime)
        assert Result != False
        self.HV.CloseHVPage()

    def test_AlsSave(self):
        """
        查看作品是否可以另存为
        :return:
        """
        self.File.ClickFilebutton()
        self.File.AlsSave()
        self.Public.ShowWaitVisibility('xpath&&//div[contains(text(), "作品保存成功")]')
        # 获取元素中的值
        BcmName = self.Public.GetElement('css&&%s' % Element.FileName).get_attribute('value')
        assert '副本' in BcmName
        self.driver.quit()

