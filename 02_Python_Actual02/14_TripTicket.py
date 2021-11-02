import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time



browser = webdriver.Chrome()
browser.maximize_window() #창 최대화
msg = browser.get_log('browser')
browser.execute_cdp_cmd('Network.getResponseBody', {'requestId': msg["message"]["params"]["requestId"]})



url = "https://m-flight.naver.com/"
browser.get(url)

# elem = browser.find_element_by_class_name("searchBox_tab__cPM55 searchBox_Tab__39-OR")
# elem.click()
time.sleep(5)
browser.find_elements_by_class_name("searchBox_tab__cPM55.searchBox_Tab__39-OR")[1].click()

browser.find_elements_by_class_name("tabContent_option__2y4c6.select_Date__1aF7Y")[0].click()

time.sleep(0.5)
browser.find_elements_by_class_name("sc-crzoAE.hnpClg.inner")[10].click()

# browser.execute_script("argument[0].click();",element)


# element = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[1]/button[2]")
# element.click()
# # browser.execute_script("arguments[0].click();", element)
# element2 = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button")
# element2.click()

# element3 = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/button")
# element3.click()



# element2 = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button")
# browser.execute_script("arguments[0].click();", element2)

# browser.find_element_by_link_text("26")[0].click()
# //*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[3]/button
# # browser.find_element_by_class_name("tabContent_option__2y4c6 select_Date__1aF7Y").click()


