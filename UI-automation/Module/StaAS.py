from lib.Public import Public
from lib import Element
from selenium.webdriver.common.keys import Keys

Character = 'div[data-report-click="角色栏-选中角色"]'
Free = '//div[contains(text(), "自由旋转")]'
About = '//div[contains(text(), "左右翻转")]'
Prohibit = '//div[contains(text(), "禁止旋转")]'





class StaAS(Public):

    def ToBG(self):
        """
        切换到背景
        :return:
        """
        self.ShowWaitVisibility(Element.BG)
        self.GetElementClick(Element.BG)

    def ClickBG(self):
        """
        点击隐藏按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.DBG)
        self.GetElementClick('css&&%s' % Element.DBG)

    def Character(self):
        """
        切换到第一个角色
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Character)
        self.GetElementClick('css&&%s' % Character)

    def Locking(self):
        """
        点击锁定按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Locking)
        self.GetElementClick('css&&%s' % Element.Locking)

    def Spin(self):
        """
        点击旋转按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Spin)
        self.GetElementClick('css&&%s' % Element.Spin)

    def SpinSet(self,Spin):
        """
        角色旋转设置
        Spin:1  -----  自由
        Spin:2  -----  左右
        Spin:3  -----  禁止
        :return:
        """
        if Spin == 1:
            self.ShowWaitVisibility('xpath&&%s' % Free)
            self.GetElementClick('xpath&&%s' % Free)
        elif Spin == 2:
            self.ShowWaitVisibility('xpath&&%s' % About)
            self.GetElementClick('xpath&&%s' % About)
        elif Spin == 3:
            self.ShowWaitVisibility('xpath&&%s' % Prohibit)
            self.GetElementClick('xpath&&%s' % Prohibit)
        else:
            raise

    def XC(self,x):
        """
        X坐标设置
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Xa)
        self.GetElementSendKeys('xpath&&%s' % Element.Xa,x)

    def YC(self,y):
        """
        Y坐标设置
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Ya)
        self.GetElementSendKeys('xpath&&%s' % Element.Ya,y)

    def Size(self,y):
        """
        角色大小设置
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Ia)
        Size = self.GetElement('xpath&&%s' % Element.Ia)
        Size.send_keys(Keys.CONTROL + 'a')
        Size.send_keys(Keys.BACKSPACE)
        self.GetElementSendKeys('xpath&&%s' % Element.Ia,y)

    def Angle(self,y):
        """
        角色角度设置
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Ka)
        self.GetElementSendKeys('xpath&&%s' % Element.Ka,y)

