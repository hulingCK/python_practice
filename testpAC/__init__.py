#-*- coding: UTF-8 -*-
__author__ = 'john'
import csv #导入csv包
from selenium import webdriver
import os
import xlrd
import xlwt
import datetime
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
driver = webdriver.Firefox()
#Readmine网站
driver.get("http://10.66.62.16")
time.sleep(2)
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("huling")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys(11111111)
driver.find_element_by_name("login").click() #登录
time.sleep(2)
#定位项目下拉框
project1 = driver.find_element_by_name("project_quick_jump_box")
#选择下拉框选项——商贸易
project1.find_elements_by_tag_name("option")[5].click()
time.sleep(2)
#点击“问题”选项卡
driver.find_element_by_link_text(u"问题").click()
#定位过滤器下拉框
filterAdd=driver.find_element_by_id("add_filter_select")
#增加过滤器“跟踪”
filterAdd.find_elements_by_tag_name("option")[2].click()
#定位状态下拉框
status=driver.find_element_by_id("operators_status_id")
#选择状态为“等于”
status.find_elements_by_tag_name("option")[1].click()
time.sleep(2)
#定位状态为等于时的条件
xiancun=[0 for index in range(0,14)]#现存bug
for i in range(0,14):
    conditions=driver.find_element_by_id("values_status_id_1").find_elements_by_tag_name("option")
    conditions[i].click()
    #应用
    driver.find_element_by_link_text(u"应用").click()
    time.sleep(1)
    try:
        driver.find_element_by_class_name("nodata").is_displayed()
    except:
        text=driver.find_element_by_class_name("items").text
        print text.split('/')[1].split(')')[0]
        xiancun[i]=int(text.split('/')[1].split(')')[0])#现存
    else:
        xiancun[i]=0
#由于与excel顺序不一致，需要做调整
xiancuntoExcel=[]
xiancuntoExcel.append(xiancun[0])#new
xiancuntoExcel.append(xiancun[1])#inprogress
xiancuntoExcel.append(xiancun[2])#resolvel
xiancuntoExcel.append(xiancun[4])#feedback
xiancuntoExcel.append(xiancun[3])#NMI
xiancuntoExcel.append(xiancun[10])#confirmed
xiancuntoExcel.append(xiancun[5])#reopen
xiancuntoExcel.append(xiancun[9])#suspended
xiancuntoExcel.append(xiancun[8])#defereed
xiancuntoExcel.append(xiancun[6])#closed
print(u"本周现存: \n"+xiancuntoExcel)#现存
#本周新增——————————————————————————————————
#选择状态为“全部”
status.find_elements_by_tag_name("option")[4].click()
#增加过滤器“创建于”
filterAdd.find_elements_by_tag_name("option")[9].click()
#选择>=
driver.find_element_by_id("operators_created_on").find_elements_by_tag_name("option")[1].click()
driver.find_element_by_class_name("ui-datepicker-trigger").click()
time.sleep(1)
#定位到本周星期1
weekday=int(time.strftime('%w',time.localtime(time.time())))#以星期天为第一天的当前星期几
todayY=int(time.strftime('%Y',time.localtime(time.time())))#今天的年
todayM=int(time.strftime('%m',time.localtime(time.time())))#今天的月
todayD=int(time.strftime('%d',time.localtime(time.time())))#今天在月中的天数
monday=str(datetime.datetime(todayY,todayM,todayD-weekday+1+1)).split(' ')[0]#星期一
#在日前中输入时间
driver.find_element_by_id("values_created_on_1").send_keys(monday)
#应用
driver.find_element_by_link_text(u"应用").click()
time.sleep(1)
newadd=0
try:
    driver.find_element_by_class_name("nodata").is_displayed()
except:
    text=driver.find_element_by_class_name("items").text
    print text.split('/')[1].split(')')[0]
    newadd=int(text.split('/')[1].split(')')[0])#现存
else:
    newadd=0
print (u"本周新增new: \n"+newadd)
#本周新增resolved
#取消创建于的勾
driver.find_element_by_id("cb_created_on").click()
#选择状态为“等于”
status.find_elements_by_tag_name("option")[1].click()
#closed
driver.find_element_by_id("values_status_id_1").find_elements_by_tag_name("option")[6].click()
#增加过滤器“更新于”
filterAdd.find_elements_by_tag_name("option")[10].click()
#选择>=
driver.find_element_by_id("operators_updated_on").find_elements_by_tag_name("option")[1].click()
#输入日期
driver.find_element_by_id("values_updated_on_1").send_keys(monday)
resolvedadd=0
try:
    driver.find_element_by_class_name("nodata").is_displayed()
except:
    text=driver.find_element_by_class_name("items").text
    print text.split('/')[1].split(')')[0]
    resolvedadd=int(text.split('/')[1].split(')')[0])#现存
else:
    resolvedadd=0
print (u"本周新增resolved: \n"+resolvedadd)
print (u"本周新增closed: \n"+resolvedadd)
print (u"本周已解决new: \n"+resolvedadd)






#导出CSV
driver.find_element_by_class_name("csv").click()
#定位CSV对话框
div=driver.find_element_by_id("csv-export-options")
div.find_element_by_id("columns_all").click()
#点击导出
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.getcwd())

div.find_elements_by_xpath("//input[@value='导出']")[0].click()
time.sleep(3)
#读取本地csv文件
my_file = 'C:\\Users\\john\\Downloads\\issues.csv'
data = csv.reader(file(my_file, 'rb'))
# #现存new bug数
#
#
# newBugcount=0;in_progress=0;resolved=0;NMF=0;feedback=0;reopen=0;closed=0;rejected=0;deferred=0;
# suspended=0;confirmed=0;assessing=0;designing=0;completed=0
# for line in data:
#     newBugcount += 1
# print newBugcount



