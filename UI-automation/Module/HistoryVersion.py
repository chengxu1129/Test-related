from lib.Public import Public
from lib import Element
from selenium.webdriver.common.action_chains import ActionChains
from lib.WebAutoTestFlow import AutoLib



# 历史版本
class History(Public):

    # def __init__(self,driver):
    #     # self.public = Public.Public(driver)
    #     super()
    #     self.driver = self.driver

    def ClickVersion(self):
        """
        点击历史版本的查看按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.HistoryTime)
        OneDriver = self.GetElement('xpath&&%s' % Element.HistoryTime)
        TwoDriver = self.GetElement('css&&%s' % Element.CheckHistory)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()

    def CloseHVPage(self):
        """
        关闭历史页面
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseHVPage)
        self.GetElementClick('xpath&&%s' % Element.CloseHVPage)