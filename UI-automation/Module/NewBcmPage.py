from lib.Public import Public
from lib import Element




class NewBP(Public):

    def All(self):
        """
        全部示例程序
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.All)
        self.GetElementClick('xpath&&%s' % Element.All)

    def Game(self):
        """
        点击游戏类模板
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Game)
        self.GetElementClick('xpath&&%s' % Element.Game)

    def Tool(self):
        """
        点击工具类模板
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Tools)
        self.GetElementClick('xpath&&%s' % Element.Tools)

    def CreatNB(self):
        """
        新建空白作品
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.CreatNB)
        self.GetElementClick('css&&%s' % Element.CreatNB)
