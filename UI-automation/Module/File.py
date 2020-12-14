from lib.Public import Public
from lib import Element



# 文件夹功能

class File(Public):

    def ClickFilebutton(self):
        """
        点击菜单栏的【文件】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.file_button)
        self.GetElementClick('css&&%s' % Element.file_button)

    def NewBcm(self):
        """
        点击【文件】-->【新建】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.new_bcm)
        self.GetElementClick('css&&%s' % Element.new_bcm)

    def OpenFile(self):
        """
        点击【文件】-->【打开】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.open_file_button)
        self.GetElementClick('css&&%s' % Element.open_file_button)

    def HistoryFile(self):
        """
        点击【文件】-->【历史版本】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.history_file_button)
        self.GetElementClick('css&&%s' % Element.history_file_button)

    def AlsSave(self):
        """
        点击【文件】-->【另存为】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.als_save_button)
        self.GetElementClick('css&&%s' % Element.als_save_button)

    def OpenLocalFile(self):
        """
        点击【文件】-->【打开电脑文件】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.open_win_file_button)
        self.GetElementClick('css&&%s' % Element.open_win_file_button)

    def SaveLocal(self):
        """
        点击【文件】-->【保存到电脑】按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.file_save_win_button)
        self.GetElementClick('css&&%s' % Element.file_save_win_button)


