from lib.Public import Public
from lib import Element



# 登录功能

class Login(Public):

    def JumpShequ(self):
        """
        跳转到社区
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.shequ_jump)
        self.GetElementClick('css&&%s' % Element.shequ_jump)

    # def ClickLoginButton(self):
    #     """
    #     点击登录按钮，打开登录窗口
    #     :return:
    #     """
    #     self.ShowWaitVisibility('css&&%s' % Element.login_button)
    #     self.GetElementClick('css&&%s' % Element.login_button)

    def DeleteUserInfo(self):
        """
        在账号、密码登录页面，清空账号、密码输入框内容
        :return:
        """
        self.GetElement('css&&%s' % Element.user_input).clear()
        self.GetElement('css&&%s' % Element.password_input).clear()

    # def InputUserInfo(self,user=None,password=None):
    #     """
    #     账号密码登录页面功能
    #     :param user: 传入账号
    #     :param password: 传入密码
    #     :return:
    #     """
    #     self.ShowWaitVisibility('css&&%s' % Element.user_input)
    #     self.GetElementSendKeys('css&&%s' % Element.user_input,user)
    #     self.GetElementSendKeys('css&&%s' % Element.password_input,password)
    #     self.GetElementClick('css&&%s' % Element.pass_button)

    def ClickInfo(self):
        """
        登录成功后，点击【用户头像】
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.user_info)
        self.GetElementClick('xpath&&%s' % Element.user_info)

    def MyBcm(self):
        """
        点击【我的作品】
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.user_bcm)
        self.GetElementClick('css&&%s' % Element.user_bcm)

    def UserInfoSet(self):
        """
        点击【账号设置】
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.user_set)
        self.GetElementClick('css&&%s' % Element.user_set)

    def OutLogin(self):
        """
        点击【退出登录】
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.quit_login)
        self.GetElementClick('css&&%s' % Element.quit_login)

