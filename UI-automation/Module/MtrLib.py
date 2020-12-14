import win32api
import win32con

from lib.Public import Public
from lib import Element, path
from selenium.webdriver.common.action_chains import ActionChains  # 拓展其他的行为
from time import sleep

BG = '//div[contains(text(), "背景")]'
BG1 = '//li[contains(text(), "全部")]'
BG2 = '//li[contains(text(), "游戏")]'
BG3 = '//li[contains(text(), "生活")]'
BG4 = '//li[contains(text(), "自然")]'

AG = '//*[@id="material-sidebar-wrapper"]/div[1]/div[2]/div[3]/div'
AG1 = '//li[contains(text(), "全部")]'
AG2 = '//li[contains(text(), "音效")]'
AG3 = '//li[contains(text(), "音乐")]'

# 分组
fenzu = 'div.add-folder-icon--3_Hw2'
fenzutext = 'input[placeholder="给你的分组取个名字吧"]'
fenzubutton = '//div[contains(text(), "确定")]'
# 重命名
# 鼠标悬停在test上
rename0 = '//div[contains(text(),"test")]'

rename1 = '//*[@id="options-2140326"]'  # ...

'''
//*[@id="material-group-list"]
//*[@id="options-2140326"]
//*[@id="group-options"]/div[1]
'''

rename2 = '//div[contains(text(), "重命名")]'
rename3 = '//div[contains(text(), "删除")]'

rename4 = '//div[contains(text(), "保留")]'
su='//*[@id="material-dialog"]/div[5]/div/div/div[2]/div/div[3]/div[1]/div'
# 素材移动到分组

move001 = '//*[@id="2128221"]/div[1]/div[2]'  # //*[@id="2128221"]/div[1]  //*[@id="2128517"]/div[1] //*[@id="iconuploaded"]
move002 = '//*[@id="material-items-wrap"]/div[2]/div[3]/div[2]'  # ...  //*[@id="material-items-wrap"]/div[2]/div[3]/div[2]
move003 = '//div[contains(text(), "移动到分组")]'

move004 = '//*[@id="material-dialog"]/div[5]/div/div/div[2]/div/div[3]/div[1]/ul/li[2]/div[2]'
move005 = '//*[@id="material-dialog"]/div[5]/div/div/div[2]/div/div[3]/div[2]/div'
move006 = '//div[contains(text(), "删除")]'

# 点击test分组
test_fenzu = '//div[contains(text(), "test999")]'

# 本地上传按钮
button1 = '//div[contains(text(),"本地上传")]/preceding-sibling::form[1]/input'  #//*[@id="material-items-wrap"]/div/div[1]/form/input
# 确认添加按钮
button2 = '//*[@id="material-dialog"]/div[4]/div/div[2]/div[1]/div/div'  # //*[@id="material-dialog"]/div[4]/div/div[2]/div[1]/div/div
# 清空按钮
button3 = '//*[@id="material-dialog"]/div[4]/div/div[2]/div[2]/div/div'
# 选择分组中的角色
role = '//*[@id="material-dialog"]/div[3]/div/div[1]/span[3]' #//*[@id="material-dialog"]/div[3]/div/div[1]/span[3]
# 选择分组中的背景
background = '//*[@id="material-dialog"]/div[3]/div/div[1]/span[4]'
# 选择分组中的声音
music = '//*[@id="material-dialog"]/div[3]/div/div[1]/span[5]'

#上传按钮
shangchuan = '//*[@id="material-dialog"]/div[5]/div/div/div[2]/div/div[2]/div[7]/div/div' #//*[@id="material-dialog"]/div[5]/div/div/div[2]/div/div[2]/div[7]/div/div
shangchuan1='//*[@id="material-dialog"]/div[5]/div/div/div[2]/div/div[2]/div[6]/div/div'                                                                                        #//*[@id="material-dialog"]/div[5]/div/div/div[2]/div/div[2]/div[6]/div/div
clear='//div[contains(text(), "清空")]'
# 素材商店
materialstore = '//*[@id="material-dialog"]/div[1]/div[2]/div[1]/div[2]'
#我的素材
mysucai='//*[@id="material-dialog"]/div[1]/div[2]/div[1]/div[1]'


# 最新上架
newshangjia = '//*[@id="material-dialog"]/div[3]/div/div[1]/span[2]'
# 最多使用
moreshiyong = '//*[@id="material-dialog"]/div[3]/div/div[1]/span[3]'
# 仅显示未采集
weicaiji = '//*[@id="material-dialog"]/div[3]/div/div[1]/span[4]'

# 购买角色三头龙
buysantoulong = '//*[@id="material-dialog"]/div[3]/div/div[2]/div[1]/div[2]/div[2]'
# 采下来
caixilai = '//*[@id="material-dialog"]/div[5]/div/div/div[2]/div/div[2]/div[6]/div/div'
# 金币显示
cornnumber = '//*[@id="material-dialog"]/div[1]/div[1]/div[2]/span[1]'
# 搜索素材的输入框
shucaiinput = '//*[@id="material-dialog"]/div[1]/div[2]/div[2]/div/input'

#关闭素材库
guanbi='//*[@id="material-dialog"]/div[1]/div[3]/div'



class MtrLib(Public):

    def AddRole(self):
        """
        点击添加角色按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.AddRole)
        self.GetElementClick('css&&%s' % Element.AddRole)

    def MLAdd(self):
        """
        点击添加角色按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.MLAdd)
        self.GetElementClick('css&&%s' % Element.MLAdd)

    def ClickOR(self):
        """
        点击展开造型按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.OpenRole)
        self.GetElementClick('xpath&&%s' % Element.OpenRole)

    def ClickRS(self):
        """
        点击造型选择按钮
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.RoleSLC)
        self.GetElementClick('xpath&&%s' % Element.RoleSLC)

    def ClickSSlc(self):
        """
        点击造型选择按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.SSlc)
        self.GetElementClick('css&&%s' % Element.SSlc)

    def Audio(self):
        """
        点击声音积木盒
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Audio)
        self.GetElementClick('css&&%s' % Element.Audio)

    def Audios(self):
        """
        点击声音积木盒中的添加声音按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.Audios)
        self.GetElementClick('css&&%s' % Element.Audios)

    def AudioSc(self):
        """
        点击声音积木盒中的添加声音按钮
        :return:
        """
        self.ShowWaitVisibility('css&&%s' % Element.AudioSc)
        self.GetElementClick('css&&%s' % Element.AudioSc)

    def ClickSR(self):
        """
        点击素材库中角色
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % Element.RoleS)
        self.GetElementClick('xpath&&%s' % Element.RoleS)

    def ClickSRS(self, select):
        """
        点击素材库中角色的分类
        select:1  ----   全部
        select:2  ----   形象
        select:3  ----   界面
        select:4  ----   道具
        select:5  ----   特效
        :return:
        """
        if select == 1:
            self.ShowWaitVisibility('xpath&&%s' % Element.RoleS1)
            self.GetElementClick('xpath&&%s' % Element.RoleS1)
        elif select == 2:
            self.ShowWaitVisibility('xpath&&%s' % Element.RoleS2)
            self.GetElementClick('xpath&&%s' % Element.RoleS2)
        elif select == 3:
            self.ShowWaitVisibility('xpath&&%s' % Element.RoleS3)
            self.GetElementClick('xpath&&%s' % Element.RoleS3)
        elif select == 4:
            self.ShowWaitVisibility('xpath&&%s' % Element.RoleS4)
            self.GetElementClick('xpath&&%s' % Element.RoleS4)
        elif select == 5:
            self.ShowWaitVisibility('xpath&&%s' % Element.RoleS5)
            self.GetElementClick('xpath&&%s' % Element.RoleS5)
        else:
            raise BaseException()

    def ClickBG(self):
        """
        点击素材库中背景
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % BG)
        self.GetElementClick('xpath&&%s' % BG)

    def ClickSBG(self, select):
        """
        点击素材库中角色的分类
        select:1  ----   全部
        select:2  ----   游戏
        select:3  ----   生活
        select:4  ----   自然
        :return:
        """
        if select == 1:
            self.ShowWaitVisibility('xpath&&%s' % BG1)
            self.GetElementClick('xpath&&%s' % BG1)
        elif select == 2:
            self.ShowWaitVisibility('xpath&&%s' % BG2)
            self.GetElementClick('xpath&&%s' % BG2)
        elif select == 3:
            self.ShowWaitVisibility('xpath&&%s' % BG3)
            self.GetElementClick('xpath&&%s' % BG1)
        elif select == 4:
            self.ShowWaitVisibility('xpath&&%s' % BG4)
            self.GetElementClick('xpath&&%s' % BG4)
        else:
            raise BaseException()

    def ClickAG(self):
        """
        点击素材库中音乐
        :return:
        """
        self.ShowWaitVisibility('xpath&&%s' % AG)
        self.GetElementClick('xpath&&%s' % AG)

    def ClickSAG(self, select):
        """
        点击素材库中角色的分类
        select:1  ----   全部
        select:2  ----   音效
        select:3  ----   音乐
        :return:
        """
        if select == 1:
            self.ShowWaitVisibility('xpath&&%s' % AG1)
            self.GetElementClick('xpath&&%s' % AG1)
        elif select == 2:
            self.ShowWaitVisibility('xpath&&%s' % AG2)
            self.GetElementClick('xpath&&%s' % AG2)
        elif select == 3:
            self.ShowWaitVisibility('xpath&&%s' % AG3)
            self.GetElementClick('xpath&&%s' % AG3)
        else:
            raise BaseException()

    # ------------------------------------------------------续写素材库的测试步骤-------------------------------------------------
    def cerateFenZu(self):
        self.ShowWaitVisibility('css&&%s' % fenzu)
        self.GetElementClick('css&&%s' % fenzu)

    def shurufenzuname(self, name):
        self.ShowWaitVisibility('css&&%s' % fenzutext)
        self.GetElement('css&&%s' % fenzutext).clear()
        self.GetElementSendKeys('css&&%s' % fenzutext, name)

    def quedingfenzu(self):
        self.ShowWaitVisibility('xpath&&%s' % fenzubutton)
        self.GetElementClick('xpath&&%s' % fenzubutton)

    def rename0(self, driver):
        self.ShowWaitVisibility('xpath&&%s' % rename0)
        ActionChains(driver).move_to_element(self.GetElement('xpath&&%s' % rename0)).perform()
        ActionChains(driver).context_click(self.GetElement('xpath&&%s' % rename0)).perform()

    # 点击分组
    # //*[@id="material-items-wrap"]/div[2]/div[1]
    def rename000(self, driver):
        self.ShowWaitVisibility('xpath&&%s' % rename0)
        self.GetElementClick('xpath&&%s' % rename0)
        ActionChains(driver).context_click(
            self.GetElement('xpath&&%s' % '//*[@id="material-items-wrap"]/div[2]/div[1]')).perform()

    def rename00(self):
        self.ShowWaitVisibility('xpath&&%s' % rename0)
        self.GetElementClick('xpath&&%s' % rename0)

    def rename001(self):
        self.ShowWaitVisibility('id&&%s' % rename1)
        self.GetElementClick('id&&%s' % rename1)

    def rename002(self):
        self.ShowWaitVisibility('xpath&&%s' % rename2)
        self.GetElementClick('xpath&&%s' % rename2)

    def rename004(self):
        self.ShowWaitVisibility('xpath&&%s' % rename4)
        self.GetElementClick('xpath&&%s' % rename4)

    def delete001(self):
        self.ShowWaitVisibility('xpath&&%s' % rename3)
        self.GetElementClick('xpath&&%s' % rename3)

    # 素材移动到分组
    def move001(self):
        self.ShowWaitVisibility('xpath&&%s' % move001)
        self.GetElementClick('xpath&&%s' % move001)

    def move002(self):
        self.ShowWaitVisibility('xpath&&%s' % move002)
        self.GetElementClick('xpath&&%s' % move002)

    #     点击移动到分组
    def move003(self):
        self.ShowWaitVisibility('xpath&&%s' % move003)
        self.GetElementClick('xpath&&%s' % move003)

    # 选择另一个分组
    def move004(self):
        self.ShowWaitVisibility('xpath&&%s' % move004)
        self.GetElementClick('xpath&&%s' % move004)

    # 点击确定
    def move005(self):
        self.ShowWaitVisibility('xpath&&%s' % move005)
        self.GetElementClick('xpath&&%s' % move005)

    # 删除
    def move006(self):
        self.ShowWaitVisibility('xpath&&%s' % move006)
        self.GetElementClick('xpath&&%s' % move006)

    # 选中test分组
    def chancefenzu(self):
        self.ShowWaitVisibility('xpath&&%s' % test_fenzu)
        self.GetElementClick('xpath&&%s' % test_fenzu)

    # 点击本地上传按钮
    def shangchaun001(self):
        self.ShowWaitVisibility('xpath&&%s' % button1)
        #self.GetElementClick('xpath&&%s' % button1)

    # 选择角色
    def role(self):
        self.ShowWaitVisibility('xpath&&%s' % role)
        self.GetElementClick('xpath&&%s' % role)

    # 上传角色
    def shangchuan002(self):
        sleep(1)
        win32api.keybd_event(17, 0, 0, 0)
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(1)
        win32api.keybd_event(13, 0, 0, 0)  # (回车)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        sleep(1)
        self.ShowWaitVisibility('xpath&&%s' % shangchuan)
        self.GetElementClick('xpath&&%s' % shangchuan)
    #点击清空
    #上传声音
    def shangchuanmusic(self):
        sleep(1)
        win32api.keybd_event(17, 0, 0, 0)
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(1)
        win32api.keybd_event(13, 0, 0, 0)  # (回车)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        sleep(1)
        self.ShowWaitVisibility('xpath&&%s' % shangchuan1)
        self.GetElementClick('xpath&&%s' % shangchuan1)

    def clear_button(self):
        self.ShowWaitVisibility('xpath&&%s' % clear)
        self.GetElementClick('xpath&&%s' % clear)



    # 选择背景
    def background(self):
        self.ShowWaitVisibility('xpath&&%s' % background)
        self.GetElementClick('xpath&&%s' % background)

    # 上传背景
    def shangchuan003(self):
        self.GetElementSendKeys('xpath&&%s' % button1, path.background)

    # 选择声音
    def music(self):
        self.ShowWaitVisibility('xpath&&%s' % music)
        self.GetElementClick('xpath&&%s' % music)

    # 上传声音
    def shangchuan004(self):
        self.GetElementSendKeys('xpath&&%s' % button1, path.music)

    # 点击清空
    def shangchaunclear(self):
        self.ShowWaitVisibility('xpath&&%s' % button3)
        self.GetElementClick('xpath&&%s' % button3)

    # 点击素材商店
    def materialstoreClick(self):
        self.ShowWaitVisibility('xpath&&%s' % materialstore)
        self.GetElementClick('xpath&&%s' % materialstore)

    # 点击最新上架
    def newnewshangjiaClick(self):
        self.ShowWaitVisibility('xpath&&%s' % newshangjia)
        self.GetElementClick('xpath&&%s' % newshangjia)

    # 点击最多使用
    def moreshiyongClick(self):
        self.ShowWaitVisibility('xpath&&%s' % moreshiyong)
        self.GetElementClick('xpath&&%s' % moreshiyong)

    # 点击仅显示未采集
    def weicaijiClick(self):
        self.ShowWaitVisibility('xpath&&%s' % weicaiji)
        self.GetElementClick('xpath&&%s' % weicaiji)

    # 点击角色三头龙
    def buysantoulongClick(self):
        self.ShowWaitVisibility('xpath&&%s' % buysantoulong)
        self.GetElementClick('xpath&&%s' % buysantoulong)

    # 采下来
    def caixilaiClick(self):
        self.ShowWaitVisibility('xpath&&%s' % caixilai)
        self.GetElementClick('xpath&&%s' % caixilai)

    # 点击确认添加
    def querentianjia(self):
        self.ShowWaitVisibility('xpath&&%s' % button2)
        self.GetElementClick('xpath&&%s' % button2)

    # 得到金币数量
    def showcornNumber(self):
        self.ShowWaitVisibility('xpath&&%s' % cornnumber)
        number = self.GetElement('xpath&&%s' % cornnumber).get_attribute('innerHTML')
        return int(number)

    # 关键词搜索素材
    def shucaiinputSend(self, sucai):
        th = self.ShowWaitVisibility('xpath&&%s' % shucaiinput)
        self.GetElementSendKeys('xpath&&%s' % shucaiinput, sucai)
        return th

    def my_sucai(self):
        self.ShowWaitVisibility('xpath&&%s' % mysucai)
        self.GetElementClick('xpath&&%s' % mysucai)


    def su(self):
        self.ShowWaitVisibility('xpath&&%s' % su)
        self.GetElementClick('xpath&&%s' % su)