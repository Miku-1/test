import time
from selenium import webdriver
driver_path = r'D:\myData\Python\test\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driver_path)
url = 'https://www.baidu.com'
browser.get(url)
time.sleep(3)
# 找到输入框,输入selenium进行搜索
browser.find_element_by_id('kw').send_keys('selenium')
time.sleep(2)


browser.quit()

