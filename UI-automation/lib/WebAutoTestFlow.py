import pyperclip
import win32api
import win32con
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#import win32api   #模拟键盘事件
#import win32con   #控制键盘
#import pyperclip
from time import sleep


DelayTime = 1

class AutoLib():
    def __init__(self,driver):
        self.driver = driver


# ----------------------------------------------------

    def GetElement(self,style):
        if "&&" not in style:
            raise NameError("语法错误，style缺少'&&'")

        else:

            by = style.split("&&")[0]
            value = style.split("&&")[1]

            if by == "id":
                element = self.driver.find_element_by_id(value)

            elif by == "name":
                element = self.driver.find_element_by_name(value)

            elif by == "class":
                element = self.driver.find_element_by_class_name(value)

            elif by == "link_text":
                element = self.driver.find_element_by_link_text(value)

            elif by == "xpath":
                element = self.driver.find_element_by_xpath(value)

            elif by == "css":
                element = self.driver.find_element_by_css_selector(value)

            else:
                raise NameError(
                    "请输入正确的定位元素：'id','name','class','link_text','xpath','css'")
            return element

# ----------------------------------------------------

    def GetElementClick(self,style,delay=DelayTime):
        if "&&" not in style:
            raise NameError("语法错误，style缺少'&&'")

        else:

            by = style.split("&&")[0]
            value = style.split("&&")[1]

            if by == "id":
                element = self.driver.find_element_by_id(value).click()
                time.sleep(delay)

            elif by == "name":
                element = self.driver.find_element_by_name(value).click()
                time.sleep(delay)

            elif by == "class":
                element = self.driver.find_element_by_class_name(value).click()
                time.sleep(delay)

            elif by == "link_text":
                element = self.driver.find_element_by_link_text(value).click()
                time.sleep(delay)

            elif by == "xpath":
                element = self.driver.find_element_by_xpath(value).click()
                time.sleep(delay)

            elif by == "css":
                element = self.driver.find_element_by_css_selector(value).click()
                time.sleep(delay)

            else:
                raise NameError(
                    "请输入正确的定位元素：'id','name','class','link_text','xpath','css'")
            return element

# ----------------------------------------------------

    def GetElementSendKeys(self,style,send_key,delay=DelayTime):
        if "&&" not in style:
            raise NameError("语法错误，style缺少'&&'")

        else:

            by = style.split("&&")[0]
            value = style.split("&&")[1]

            if by == "id":
                element = self.driver.find_element_by_id(value).send_keys(send_key)
                time.sleep(delay)

            elif by == "name":
                element = self.driver.find_element_by_name(value).send_keys(send_key)
                time.sleep(delay)

            elif by == "class":
                element = self.driver.find_element_by_class_name(value).send_keys(send_key)
                time.sleep(delay)

            elif by == "link_text":
                element = self.driver.find_element_by_link_text(value).send_keys(send_key)
                time.sleep(delay)

            elif by == "xpath":
                element = self.driver.find_element_by_xpath(value).send_keys(send_key)
                time.sleep(delay)

            elif by == "css":
                element = self.driver.find_element_by_css_selector(value).send_keys(send_key)
                time.sleep(delay)

            else:
                raise NameError(
                    "请输入正确的定位元素：'id','name','class','link_text','xpath','css'")
            return element

# ----------------------------------------------------

    def ShowWaitVisibility(self, style, timeout=20, delay=DelayTime):

        """
        ShowWaitVisibility:显示等待函数（该方法需要找到元素，并且该元素也可见）
        提供6种显示等待方法，开发者随使用情况调用
        style必须为 XX&&XX的格式，以字符串形式传参
        && 前面是定位的方式，后面是定位的元素。例如：id&&#kk
        timeout:显示等待超时时间
        delay:延迟时间
        # presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
        # visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。
        :return:
        """
        # 显示等待方法导入
        if "&&" not in style:
            raise NameError("语法错误，style缺少'&&'")

        else:

            by = style.split("&&")[0]
            value = style.split("&&")[1]

            if by == "id":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located((By.ID, value)))
                time.sleep(delay)
                return expected

            elif by == "name":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located((By.NAME, value)))
                time.sleep(delay)
                return expected

            elif by == "class":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, value)))
                time.sleep(delay)
                return expected

            elif by == "link_text":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, value)))
                time.sleep(delay)
                return expected

            elif by == "xpath":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located((By.XPATH, value)))
                time.sleep(delay)
                return expected

            elif by == "css":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
                time.sleep(delay)
                return expected

            else:
                raise NameError(
                    "请输入正确的定位元素：'id','name','class','link_text','xpath','css'")

# ----------------------------------------------------

    def ShowWaitV_until_not(self,style, timeout=20, delay=DelayTime):

        if "&&" not in style:
            raise NameError("语法错误，style缺少'&&'")
        else:
            by = style.split("&&")[0]
            value = style.split("&&")[1]

            if by == "id":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.visibility_of_element_located((By.ID, value)))
                time.sleep(delay)
                return expected

            elif by == "name":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.visibility_of_element_located((By.NAME, value)))
                time.sleep(delay)
                return expected

            elif by == "class":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.visibility_of_element_located((By.CLASS_NAME, value)))
                time.sleep(delay)
                return expected

            elif by == "link_text":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.visibility_of_element_located((By.LINK_TEXT, value)))
                time.sleep(delay)
                return expected

            elif by == "xpath":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.visibility_of_element_located((By.XPATH, value)))
                time.sleep(delay)
                return expected

            elif by == "css":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
                time.sleep(delay)
                return expected

            else:
                raise NameError(
                    "请输入正确的定位元素：'id','name','class','link_text','xpath','css'")

# ----------------------------------------------------

    def ShowWaitPresence(self, style, timeout=20, delay=DelayTime):

        """
        ShowWaitPresence:显示等待函数（该方法不关心元素是否可见，只关心元素是否存在在页面中）
        提供6种显示等待方法，开发者随使用情况调用
        style必须为 XX&&XX的格式，以字符串形式传参
        && 前面是定位的方式，后面是定位的元素。例如：id&&#kk
        timeout:显示等待超时时间
        delay:延迟时间
        # presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
        # visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。
        :return:
        """
        # 显示等待方法导入
        if "&&" not in style:
            raise NameError("语法错误，style缺少'&&'")

        else:

            by = style.split("&&")[0]
            value = style.split("&&")[1]

            if by == "id":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.ID, value)))
                time.sleep(delay)
                return expected

            elif by == "name":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.NAME, value)))
                time.sleep(delay)
                return expected

            elif by == "class":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
                time.sleep(delay)
                return expected

            elif by == "link_text":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
                time.sleep(delay)
                return expected

            elif by == "xpath":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.XPATH, value)))
                time.sleep(delay)
                return expected

            elif by == "css":
                expected = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
                time.sleep(delay)
                return expected

            else:
                raise NameError(
                    "请输入正确的定位元素：'id','name','class','link_text','xpath','css'")

# ----------------------------------------------------

    def ShowWaitP_until_not(self, style, timeout=20, delay=DelayTime):
        if "&&" not in style:
            raise NameError("语法错误，style缺少'&&'")

        else:

            by = style.split("&&")[0]
            value = style.split("&&")[1]

            if by == "id":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.presence_of_element_located((By.ID, value)))
                time.sleep(delay)
                return expected

            elif by == "name":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.presence_of_element_located((By.NAME, value)))
                time.sleep(delay)
                return expected

            elif by == "class":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.presence_of_element_located((By.CLASS_NAME, value)))
                time.sleep(delay)
                return expected

            elif by == "link_text":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.presence_of_element_located((By.LINK_TEXT, value)))
                time.sleep(delay)
                return expected

            elif by == "xpath":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.presence_of_element_located((By.XPATH, value)))
                time.sleep(delay)
                return expected

            elif by == "css":
                expected = WebDriverWait(self.driver, timeout, 1).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
                time.sleep(delay)
                return expected

            else:
                raise NameError(
                    "请输入正确的定位元素：'id','name','class','link_text','xpath','css'")


    def shangchuan(self,file_path,webEle):
        '''
            import win32api   #模拟键盘事件
            import win32con   #控制键盘
            import pyperclip  #拷贝粘贴字符串
            针对非input标签上传
            @file_path:上传的路径名
            @
        :return:
        '''
        pyperclip.copy(file_path)
        self.GetElementClick(webEle)
        sleep(0.5)
        win32api.keybd_event(17, 0, 0, 0)
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        win32api.keybd_event(13, 0, 0, 0)  # (回车)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按键
        time.sleep(2)
        return True




        pass