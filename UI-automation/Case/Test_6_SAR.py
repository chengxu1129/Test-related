from lib import Public,TestData,Element
from Module import SaveAndRelease,File,BcmPage,NewBcmPage
from selenium import webdriver




class TestSar():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.Sar = SaveAndRelease.SRFeatures(cls.driver)
        cls.File = File.File(cls.driver)
        cls.BP = BcmPage.BcmPage(cls.driver)
        cls.NewBP = NewBcmPage.NewBP(cls.driver)

    def test_ModifyBN(self):
        """
        查看重名是否+1
        :return:
        """
        self.Public.CloseGP()
        self.Public.SuccessLogin()
        self.File.ClickFilebutton()
        self.File.OpenFile()
        NBN = self.Public.GetElement('xpath&&%s' % Element.bcm_name).text
        self.BP.CloseFilePage()
        self.Sar.InputFileName(NBN)
        self.Sar.ClickSave()
        self.Public.ShowWaitVisibility('xpath&&%s' % Element.SaveS)
        # 获取HTML某个元素的值
        BN = self.Public.GetElement('css&&%s' % Element.FileName).get_attribute('value')
        assert NBN != BN

    def test_Release(self):
        """
        查看发布是否正常
        :return:
        """
        self.File.ClickFilebutton()
        self.File.NewBcm()
        self.NewBP.CreatNB()
        self.Sar.ClickRelease()
        self.Sar.ClickDtermRas()
        Res = '//div[contains(text(), "作品发布成功")]'
        self.Public.ShowWaitVisibility('xpath&&%s' % Res)
        UI = 'success_publish_qr_code'
        Result = self.Public.ShowWaitVisibility('id&&%s' % UI)
        assert Result != False


        self.driver.quit()
