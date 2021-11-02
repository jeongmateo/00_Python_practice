from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


browser = webdriver.Chrome()
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
# 1. Naver borwser 켜기
browser.get("https://naver.com")
# 2.로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "jeongmate7", pw = "Wjdgkstn20!")
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
print(type(input_js))
browser.execute_script(input_js)
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.find_element_by_id("log.login").click()

# 5. id를 새로 입력
print(browser.page_source)

browser.quit()

