from lib.Public import Public
from lib import Element



# 云端作品页面功能

class BcmPage(Public):

    def CloseFilePage(self):
        """
        关闭文件页面
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.CloseFilePage)
        self.GetElementClick('css&&%s' % Element.CloseFilePage)

    def OneBCM(self):
        """
        点击第一个文件
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.one_bcm)
        self.GetElementClick('css&&%s' % Element.one_bcm)

    def ObtainVersion(self):
        """
        点击展开【所有版本】
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.check_version)
        self.GetElementClick('css&&%s' % Element.check_version)

    def ClickAllVersion(self):
        """
        【所有版本】-->点击【所有版本】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.all_version)
        self.GetElementClick('css&&%s' % Element.all_version)

    def ClickFourVersion(self):
        """
        【所有版本】-->点击【4.0】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.four_version)
        self.GetElementClick('css&&%s' % Element.four_version)

    def ClickThreeVersion(self):
        """
        【所有版本】-->点击【3.0】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.three_version)
        self.GetElementClick('css&&%s' % Element.three_version)

    def ClickAllBcm(self):
        """
        点击【全部】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.all_bcm)
        self.GetElementClick('css&&%s' % Element.all_bcm)

    def ClickReleaseBcm(self):
        """
        点击已发布
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.release_yes)
        self.GetElementClick('css&&%s' % Element.release_yes)

    def ClickNoReleaseBcm(self):
        """
        点击未发布
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.release_no)
        self.GetElementClick('css&&%s' % Element.release_no)

    def InputBcmName(self,BcmName):
        """
        搜索框输入搜索内容
        :return:
        """
        self.ShowWaitVisibility(Element.search_for_bcm)
        # BcmName = self.GetElement('xpath&&%s' % Element.bcm_name).text
        self.GetElementSendKeys(Element.search_for_bcm,BcmName)
