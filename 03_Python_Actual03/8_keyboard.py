import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
browser.maximize_window()

browser.get('https://form.office.naver.com/form/editor.cmd?docId=ZDVhNmExYmItMzNhNy00ZjVmLWJmMTQtYWYxYTIzOTVmZTA1&templateId=41002')

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="id"]')

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택하기")
    elem.
else:
    print("선택 되어 있으므로 아무것도 안함")

time.sleep(5)