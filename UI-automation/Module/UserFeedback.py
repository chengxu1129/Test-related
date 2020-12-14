from lib.Public import Public
from lib import Element



class UserFeedback(Public):


    def ClickUFB(self):
        """
        点击属性栏的用户反馈
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.UFB)
        self.GetElementClick('css&&%s' % Element.UFB)

