# coding:utf-8
# 确定默认编码格式不能少
__author__ = 'huling'

from selenium import webdriver


import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
driver = webdriver.Ie()
driver.get("http://10.66.62.88:8080/wms/")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("superadmin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys(111)
print driver.find_element_by_name("password").text
driver.find_element_by_xpath("//input[@class='btn btn-primary btn-block']").click()
time.sleep(2)
title=driver.title
print title
if title == u"智慧仓储系统":
    print "OK"
else:
    print "wrong"

driver.quit()
print "test"