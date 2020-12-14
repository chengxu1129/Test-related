from lib.Public import Public
from lib import Element,TestData
from selenium.webdriver.common.action_chains import ActionChains




class Screen(Public):

    def UnfoldScreen(self):
        """
        点击展开屏幕按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Unfold)
        self.GetElementClick('css&&%s' % Element.Unfold)

    def AddScreen(self):
        """
        点击 添加新的空白屏幕
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.AddScreen)
        self.GetElementClick('css&&%s' % Element.AddScreen)

    def DelScreen(self):
        """
        删除屏幕
        :return:
        """
        self.ShowWaitVisibility('id&&%s' % Element.TwoScreen)
        Two = self.GetElement('id&&%s' % Element.TwoScreen)
        # 右键操作
        ActionChains(self.driver).context_click(Two).perform()
        self.ShowWaitVisibility('css&&%s' % Element.DelScreen)
        self.GetElementClick('css&&%s' % Element.DelScreen)

    def CopyScreen(self):
        """
        复制屏幕
        :return:
        """
        self.ShowWaitVisibility('id&&%s' % Element.OneScreen)
        One = self.GetElement('id&&%s' % Element.OneScreen)
        # 右键操作
        ActionChains(self.driver).context_click(One).perform()
        self.ShowWaitVisibility('css&&%s' % Element.CopyScreen)
        self.GetElementClick('css&&%s' % Element.CopyScreen)

    def CSRename(self):
        """
        屏幕展开后，右键点击重命名
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Aimg)
        img = self.GetElement('css&&%s' % Element.Aimg)
        ActionChains(self.driver).context_click(img).perform()
        self.ShowWaitVisibility('css&&%s' % Element.SRN)
        self.GetElementClick('css&&%s' % Element.SRN)

    def ClickSN(self):
        """
        点击缩略图名称
        :return:
        """
        C = '//span[contains(text(), "%s")]' % TestData.SRN
        self.ShowWaitPresence('xpath&&%s' % C)
        self.GetElementClick('css&&%s' % Element.ipt)

    def SRename(self,name):
        """
        修改屏幕名称
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.ipt)
        self.GetElementSendKeys('css&&%s' % Element.ipt,name)

    def CS(self):
        """
        展开屏幕后复制屏幕
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Aimg)
        img = self.GetElement('css&&%s' % Element.Aimg)
        ActionChains(self.driver).context_click(img).perform()
        self.ShowWaitVisibility('css&&%s' % Element.CS)
        self.GetElementClick('css&&%s' % Element.CS)





