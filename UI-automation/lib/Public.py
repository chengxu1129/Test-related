from lib.WebAutoTestFlow import AutoLib
from lib import Element,TestData





class Public(AutoLib):

# 通用登录

    def ClickLoginButton(self):
        """
        点击登录按钮，打开登录窗口
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.login_button)
        self.GetElementClick('css&&%s' % Element.login_button)

    def InputUserInfo(self,user=None,password=None):
        """
        账号密码登录页面功能
        :param user: 传入账号
        :param password: 传入密码
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.user_input)
        self.GetElementSendKeys('css&&%s' % Element.user_input,user)
        self.GetElementSendKeys('css&&%s' % Element.password_input,password)
        self.GetElementClick('css&&%s' % Element.pass_button)

# ------------------------------------------------------------------------------

    def SuccessLogin(self,user=TestData.User,password=TestData.Pswd):
        """
        成功登陆账号功能
        :return:
        """
        self.ClickLoginButton()
        self.InputUserInfo(user,password)


# 新手引导页

    def CloseGuide(self):
        """
        关闭新手引导页
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.CloseGuide)
        self.GetElementClick('css&&%s' % Element.CloseGuide)

    def CreateNow(self):
        """
        新手引导页的立即创作
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.CreateNow)
        self.GetElementClick('css&&%s' % Element.CreateNow)

    def OK(self):
        """
        关闭引导页后，提示引导页路径
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.OK)
        self.GetElementClick('css&&%s' % Element.OK)

# ------------------------------------------------------------------------------

    def CloseGP(self):
        """
        关闭引导页
        :return:
        """
        self.CloseGuide()
        self.OK()