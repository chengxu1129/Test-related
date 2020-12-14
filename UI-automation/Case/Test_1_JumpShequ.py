from Module import Login
from selenium import webdriver
from lib import TestData,Public



class TestJumpShequ():

    @classmethod
    def setup_class(cls):
        # cls.driver = webdriver.Chrome(executable_path=DriverDir)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.Login = Login.Login(cls.driver)

    def test_JumpShequ(self):
        """
        跳转到社区
        :return:
        """
        self.Public.CloseGP()
        self.Login.JumpShequ()
        # 获取当前浏览器所有句柄
        all_h = self.driver.window_handles
        # 切换到最后一个句柄
        self.driver.switch_to.window(all_h[-1])
        SHurl = self.driver.current_url
        assert SHurl == TestData.SHurl
        self.driver.quit()
