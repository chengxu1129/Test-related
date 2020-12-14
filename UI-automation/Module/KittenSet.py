from lib.Public import Public
from lib import Element
from selenium.webdriver.common.action_chains import ActionChains



class KittenSet(Public):

    def ClickSet(self):
        """
        点击【设置】按钮
        :return:
        """
        self.ShowWaitVisibility('id&&%s' % Element.KittenSet)
        self.GetElementClick('id&&%s' % Element.KittenSet)

    def JGMLguage(self):
        """
        判断当前页面到底是什么语言
        :return:
        """
        JG = self.GetElement('css&&%s' % Element.Aboutkitten).text
        if JG == '关于Kitten':
            OneDriver = self.GetElement('xpath&&%s' % Element.SCNSet)
            return OneDriver

        JG = self.GetElement('css&&%s' % Element.Aboutkitten).text
        if JG == '關於Kitten':
            OneDriver = self.GetElement('xpath&&%s' % Element.TCNSet)
            return OneDriver

        JG = self.GetElement('css&&%s' % Element.Aboutkitten).text
        if JG == 'About Kitten':
            OneDriver = self.GetElement('xpath&&%s' % Element.ENSet)
            return OneDriver

    def ClickSimpleChinese(self):
        """
        点击简体中文
        :return:
        """
        OneDriver = self.JGMLguage()
        TwoDeiver = self.GetElement('css&&%s' % Element.SimpleChinese)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDeiver).perform()

    def ClickComplexChinese(self):
        """
        点击繁体中文
        :return:
        """
        OneDriver = self.JGMLguage()
        TwoDriver = self.GetElement('css&&%s' % Element.ComplexChinese)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()

    def ClickEnglish(self):
        """
        点击英语
        :return:
        """
        OneDriver = self.JGMLguage()
        TwoDriver = self.GetElement('css&&%s' % Element.English)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()


    def ColourSet(self,Colour):
        """
        设置主题颜色
        Colour：Yellow、Blue、Green、Orange、Violet、Gules
        Colour只能传以上参数，其他无效
        :param Colour:
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.ColourSet)
        if Colour == 'Yellow':
            OneDriver = self.GetElement('xpath&&%s' % Element.ColourSet)
            TwoDriver = self.GetElement('css&&%s' % Element.Yellow)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        elif Colour == 'Blue':
            OneDriver = self.GetElement('xpath&&%s' % Element.ColourSet)
            TwoDriver = self.GetElement('css&&%s' % Element.Blue)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        elif Colour == 'Green':
            OneDriver = self.GetElement('xpath&&%s' % Element.ColourSet)
            TwoDriver = self.GetElement('css&&%s' % Element.Green)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        elif Colour == 'Orange':
            OneDriver = self.GetElement('xpath&&%s' % Element.ColourSet)
            TwoDriver = self.GetElement('css&&%s' % Element.Orange)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        elif Colour == 'Violet':
            OneDriver = self.GetElement('xpath&&%s' % Element.ColourSet)
            TwoDriver = self.GetElement('css&&%s' % Element.Violet)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        elif Colour == 'Gules':
            OneDriver = self.GetElement('xpath&&%s' % Element.ColourSet)
            TwoDriver = self.GetElement('css&&%s' % Element.Gules)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        else:
            raise

    def BlockStyleSet(self,BlockSty):
        """
        积木样式设置
        BlockSty：MagnetStyle、ClassicStyle
        BlockSty只能传以上参数，其他无效
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.BlockStyle)
        if BlockSty == 'MagnetStyle':
            OneDriver = self.GetElement('xpath&&%s' % Element.BlockStyle)
            TwoDriver = self.GetElement('css&&%s' % Element.MagnetStyle)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        elif BlockSty == 'ClassicStyle':
            OneDriver = self.GetElement('xpath&&%s' % Element.BlockStyle)
            TwoDriver = self.GetElement('css&&%s' % Element.ClassicStyle)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        else:
            raise

    def BlockGroupStyleSet(self,BlockGroupStyle):
        """
        积木栏模式设置
        BlockGroupStyle：Collect、Fixed
        BlockGroupStyle只能传以上参数，其他无效
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.BlockGroupStyle)
        if BlockGroupStyle == 'Collect':
            OneDriver = self.GetElement('xpath&&%s' % Element.BlockGroupStyle)
            TwoDriver = self.GetElement('css&&%s' % Element.Collect)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        elif BlockGroupStyle == 'Fixed':
            OneDriver = self.GetElement('xpath&&%s' % Element.BlockGroupStyle)
            TwoDriver = self.GetElement('css&&%s' % Element.Fixed)
            ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()
        else:
            raise

    def ClickUserFeedback(self):
        """
        点击用户反馈
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.UserFeedback)
        self.GetElementClick('css&&%s' % Element.UserFeedback)

    def ClickEquipmentTesting(self):
        """
        点击设备检查按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.EquipmentTesting)
        self.GetElementClick('css&&%s' % Element.EquipmentTesting)

    def CloseRecheckPage(self):
        """
        关闭重新检查设备页面
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseRecheckPage)
        self.GetElementClick('xpath&&%s' % Element.CloseRecheckPage)

    def ClickRecheck(self):
        """
        点击重新检查
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Recheck)
        self.GetElementClick('css&&%s' % Element.Recheck)

    def CliskNemoProgramming(self):
        """
        点击Nemo编程
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.NemoProgramming)
        self.GetElementClick('css&&%s' % Element.NemoProgramming)

    def CloseNemoPage(self):
        """
        关闭Nemo编程页面
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseNemoPage)
        self.GetElementClick('xpath&&%s' % Element.CloseNemoPage)

    def ClickAboutkitten(self):
        """
        点击关于Kitten
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Aboutkitten)
        self.GetElementClick('css&&%s' % Element.Aboutkitten)

    def CloseAboutKitten(self):
        """
        关闭【关于Kitten】页面
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseAboutKitten)
        self.GetElementClick('xpath&&%s' % Element.CloseAboutKitten)

