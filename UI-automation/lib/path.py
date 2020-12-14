import os
import time


# 文件名格式
NameFormat = str(time.strftime("%Y%m%d%H%M%S",time.localtime()))
ReportName = NameFormat + '.html'
ImageName = NameFormat + '.jpg'


# 下载路径
# DownloadP = "C:\\Users\\Administrator\\Downloads"

# 未下载完成的硬件助手
# HL = os.path.join(DownloadP,'编程猫硬件助手_windows_32.zip.crdownload')


# 下载页面的文件数量
# DLCount = len(os.listdir(DownloadP))

# 判断是否有硬件助手
# HDLResult = [i for i in os.listdir(DownloadP) if '硬件' in i]



# 工程根目录
BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试入口
TESTPATH = os.path.join(BASEPATH,'bin')

# 用例目录
CASEPATH = os.path.join(BASEPATH,'TestCase')

# 报告路径
REPORTPATH = os.path.join(BASEPATH,'TestReport',ReportName)

# proxy配置路径

#上传角色素材路径
filepath= os.path.join(BASEPATH,'character_test/test1.jpeg')

#素材库的角色图
role= os.path.join(BASEPATH,'character_test\\role.jpg')
#音乐
music=os.path.join(BASEPATH,'character_test\music.mp3')
#背景
background=os.path.join(BASEPATH,'character_test\\background.jpg')




#--------------------------------------积木区-------------------------------------------
jimu='开始'


print(BASEPATH)








