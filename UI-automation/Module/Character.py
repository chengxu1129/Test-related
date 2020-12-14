from lib.Public import Public
from lib import Element
from lib import TestData
from selenium.webdriver.common.action_chains import ActionChains
import time


class Character(Public):

    def open_Addcharacter(self):
        self.ShowWaitVisibility('css&&%s' % Element.Addcharacter_button)
        self.GetElementClick('css&&%s' % Element.Addcharacter_button)

    def library_add_character(self):
        """
        素材库添加角色
        :return:
        """
        self.open_Addcharacter()
        self.ShowWaitVisibility('css&&%s' % Element.Library_character)
        self.GetElementClick('css&&%s' % Element.Library_character)
        self.ShowWaitVisibility('css&&%s' %Element.Character_id1)
        self.GetElementClick('css&&%s' % Element.Character_id1)
        self.GetElementClick('css&&%s' % Element.Character_id2)
        self.GetElementClick('css&&%s' % Element.Confirm_add)

    def drawingboard_add_character(self):
        """
        画板添加角色
        :return:
        """
        self.open_Addcharacter()
        self.GetElementClick('css&&%s' % Element.Drawingboard_character)
        self.GetElementClick('css&&%s' % Element.Drawing_Button)
        self.GetElementClick('css&&%s' % Element.Drawing_graph)
        self.GetElementClick('xpath&&%s' % Element.Confirm_add1)

    def random_add_character(self):
        """
        随机添加角色
        :return:
        """
        self.open_Addcharacter()
        self.GetElementClick('css&&%s' % Element.Random_character)
        self.GetElementClick('id&&%s' % Element.workspace_id)

    def upload_add_character(self,filepath):
        """
        本地添加角色
        :return:
        """
        self.open_Addcharacter()
        #self.GetElementSendKeys('css&&%s' % Element.loadwindow,filepath,delay=5)
        self.GetElementSendKeys('css&&%s' % Element.loadwindow, filepath)

    def del_character1(self):
        """
        删除角色，角色下无积木直接删除
        :return:
        """
        self.GetElementClick('css&&%s' % Element.del_icon1)

    def del_character2(self):
        """
        删除角色，角色下有积木，弹出二次确认框点击确认后删除
        :return:
        """
        self.GetElementClick('xpath&&%s' % Element.del_chara2)
        self.GetElementClick('css&&%s' % Element.del_icon2)
        self.GetElementClick('css&&%s' % Element.del_confirm)

    def copy_chara(self):
        """
        右键复制角色
        :return:
        """
        SEL_Chara = self.GetElement('css&&%s' % Element.select_chara)
        ActionChains(self.driver).context_click(SEL_Chara).perform()
        self.ShowWaitVisibility('css&&%s' % Element.copy)
        self.GetElementClick('css&&%s' % Element.copy)

    def rc_rename(self):
        """
        右键修改角色名称
        :return:
        """
        SEL_Chara = self.GetElement('css&&%s' % Element.select_chara)
        ActionChains(self.driver).context_click(SEL_Chara).perform()
        self.ShowWaitVisibility('css&&%s' % Element.rename)
        self.GetElementClick('css&&%s' % Element.rename)

    def rename_chara(self,cname):
        """
        角色改名
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.input_text)
        self.GetElementSendKeys('xpath&&%s' % Element.input_text, cname)
        self.GetElementClick('id&&%s' % Element.workspace_id)

    def ClinkChara(self):
        """
        单击角色名称
        :return:
        """
        self.GetElementClick('xpath&&%s' % Element.input_text)
        self.rename_chara(TestData.CRN1)

    def rc_export(self):
        """
        右键导出角色
        :return:
        """
        SEL_Chara = self.GetElement('css&&%s' % Element.select_chara)
        ActionChains(self.driver).context_click(SEL_Chara).perform()
        self.ShowWaitVisibility('css&&%s' %Element.export)
        self.GetElementClick('css&&%s' %Element.export)

    def rc_backpack(self):
        """
        右键添加角色至背包
        :return:
        """
        SEL_Chara = self.GetElement('css&&%s' % Element.select_chara)
        ActionChains(self.driver).context_click(SEL_Chara).perform()
        self.ShowWaitVisibility('css&&%s' % Element.add_backpack)
        self.GetElementClick('css&&%s' % Element.add_backpack)

    def rc_group(self):
        """
        右键创建分组
        :return:
        """
        SEL_Chara = self.GetElement('css&&%s' % Element.select_chara)
        ActionChains(self.driver).context_click(SEL_Chara).perform()
        self.ShowWaitVisibility('css&&%s' % Element.c_group)
        self.GetElementClick('css&&%s' % Element.c_group)

    def rc_G_copy(self):
        """
        右键复制分组
        :return:
        """
        Group = self.GetElement('css&&%s' % Element.group)
        ActionChains(self.driver).context_click(Group).perform()
        self.ShowWaitVisibility('css&&%s' % Element.g_copy)
        self.GetElementClick('css&&%s' % Element.g_copy)