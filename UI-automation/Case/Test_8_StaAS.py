from lib import Public,TestData,Element
from selenium import webdriver
from Module import StaAS



class TestStaAS():

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.StaAS = StaAS.StaAS(cls.driver)

    def test_HDBG(self):
        """
        隐藏/显示背景
        :return:
        """
        self.Public.CloseGP()
        self.StaAS.ToBG()
        self.StaAS.ClickBG()
        DBG = '//span[contains(text(), "背景已隐藏")]'
        self.Public.ShowWaitVisibility('xpath&&%s' % DBG)
        self.StaAS.ClickBG()
        DBG = '//span[contains(text(), "背景已显示")]'
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % DBG)
        assert Result != False

    def test_HDC(self):
        """
        隐藏/显示角色
        :return:
        """
        self.StaAS.Character()
        self.StaAS.ClickBG()
        DBG = '//span[contains(text(), "角色已隐藏")]'
        self.Public.ShowWaitVisibility('xpath&&%s' % DBG)
        self.StaAS.ClickBG()
        DBG = '//span[contains(text(), "角色已显示")]'
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % DBG)
        assert Result != False

    def test_Locking(self):
        """
        查看是否能锁定/解锁角色
        :return:
        """
        self.StaAS.Locking()
        L = '//span[contains(text(), "角色已锁定")]'
        self.Public.ShowWaitVisibility('xpath&&%s' % L)
        self.StaAS.Locking()
        L = '//span[contains(text(), "角色未锁定")]'
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % L)
        assert Result != False

    def test_Spin(self):
        """
        查看角色是否能旋转
        :return:
        """
        self.StaAS.Spin()
        self.StaAS.SpinSet(2)
        S = '//div[contains(text(), "自由旋转")]'
        Result = self.Public.ShowWaitV_until_not('xpath&&%s' % S)
        assert Result != False

    def test_X(self):
        """
        X坐标设置
        :return:
        """
        self.StaAS.XC(100)
        Result = self.Public.GetElement('xpath&&%s' % Element.Xa).get_attribute('value')
        assert Result == '100'

    def test_Y(self):
        """
        Y坐标设置
        :return:
        """
        self.StaAS.YC(100)
        Result = self.Public.GetElement('xpath&&%s' % Element.Xa).get_attribute('value')
        assert Result == '100'

    def test_RoleSize(self):
        """
        查看角色是否能设置大小
        :return:
        """
        self.StaAS.Size(50)
        Result = self.Public.GetElement('xpath&&%s' % Element.Ia).get_attribute('value')
        assert Result == '50'

    def test_RoleAngle(self):
        """
        查看角色是否能设置角度
        :return:
        """
        self.StaAS.Angle(180)
        Result = self.Public.GetElement('xpath&&%s' % Element.Ka).get_attribute('value')
        assert Result == '180'


        self.driver.quit()

