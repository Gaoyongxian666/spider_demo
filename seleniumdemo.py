# encoding: utf-8
'''
@author: gaoyongxian666
@file: seleniumdemo.py
@time: 2018/4/10 20:33
'''



from telnetlib import EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
browser=WebDriver("")
browser.get("")
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

# 打开页面设置代理，超时

# 获取元素
# element = driver.find_element_by_id("passwd-id")
# element = driver.find_element_by_name("passwd")
# element = driver.find_element_by_xpath("//input[@id='passwd-id']")
# browser.page_source
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')进行遍历
# 获取属性
# logo.get_attribute('class')
# 获取文本
# input.text




# 等待
# title_is
# title_contains
# presence(存在)_of_element_located
# visibility(能见度)_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element(元素)
# text_to_be_present_in_element_value
# frame(有木架的)_to_be_available_and_switch(转换)_to_it
# invisibility(看不见)_of_element_located(处于)
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection(选择)_state_to_be
# element_located_selection_state_to_be
# alert_is_present



# 显示等待
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "myDynamicElement"))
# )
# 隐式等待
# driver.implicitly_wait(10)

# 元素交互:keyboard like RETURN, F1, ALT etc.
# elem.clear()
# elem.send_keys("pycon") textarea or text field
# elem.send_keys(Keys.RETURN)
# element.send_keys(" and some", Keys.ARROW_DOWN)

# 前进后退，选项卡管理
# driver.forward()
# driver.back()
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')


# 滚动,执行js
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# browser.execute_script('alert("To Bottom")')
# 1.js = "window.scrollTo(0, %d)"%a
# 2.我爬京东和淘宝的方法是，设置一个循环，依次类似这样，第一次，document.body.scrollTop=1080，
# 第二次document.body.scrollTop=2048
# 这样以此类推这样下去整个页面都滚了一次就好了。
# 两种都可以


# cookie
# cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
# driver.add_cookie(cookie)
# driver.get_cookies()


# frame跳转
# driver.switch_to_window("windowName")
# 对话框跳转
# alert = driver.switch_to_alert()
# authenticate


# ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
