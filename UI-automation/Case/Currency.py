# from Module import Login
from Module import Login,Public
from lib import TestData,Element
from lib.WebAutoTestFlow import AutoLib



class Currency(AutoLib):

    def __init__(self,driver):
        # cls.driver = webdriver.Chrome(executable_path=DriverDir)
        super().__init__(driver)
        self.Login = Login.Login(self.driver)
        # self.driver = self.Login.driver


    def SuccessLogin(self):
        """
        成功登陆账号功能
        :return:
        """
        self.Login.ClickLoginButton()
        self.Login.InputUserInfo(TestData.User,TestData.Pswd)

    def CloseGP(self):
        """
        关闭新手引导页面
        :return:
        """

