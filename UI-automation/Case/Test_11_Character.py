import sys
sys.path.append('..')
from lib import Element,TestData,Public,path
from Module import Character
from Module import Backpack
from selenium import webdriver
import allure


@allure.feature("角色模块")
class TestCharacter():
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(TestData.Productions)
        cls.Public = Public.Public(cls.driver)
        cls.character = Character.Character(cls.driver)
        cls.Backpack = Backpack.BackPack(cls.driver)

    @allure.title('素材库添加角色')
    def test_library_add_character(self):
        """
        素材库添加角色
        :return:
        """
        try:
            with allure.step('关闭新手引导'):
                self.Public.CloseGP()
            with allure.step('素材库添加角色'):
                self.character.library_add_character()
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.Lib_add)
            assert Result != False

        except BaseException as e:
            raise BaseException(e, '用例[素材库添加角色]执行失败')

    @allure.title('画板添加角色')
    def test_drawingboard_add_character(self):
        """
        画板添加角色
        :return:
        """
        try:
            with allure.step('画板添加角色'):
                self.character.drawingboard_add_character()
            Result = self.Public.ShowWaitVisibility('xpath&&%s' % Element.Draw_add)
            assert Result != False
        except BaseException as e:
            raise  BaseException(e,'用例[画板添加角色]执行失败')

    @allure.title('随机添加角色')
    def test_random_add_character(self):
        """
        随机添加角色
        :return:
        """
        try:
            with allure.step('随机添加角色'):
                self.character.random_add_character()
            Result = self.Public.ShowWaitVisibility('css&&%s' % Element.chara_selected)
            assert Result != False
        except BaseException as e:
            raise  BaseException(e,'用例[随机添加角色]执行失败')

    @allure.title('本地上传角色')
    def test_upload_add_character(self):
        """
        本地上传角色
        :return:
        """
        try:
            with allure.step('本地上传角色'):
                self.character.upload_add_character(path.filepath)
            Result = self.Public.ShowWaitVisibility('css&&%s' % Element.up_add)
            assert Result != False
        except BaseException as e:
            raise BaseException(e, '用例[本地上传角色]执行失败')

    @allure.title('角色下无积木删除角色')
    def test_del_character1(self):
        """
        删除角色,角色下无积木直接删除
        :return:
        """
        try:
            with allure.step('角色下无积木删除角色'):
                self.character.del_character1()
            Result = self.Public.ShowWaitV_until_not('css&&%s' %Element.del_chara1)
            assert Result != False
        except BaseException as e:
            raise BaseException(e, '用例[角色下无积木删除角色]执行失败')

    @allure.title('角色下有积木删除角色')
    def test_del_character2(self):
        """
        删除角色，角色下有积木，弹出二次确认框点击确认后删除
        :return:
        """
        try:
            with allure.step('角色下有积木删除角色'):
                self.character.del_character2()
            Result = self.Public.ShowWaitV_until_not('xpath&&%s' % Element.del_chara2)
            assert Result != False
        except BaseException as e:
            raise BaseException(e, '用例[角色下有积木删除角色]执行失败')

    @allure.title('右键复制角色')
    def test_copy_chara(self):
        """
        右键复制角色
        :return:
        """
        try:
            with allure.step('右键复制角色'):
                self.character.copy_chara()
            Result = self.Public.ShowWaitVisibility('css&&%s' % Element.copy_chara)
            assert Result != False
        except BaseException as e:
            raise BaseException(e, '用例[右键复制角色]执行失败')

    @allure.title('右键修改角色名称')
    def test_rc_rename(self):
        """
        右键改名
        :return:
        """
        try:
            with allure.step('角色上右键'):
                self.character.rc_rename()
            with allure.step('单击改名'):
                self.character.rename_chara(TestData.CRN)
            with allure.step('获取修改后的名称'):
                Name = self.Public.GetElement('xpath&&%s' % Element.input_text).get_attribute('value')
            assert Name == TestData.CRN
        except BaseException as e:
            raise BaseException(e, '用例[右键修改角色名称]执行失败')

    @allure.title('单击修改角色名称')
    def test_rename(self):
        """
        单击改名
        :return:
        """
        try:
            with allure.step('单击改名'):
                self.character.ClinkChara()
            with allure.step('获取修改后的名称'):
                Name = self.Public.GetElement('xpath&&%s' % Element.input_text).get_attribute('value')
            assert Name == TestData.CRN1
        except BaseException as e:
            raise BaseException(e, '用例[单击修改角色名称]执行失败')

    @allure.title('右键导出角色')
    def test_rc_export(self):
        """
        右键导出角色
        :return:
        """
        try:
            with allure.step('右键导出角色'):
                self.character.rc_export()
        except BaseException as e:
            raise BaseException(e, '用例[右键导出角色]执行失败')

    @allure.title('右键添加角色至背包')
    def test_rc_backpack(self):
        """
        右键添加角色至背包
        :return:
        """
        try:
            with allure.step('检查登录态'):
                self.Public.SuccessLogin()
            with allure.step('右键添加角色至背包'):
                self.character.rc_backpack()
            with allure.step('打开背包，检查角色添加成功'):
                self.Backpack.ClickBackPack()
            Name = self.Public.GetElement('xpath&&%s' % Element.OneGroupOneRole).text
            assert Name == TestData.CRN1
            with allure.step('关闭背包弹窗'):
                self.Backpack.CloseBackPack()
        except BaseException as e:
            raise BaseException(e, '用例[右键添加角色至背包]执行失败')

    @allure.title('右键创建分组')
    def test_rc_group(self):
        """
        右键创建分组
        :return:
        """
        try:
            with allure.step('右键创建分组'):
                self.character.rc_group()
            Result = self.Public.ShowWaitVisibility('css&&%s' % Element.group)
            assert Result != False
        except BaseException as e:
            raise BaseException(e, '用例[右键创建分组]执行失败')

    @allure.title('右键复制分组')
    def test_rc_Gcopy(self):
        """
        右键复制分组
        :return:
        """
        try:
            with allure.step('右键复制分组'):
                self.character.rc_G_copy()
            Result = self.Public.ShowWaitVisibility('css&&%s' % Element.group1)
            assert Result != False
        except BaseException as e:
            raise BaseException(e, '用例[右键复制分组]执行失败')

    @classmethod
    def teardown_class(cls):
        """
        退出网页
        :return:
        """
        cls.driver.quit()


if __name__ == '__main__':
    pass
