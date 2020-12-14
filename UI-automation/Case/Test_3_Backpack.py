from Module import Backpack
from selenium import webdriver
from lib import TestData,Public,Element



class TestJumpShequ():

    @classmethod
    def setup_class(cls):
        # cls.driver = webdriver.Chrome(executable_path=DriverDir)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.BP = Backpack.BackPack(cls.driver)


    def test_NewGroup(self):
        """
        查看是否能在背包创建新的分组
        :return:
        """
        self.Public.CloseGP()
        self.Public.SuccessLogin()
        self.BP.ClickBackPack()
        self.BP.AddGroup()
        self.BP.DefGroupName(TestData.GroupName)
        self.BP.DetermineAddGroup()
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.CGS)
        assert Result != False

    def test_GroupRN(self):
        """
        查看分组是否能重命名
        :return:
        """
        self.BP.ClickTwoGroupChoice()
        self.BP.ClickGroupRename()
        self.BP.DefGroupName('TestRN')
        self.BP.DetermineRename()
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.RNS)
        assert Result != False

    def test_MoveM(self):
        """
        查看是否能将素材移动到别的分组
        :return:
        """
        self.BP.ClickChoice()
        self.BP.MoveToGroup()
        self.BP.DetermineMoveGroup()
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.MoveS)
        assert Result != False

    def test_DeleteGp(self):
        """
        查看分组是否能被删除
        :return:
        """
        self.BP.ClickTwoGroupChoice()
        self.BP.ClickDelete()
        self.BP.DetermineDeleteGroup()
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.DeleteS)
        assert Result != False

    def test_MoveRN(self):
        """
        素材重命名
        :return:
        """
        self.BP.ClickChoice()
        self.BP.Rename()
        self.BP.RenameInput(TestData.GroupName)
        self.BP.DetermineName()
        Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.RNS)
        assert Result != False

    def test_DLTMove(self):
        """
        删除素材
        :return:
        """
        Oname = self.Public.GetElement('xpath&&%s' % Element.OneGroupOneRole).text
        print(Oname)
        self.BP.ClickChoice()
        self.BP.DeleteChoice()
        self.BP.DetermineDelete()
        Tname = self.Public.GetElement('xpath&&%s' % Element.OneGroupOneRole).text
        print(Tname)
        assert Oname != Tname
        self.driver.quit()
