from lib import Element
from lib.Public import Public
from selenium.webdriver.common.action_chains import ActionChains



class BackPack(Public):

    def ClickBackPack(self):
        """
        打开背包素材
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.BackPack)
        self.GetElementClick('css&&%s' % Element.BackPack)
        self.ShowWaitVisibility('xpath&&%s' % Element.OneGroupOneRole)
        self.RoleName = self.GetElement('xpath&&%s' % Element.OneGroupOneRole).text

    def CloseBackPack(self):
        """
        关闭背包
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseBackPack)
        self.GetElementClick('xpath&&%s' % Element.CloseBackPack)

    def ClickRole(self):
        """
        点击背包的角色
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.OneGroupOneRole)
        self.GetElementClick('xpath&&%s' % Element.OneGroupOneRole)

    def DeleteRole(self):
        """
        添加在下方的角色栏的第一个角色的删除按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.OneRole)
        OneDriver = self.GetElement('xpath&&%s' % Element.OneRole)
        TwoDriver = self.GetElement('xpath&&%s' % Element.DeleteRole)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()

    def EmptyRole(self):
        """
        点击清空按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Empty)
        self.GetElementClick('xpath&&%s' % Element.Empty)

    def DetermineAddRole(self):
        """
        点击确认添加角色按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.DetermineAddRole)
        self.GetElementClick('xpath&&%s' % Element.DetermineAddRole)

    def AddGroup(self):
        """
        点击添加分组按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.AddGroup)
        self.GetElementClick('xpath&&%s' % Element.AddGroup)

    def CancelAddGroup(self,cancel):
        """
        关闭新建分组页面
        cancel传参
            传x：点击右上角关闭按钮
            传cancel：点击取消按钮
        :return:
        """
        if cancel == 'x':
            self.ShowWaitVisibility('xpath&&%s' % Element.CloseGroupWin)
            self.GetElementClick('xpath&&%s' % Element.CloseGroupWin)
        elif cancel == 'cancel':
            self.ShowWaitVisibility('xpath&&%s' % Element.CancelGroupWin)
            self.GetElementClick('xpath&&%s' % Element.CancelGroupWin)
        else:
            raise

    def DefGroupName(self,name):
        """
        1、新建分组名称输入框输入内容
        2、分组重命名输入框
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.GroupName)
        self.GetElementSendKeys('css&&%s' % Element.GroupName,name)

    def DetermineAddGroup(self):
        """
        新建分组确定按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.DetermineDelete)
        self.GetElementClick('xpath&&%s' % Element.DetermineDelete)

    def ClickChoice(self):
        """
        点击背包素材右上角的多选按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.OneGroupOneRole)
        OneDriver = self.GetElement('xpath&&%s' % Element.OneGroupOneRole)
        TwoDriver = self.GetElement('xpath&&%s' % Element.OneGroupChoice)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()

    def MoveToGroup(self):
        """
        点击移动到分组
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.MoveToGroup)
        self.GetElementClick('xpath&&%s' % Element.MoveToGroup)

    def CloseMoveGroupWin(self):
        """
        点击关闭移动分组窗口按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.CloseMoveGroupWin)
        self.GetElementClick('xpath&&%s' % Element.CloseMoveGroupWin)

    def DetermineMoveGroup(self):
        """
        点击移动分组页面的确定按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.DetermineMoveGroup)
        self.GetElementClick('xpath&&%s' % Element.DetermineMoveGroup)

    def NewGroupName(self,NewGroupName):
        """
        移动分组页面中输入新建分组名称
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.NewGroupName)
        self.GetElementSendKeys('css&&%s' % Element.NewGroupName,NewGroupName)

    def Rename(self):
        """
        点击素材重命名
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Rename)
        self.GetElementClick('xpath&&%s' % Element.Rename)

    def CloseRenamePage(self,cancel):
        """
        关闭分组重命名页面
        cancel传参
            传x：点击右上角关闭按钮
            传cancel：点击取消按钮
        :return:
        """
        if cancel == 'x':
            self.ShowWaitVisibility('xpath&&%s' % Element.CloseRenameWin)
            self.GetElementClick('xpath&&%s' % Element.CloseRenameWin)
        elif cancel == 'cancel':
            self.ShowWaitVisibility('xpath&&%s' % Element.CancelRenameWin)
            self.GetElementClick('xpath&&%s' % Element.CancelRenameWin)
        else:
            raise

    def DetermineName(self):
        """
        重命名窗口点击确定
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.DetermineName)
        self.GetElementClick('xpath&&%s' % Element.DetermineName)


    def RenameInput(self,Renames):
        # Renames
        """
        重命名窗口修改名称
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.RenameInputElement)
        RenameInputElement = self.GetElement('xpath&&%s' % Element.RenameInputElement)
        # 需要开发后期加个ID
        self.driver.execute_script("document.getElementsByClassName('edit-group-name--3bMpf')[0].value = '';", RenameInputElement)
        RenameInputElement.send_keys(Renames)


    def DeleteChoice(self):
        """
        点击删除角色按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.DeleteChoice)
        self.GetElementClick('xpath&&%s' % Element.DeleteChoice)

    def DeleteCancel(self,cancel):
        """
        关闭删除窗口：
            传x：点击右上角关闭按钮
            传cancel：点击取消按钮
        :return:
        """
        if cancel == 'x':
            self.ShowWaitVisibility('xpath&&%s' % Element.CloseDeleteWin)
            self.GetElementClick('xpath&&%s' % Element.CloseDeleteWin)
        elif cancel == 'cancel':
            self.ShowWaitVisibility('xpath&&%s' % Element.CancelDeleteWin)
            self.GetElementClick('xpath&&%s' % Element.CancelDeleteWin)
        else:
            raise

    def DetermineDelete(self):
        """
        删除页面点击确定
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.DetermineDelete)
        self.GetElementClick('xpath&&%s' % Element.DetermineDelete)

    def ClickTwoGroupChoice(self):
        """
        点击第二个分组的选择按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.TwoGroup)
        OneDriver = self.GetElement('xpath&&%s' % Element.TwoGroup)
        TwoDriver = self.GetElement('xpath&&%s' % Element.TwoGroupChoice)
        ActionChains(self.driver).move_to_element(OneDriver).click(TwoDriver).perform()

    def ClickGroupRename(self):
        """
        分组重命名点击
        ps：分组重命名输入框是：DefGroupName方法
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.ClickRename)
        self.GetElementClick('xpath&&%s' % Element.ClickRename)

    def CancelRename(self,cancel):
        """
        关闭分组重命名窗口：
            传x：点击右上角关闭按钮
            传cancel：点击取消按钮
        :return:
        """
        if cancel == 'x':
            self.ShowWaitVisibility('xpath&&%s' % Element.CloseGroupRenameWin)
            self.GetElementClick('xpath&&%s' % Element.CloseGroupRenameWin)
        elif cancel == 'cancel':
            self.ShowWaitVisibility('xpath&&%s' % Element.CancelDeleteWin)
            self.GetElementClick('xpath&&%s' % Element.CancelDeleteWin)
        else:
            raise

    def DetermineRename(self):
        """
        重命名窗口点击确定
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.DetermineDelete)
        self.GetElementClick('xpath&&%s' % Element.DetermineDelete)

    def ClickDelete(self):
        """
        分组点击删除按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Delete)
        self.GetElementClick('xpath&&%s' % Element.Delete)

    def CancelDeleteGroup(self,cancel):
        """
        关闭分组删除窗口：
            传x：点击右上角关闭按钮
            传cancel：点击取消按钮
        :return:
        :return:
        """
        if cancel == 'x':
            self.ShowWaitVisibility('xpath&&%s' % Element.CloseGroupDeleteWin)
            self.GetElementClick('xpath&&%s' % Element.CloseGroupDeleteWin)
        elif cancel == 'cancel':
            self.ShowWaitVisibility('xpath&&%s' % Element.Cancel)
            self.GetElementClick('xpath&&%s' % Element.Cancel)
        else:
            raise

    def DetermineDeleteGroup(self):
        """
        点击【删除分组窗口】-->【确定】按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.Determine)
        self.GetElementClick('xpath&&%s' % Element.Determine)

