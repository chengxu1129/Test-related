"""
临时页面
"""
# 关闭介绍页面
# 关闭按钮：xpath
head_close = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[1]'
# 跳转页面按钮：xpath
head_jump = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]'
# 社区跳转:css
shequ_jump = 'div[data-report-click="进入官网"]'

# 关闭新手引导
CloseGuide = 'div[data-report-click="新手引导-弹窗-关闭"]'
# 新手引导立即创作
CreateNow = 'div[data-report-click="新手引导-弹窗-立即创作"]'
# 新手引导指引窗口
OK = 'div[style="border-radius: 16px;"]'



"""
公共元素
"""
# 取消按钮
Cancel = '//div[contains(text(), "取消")]'
# 确定按钮
Determine = '//div[contains(text(), "确定")]'




"""
登录页面
"""
# 账号密码登录
# 页面右上角登录按钮：css
login_button = 'div[data-report-click="用户信息-登录"]'
# 密码登录-手机/邮箱/用户名  输入框：css
user_input = 'input[maxlength="100"][style="padding-right: 28px; padding-left: 8px; font-size: 16px;"]'
# 密码登录-密码  输入框：css
password_input = 'input[maxlength="20"][style="padding-right: 28px; padding-left: 8px; font-size: 16px; font-family: initial;"]'
# 账号密码登录按钮：css
pass_button = 'div[data-report-click="用户信息-密码登录"]'
# 账号或密码错误提示：xpath
UserErrorInfo = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/form/div[5]'
# -----
# 短信登录
# 短信登录切换入口：xpath
phone_entrance = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]'
# 手机号码输入框：css
phone_input = 'input[maxlength="11"][style="padding-right: 28px; padding-left: 8px; font-size: 16px;"]'
# 验证码输入框：css
captcha_input = 'input[maxlength="10"][style="padding-right: 8px; padding-left: 8px; font-size: 16px;"]'
# 获取验证码：css
get_captcha = 'span[data-report-click="用户信息-登录验证码"]'
# 短信登录按钮:css
phone_login_button = 'div[data-report-click="用户信息-短信登录"]'
# 手机格式不正确提示:xpath
phone_error = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/form/div[2]/span'
# 获取验证码倒计时:css
countdown = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/form/div[3]/span/text()[2]'
# 登录成功后，点击头像：xpath
user_info = '//*[@id="kitten_header"]/div[3]/div[4]/div/div[1]/div'
# 查看个人作品：css
user_bcm = 'div[data-report-click="用户信息-我的作品"]'
# 账号设置按钮
user_set = 'div[data-report-click="用户信息-账号设置"]'
# 退出登录按钮：css
quit_login = 'div[data-report-click="用户信息-退出登录"]'
# 跳转账号注册页面按钮：xpath
register = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/span[2]/span'

"""
保存和发布
"""
# 保存按钮
Save = 'div[data-report-click="保存"]'
SaveS = '//div[contains(text(), "作品保存成功")]'
# 作品名称输入框
FileName = 'input[placeholder="作品名称不能为空"]'
# 发布按钮
Release = 'div[data-report-click="发布-入口"]'
# 发布页重命名
ReleaseName = 'input[style="padding-right: 8px; padding-left: 8px; border: 2px solid transparent;"]'
# ReleaseName = 'input[maxlength="20"][padding-right: 8px; padding-left: 8px; border: 2px solid transparent;]'
# 不允许购买作品
NoPurchase = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div[2]/label[2]/i'
# 可以购买
Purchase = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div[2]/label[1]/i'
# 作品介绍
FileIntroduce = 'textarea[placeholder="向大家介绍你的作品，如果你的作品是基于他人作品的再创作，或者从他人作品中得到灵感，别忘记感谢原作者哦～"]'
# 操作指南
OperationGuide = 'textarea[placeholder="给你的作品写一个体验指南，并教大家如何操作吧~"]'
# 确认发布
DetermineRelease = 'div[data-report-click="发布-确认发布"]'





"""
文件功能
"""
# 文件按钮：css
file_button = 'svg[style="font-size: 26px;"]'
# 新建文件按钮：css
new_bcm = 'div[data-report-click="文件-新建"]'
# 打开文件按钮：css
open_file_button = 'div[data-report-click="文件-打开"]'
# 关闭文件页面
CloseFilePage = 'div[style="top: 21px; right: 15px;"]'
# 历史版本查看按钮：css
history_file_button = 'div[data-report-click="文件-历史版本"]'
# 另存为：css
als_save_button = 'div[data-report-click="文件-另存为"]'
# 打开电脑文件：css
open_win_file_button = 'div[data-report-click="文件-打开电脑文件"]'
# 作品保存到电脑
file_save_win_button = 'div[data-report-click="文件-保存到电脑"]'
# 新建完成后断言元素：css
disappear = 'input[value="编程猫划船"]'
# 查看版本:css
check_version = 'div[tabindex="-1"][style="width: 98px; height: 28px;"]'
# 查看所有版本作品
all_version = '//*[@id="root"]/div/div[2]/div[6]/div/div/div[1]/div'
# 查看4.0版本作品
four_version = '//*[@id="root"]/div/div[2]/div[6]/div/div/div[2]/div'
# 查看3.0版本作品
three_version = '//*[@id="root"]/div/div[2]/div[6]/div/div/div[3]/div'
# 全部作品按钮：css
all_bcm = 'span[data-report-click="作品弹窗-全部"]'
# 作品已发布：css
release_yes = 'span[data-report-click="作品弹窗-已发布"]'
# 已发布中第一个作品的名字
RName = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[1]'
# 作品未发布：css
release_no = 'span[data-report-click="作品弹窗-未发布"]'
# 作品搜索框
search_for_bcm = ('css&&%s' % 'input[data-report-click="作品弹窗-搜索作品"]')
# 作品中的第一个bcm：css
one_bcm = 'img[alt="project_img"]'
# 获取第一个bcm的名称：css
bcm_name = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[1]'
# 保持弹窗：不保存（css）
not_save = 'div[data-report-click="保存确认-不保存"]'
# 取消保存：css
cancel = 'div[data-report-click="保存确认-取消"]'
# 作品搜索框：css
grep_bcm = 'input[data-report-click="作品弹窗-搜索作品"]'
# 打开本地作品按钮：css
local_file = 'svg[aria-hidden="true"][style="font-size: 55px;"]'
# 历史版本的时间
HistoryTime = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[3]/div[1]/div[2]'
# 查看历史按钮
CheckHistory = 'div[data-report-click="文件-查看历史版本"]'
# 关闭历史版本页面
CloseHVPage = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[2]'
# 新建页：全部作品
All = '//div[contains(text(), "全部")]'
# 新建页：游戏类模板
Game = '//div[contains(text(), "游戏类模板")]'
# 新建页：工具类模板
Tools = '//div[contains(text(), "工具类模板")]'
# 新建空白作品按钮
CreatNB = 'div[data-report-click="作品弹窗-空白作品"]'






"""
背包
"""
# 背包入口:css
BackPack = 'div[data-report-click="背包-入口"]'
# 关闭背包素材：xpath
CloseBackPack = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div'
# 添加分组按钮
AddGroup = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/div'
# 关闭创建分组窗口按钮
CloseGroupWin = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[2]/div/svg'
# 取消创建分组窗口按钮
CancelGroupWin = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div[1]'
# 确定创建新分组按钮
DetermineAddGroup = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div[2]'
# 新建分组成功
CGS = '//div[contains(text(), "新建分组成功")]'
# 新建分组窗口输入框输入名称：css
GroupName ='input[placeholder="给你的分组取个名字吧"]'
# 第一个分组
OneGroup = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span[2]'
# 第一个分组第一个角色名称
OneGroupOneRole = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[3]'
# 第一个分组第一个角色的选择按钮
OneGroupChoice = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div[1]'
# 第一个角色-->移动到分组
MoveToGroup = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div[1]'
# 关闭移动分组窗口按钮
CloseMoveGroupWin = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div/div[5]'
# 移动分组窗口的输入框：css
NewGroupName = 'input[placeholder="输入文字，按回车创建分组"]'
# 移动分组确定按钮
DetermineMoveGroup = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div/div[4]'
# 成功移动到我的背包
MoveS = '//div[contains(text(), "成功移动到我的背包")]'
# 第一个角色-->重命名
Rename = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div[2]'
# 重命名窗口关闭
CloseRenameWin = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[2]/div/svg'
# 重命名窗口取消
CancelRenameWin = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div[1]'
# 重命名页面确定按钮
DetermineName = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[1]/div[2]/div[2]'
# 重命名输入框
RenameInputElement = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[1]/input'
# 第一个角色-->删除
DeleteChoice = '//div[contains(text(), "删除")]'
# 删除页面关闭按钮
CloseDeleteWin = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[2]/div/svg/use'

# 删除页面取消按钮
CancelDeleteWin = '//div[contains(text(), "取消")]'
# 删除页面确定按钮
DetermineDelete = '//div[contains(text(), "确定")]'
# 删除页面确定按钮
DeleteS = '//div[contains(text(), "删除成功")]'

# 重命名统一按钮
ClickRename = '//div[contains(text(), "重命名")]'
# 重命名成功
RNS = '//div[contains(text(), "重命名成功")]'
# 第二个分组
TwoGroup = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/span[2]'
# 第二个分组第一个角色名称
TwoGroupOneRole = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]'
# 第二个分组的选择按钮
TwoGroupChoice = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/span[3]'
# 分组重命名窗口关闭按钮
CloseGroupRenameWin = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[2]/div/svg/use'
Delete = '//div[contains(text(), "删除")]'
# 删除分组窗口关闭按钮
CloseGroupDeleteWin = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div[2]/div/svg/use'
# 已添加的第一个角色
OneRole = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/img'
# 已添加的角色中的 删除 按钮
DeleteRole = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/div[1]/div/span'
# 清空按钮
Empty = '//div[contains(text(), "清空")]'
DetermineAddRole = '//div[contains(text(), "确认添加")]'




"""
帮助
"""
# 帮助按钮
Help = '//*[@id="kitten_header"]/div[1]/div[4]/div'
# 帮助-->帮助按钮
Helps = '//div[contains(text(), "帮助")]'
# 工具
Tool = '//div[contains(text(), "工具")]'
# 源码图鉴
CodeBooks = 'div[data-report-click="帮助-源码图鉴"]'
# 加入QQ群
JoinQQ = 'div[data-report-click="帮助-加入QQ群"]'
# 关闭QQ页面
CloseQQPage = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div'
# 积木图片
BlockPicture = 'div[data-report-click="工具-积木图片"]'
# 关闭积木图片页面
CloseBlockPicturePage = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[2]'
# 【我知道啦】按钮
CloseBlockPicturePages = '//div[contains(text(), "我知道啦")]'
# 硬件助手
HardwareAssistant = 'div[data-report-click="工具-硬件助手"]'
# 关闭硬件助手页面
CloseHAPage = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[2]'
# 下载硬件助手
DownloadHA = '//div[contains(text(), "下载")]'
DownloadHAC = 'div[data-report-click="硬件助手-下载"]'
# Scratch文件导入
Scratch = 'div[data-report-click="工具-Scratch文件导入"]'
# 关闭Scratch页面
CloseScratchPage = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[2]'
# 打开本地Scratch文件
LoadScratch = 'div[data-report-click="Scratch文件-导入文件"]'

"""
用户反馈
"""
UFB = 'div[data-report-click="Pre-反馈建议"]'


"""
设置
"""
# 设置按钮
KittenSet = 'header-setting-btn'
# 修改语言
SCNSet = '//div[contains(text(), "修改语言")]'
TCNSet = '//div[contains(text(), "修改語言")]'
ENSet = '//div[contains(text(), "Language")]'

# 简体中文
SimpleChinese = 'div[data-report-click="切换语言-简体中文"]'
# 繁体中文
ComplexChinese = 'div[data-report-click="切换语言-繁体中文"]'
# 英语
English = 'div[data-report-click="切换语言-英文"]'
# 主题颜色
ColourSet = '//div[contains(text(), "主题颜色")]'
# 黄色
Yellow = 'span[style="width: 14px; height: 14px; border-radius: 50%; background: rgb(255, 219, 41); margin-right: 5px;"]'
# 蓝色
Blue = 'span[style="width: 14px; height: 14px; border-radius: 50%; background: rgb(41, 126, 255); margin-right: 5px;"]'
# 绿色
Green = 'span[style="width: 14px; height: 14px; border-radius: 50%; background: rgb(29, 184, 106); margin-right: 5px;"]'
# 橙色
Orange = 'span[style="width: 14px; height: 14px; border-radius: 50%; background: rgb(255, 123, 46); margin-right: 5px;"]'
# 紫色
Violet = 'span[style="width: 14px; height: 14px; border-radius: 50%; background: rgb(148, 41, 255); margin-right: 5px;"]'
# 红色
Gules = 'span[style="width: 14px; height: 14px; border-radius: 50%; background: rgb(255, 41, 112); margin-right: 5px;"]'
# 积木样式
BlockStyle = '//div[contains(text(), "积木样式")]'
# 磁铁吸附
MagnetStyle = 'div[data-report-click="积木样式切换-磁吸"]'
# 经典样式
ClassicStyle = 'div[data-report-click="积木样式切换-经典"]'
# 积木栏模式
BlockGroupStyle = '//div[contains(text(), "积木栏模式")]'
# 收起模式
Collect = 'div[data-report-click="Pre-收起模式"]'
# 常驻模式
Fixed = 'div[data-report-click="Pre-常驻模式"]'
# 用户反馈
UserFeedback = 'div[data-report-click="设置-用户反馈"]'
# 创作环境检测
EquipmentTesting = 'div[data-report-click="设置-设备检测"]'
# 重新检查设备
Recheck = 'div[data-report-click="设置-重新检测"]'
# 重新检查页面关闭按钮
CloseRecheckPage = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/svg/use'
# Nemo编程
NemoProgramming = 'div[data-report-click="设置-手机编程Nemo"]'
# 关闭Nemo页面
CloseNemoPage = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div'
# 关于Kitten
Aboutkitten = 'div[data-report-click="设置-关于"]'
# 关闭【关于Kitten】介绍页面按钮
CloseAboutKitten = '//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div[2]'

"""
角色栏
"""
# 添加角色按钮:css
Addcharacter_button = 'div[data-report-click="角色栏-添加角色"]'
"""
素材库添加角色
"""
#角色栏素材库添加按钮
Library_character = 'div[data-report-click="角色栏-素材库"]'
#素材库角色
Character_id1 = 'div[data-id="1"]'
Character_id2 = 'div[data-id="2"]'
#素材库确认按钮
Confirm_add = 'div[class=" th1-bg-0 th1-bg-hover-m1 th1-bg-active-m2 th1-text-s1  btn--1q-Xf primary--1JoWA"]'
#素材库角色
Lib_add ='//*[@id="content_draggable_wrap"]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div[2]/div/div/div/div'
"""
画板添加角色
"""
#角色栏画板添加按钮
Drawingboard_character = 'div[data-report-click="角色栏-画板"]'
#画板图形选择按钮
Drawing_Button = 'li[data-aria-label="图形"]'
#画板基础图形
Drawing_graph = 'span[data-report-click="画板-图形-hot_1"]'
#画板确认按钮
Confirm_add1 = '//*[@id="PaintEditorWrapper"]/div/section/section/footer/div[2]/button'
#画板添加角色
Draw_add = '//*[@id="content_draggable_wrap"]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div[1]/div/div/div/div'
"""
随机添加角色
"""
#角色栏随机添加按钮
Random_character = 'div[data-report-click="角色栏-随机添加"]'
#workspace任意位置
workspace_id = 'workspace'
#选中角色
chara_selected = 'div[data-report-click="角色栏-选中角色"]'
"""
本地上传角色
"""
#角色栏本地添加按钮
Upload_character = 'div[data-report-click="角色栏-本地添加"]'
#本地添加入口
loadwindow = 'input[class="upload_btn--1i3xM" ]'
#上传角色
up_add = 'input[type="text"][value="test1"]'
"""
删除角色
"""
#删除角色按钮
del_icon1 = 'div[data-report-click="角色栏-删除角色"]'
#已删除角色1
del_chara1 = 'input[value="test1]'
#含有积木的角色
#del_chara2='//*[@id="content_draggable_wrap"]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div[5]'
#del_chara2='//*[@id="content_draggable_wrap"]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div[5]/div/div/div/div/div[3]'
del_chara2 ='//*[@id="content_draggable_wrap"]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div[5]/div/div/div/div'
#含有积木的角色删除按钮
del_icon2 = '[class="icon--33OD- delete_icon--R4Rze selected--13WAl"]'
#删除角色二次弹窗"确认"按钮
del_confirm = 'div[data-report-click="角色栏-确认删除角色"]'

"""
角色右键
"""
#选中角色
select_chara = 'div[class="entity-selected entity_wrap--3BHkT selected--13WAl"]'
#右键复制按钮
copy = 'div[data-report-click="角色栏-复制"]'
#复制的角色
copy_chara = 'input[type="text"][value$="(1)"]'
#右键改名
rename = 'div[data-report-click="角色栏-右键改名"]'
#右键改名输入框
#input_text='//div[@data-report-click="角色栏-选中角色"]/div[3]/div[3]/input'
input_text ='//*[@id="content_draggable_wrap"]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div[4]/div/div/div/div/div[3]/div[3]/input'
#右键创建分组按钮
c_group = 'div[data-report-click="分组-创建分组"]'
#已经创建的分组
group = 'div[class="fold_icon_wrap--3V_C0"]'
#右键导出角色
export = 'div[data-report-click="角色栏-导出角色"]'
#右键添加至背包
add_backpack ='div[data-report-click="角色栏-添加到背包"]'

"""
角色分组右键
"""
#右键复制分组
g_copy = 'div[data-report-click="分组-复制"]'
#复制的分组
group1 = 'input[type="text"][value$="组"]'



"""舞台区"""
# 运行按钮
Run = 'div[data-report-click="舞台-开始"]'
# 从当前屏幕开始运行1
RunOne = 'div[tabindex="-1"][style="box-shadow: rgba(41, 169, 255, 0.5) 0px 2px 4px 0px;"]'
# 选择从当前屏幕开始运行2
RunTwo = 'div[data-report-click="舞台-从当前屏幕运行"]'
# 选择从当前屏幕开始运行3
RunTwos = 'div[data-report-click="舞台-从第一屏幕运行"]'
# 舞台比例切换
Proportion = 'change_stage_mode_btn'
Vertical = 'div[data-report-click="舞台-竖版"]'
Horizontal = 'div[data-report-click="舞台-横版4:3"]'
Horizontals = 'div[data-report-click="舞台-横版16:9"]'
# 网格开关
OpenGrid = 'div[data-report-click="舞台-打开坐标"]'
CloseGrid = 'div[data-report-click="舞台-收起坐标"]'
# 舞台全屏按钮
FullScreen = 'div[data-report-click="舞台-打开全屏"]'
# 关闭舞台全屏
CloseFS = 'span[data-report-click="舞台-收起全屏"]'
# 手机预览按钮
Phone = 'div[data-report-click="手机预览"]'
# 手机预览页面链接
PhoneUrl = 'span[data-report-click="手机预览-复制链接"]'


""""舞台属性栏"""
# 选中背景
BG = 'css&&div[style="width: 124px; height: 84px; margin: 0px 0px 10px; border-radius: 6px;"]'
# 隐藏角色按钮
DBG = 'div[data-report-click="角色设置区-显示/隐藏"]'
# 锁定/解锁按钮
Locking = 'div[data-report-click="角色设置区-锁定/解锁"]'
# 角色旋转设置
Spin = 'svg[style="font-size: 14px; transform: rotate(180deg);"]'
# X坐标设置
Xa = '//*[@id="property_panel"]/div[5]/input'
Ya = '//*[@id="property_panel"]/div[6]/input'
Ia = '//*[@id="property_panel"]/div[7]/input'
Ka = '//*[@id="property_panel"]/div[8]/input'



"""屏幕"""
# 屏幕展开按钮
Unfold = 'div[data-report-click="屏幕-展开"]'
# 展开的屏幕列表中点击添加新的屏幕按钮
AddScreen = 'div[data-report-click="屏幕-展开添加"]'
# 屏幕栏中的小屏幕序列
OneScreen = 'screen_1'  # 一屏幕ID
TwoScreen = 'screen_2'  # 二屏幕ID
# 屏幕ID以上类推
CopyScreen = 'div[data-report-click="屏幕-收起复制"]'
# 删除屏幕
DelScreen = 'div[data-report-click="屏幕-右键删除"]'
# 屏幕展开缩略图
Aimg = 'img[alt="屏幕缩略图"]'
# 展开缩略图右键改名按钮
SRN = 'div[data-report-click="屏幕-右键改名"]'
# 缩略图重名input框
ipt = 'input[style="height: 20px; width: 106px; font-size: 14px; line-height: 20;"]'
CS = 'div[data-report-click="屏幕-展开复制"]'


"""其他"""
# 添加素材按钮
AddRole = 'div[data-report-click="角色栏-添加角色"]'
# 素材库添加素材按钮
MLAdd = 'div[data-report-click="角色栏-素材库"]'



"""素材库"""
# 素材库搜索
Search = 'input[placeholder="关键词搜索素材"]'
# 关闭素材库
CloseS = '//*[@id="material-dialog"]/div[1]/div[3]'
# 展开造型按钮
OpenRole = '//*[@id="content_draggable_wrap"]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]'
# 造型选择
RoleSLC = '//*[@id="content_draggable_wrap"]/div[2]/div/div[3]/div[4]/div'
# 素材库选择造型按钮
SSlc = 'div[data-report-click="造型栏-素材库添加"]'
Audio = 'div[category-name="声音"]'
Audios = 'div[data-report-click="声音-添加声音"]'
AudioSc = 'div[data-report-click="声音-素材库添加"]'
RoleS = '//div[contains(text(), "角色")]'
RoleS1 = '//li[contains(text(), "全部")]'
RoleS2 = '//li[contains(text(), "形象")]'
RoleS3 = '//li[contains(text(), "界面")]'
RoleS4 = '//li[contains(text(), "道具")]'
RoleS5 = '//li[contains(text(), "特效")]'


