from lib.Public import Public
from lib import Element




class Stage(Public):

    def ClickRun(self):
        """
        点击运行
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Run)
        self.GetElementClick('css&&%s' % Element.Run)

    def RunStatus(self,Status):
        """
        选择运行状态
        Status:one   ----  第一屏运行
        Status:now  ----  从当前屏运行
        :param Status:
        :return:
        """
        if Status == 'one':
            self.ShowWaitVisibility('css&&%s' % Element.RunOne)
            self.GetElementClick('css&&%s' % Element.RunOne)
            self.ShowWaitVisibility('css&&%s' % Element.RunTwos)
            self.GetElementClick('css&&%s' % Element.RunTwos)
        elif Status == 'now':
            self.ShowWaitVisibility('css&&%s' % Element.RunOne)
            self.GetElementClick('css&&%s' % Element.RunOne)
            self.ShowWaitVisibility('css&&%s' % Element.RunTwo)
            self.GetElementClick('css&&%s' % Element.RunTwo)
        else:
            raise

    def Proportion(self,PT):
        """
        切换舞台比例
        PT:1  --- 竖屏
        PT:2  --- 4:3
        PT:3  --- 16:9
        :return:
        """
        if PT == 1:
            self.ShowWaitVisibility('id&&%s' % Element.Proportion)
            self.GetElementClick('id&&%s' % Element.Proportion)
            self.ShowWaitVisibility('css&&%s' % Element.Vertical)
            self.GetElementClick('css&&%s' % Element.Vertical)
        elif PT == 2:
            self.ShowWaitVisibility('id&&%s' % Element.Proportion)
            self.GetElementClick('id&&%s' % Element.Proportion)
            self.ShowWaitVisibility('css&&%s' % Element.Horizontal)
            self.GetElementClick('css&&%s' % Element.Horizontal)
        elif PT == 3:
            self.ShowWaitVisibility('id&&%s' % Element.Proportion)
            self.GetElementClick('id&&%s' % Element.Proportion)
            self.ShowWaitVisibility('css&&%s' % Element.Horizontals)
            self.GetElementClick('css&&%s' % Element.Horizontals)
        else:
            raise

    def Grid(self,Grid):
        """
        网格开关
        Grid:1   ------ 打开网格
        Grid:2   ------ 关闭网格
        :param Grid:
        :return:
        """
        if Grid == 1:
            self.ShowWaitVisibility('css&&%s' % Element.OpenGrid)
            self.GetElementClick('css&&%s' % Element.OpenGrid)
        elif Grid == 2:
            self.ShowWaitVisibility('css&&%s' % Element.CloseGrid)
            self.GetElementClick('css&&%s' % Element.CloseGrid)

    def FullScreen(self):
        """
        打开全屏
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.FullScreen)
        self.GetElementClick('css&&%s' % Element.FullScreen)

    def CloseFS(self):
        """
        关闭全屏
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.CloseFS)
        self.GetElementClick('css&&%s' % Element.CloseFS)

    def PhoneCheck(self):
        """
        点击手机预览按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Phone)
        self.GetElementClick('css&&%s' % Element.Phone)
