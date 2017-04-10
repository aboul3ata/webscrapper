from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess
import time

driver = webdriver.Safari()
driver.get('http://www.ebay.com')
searcher = driver.find_element_by_css_selector('.ui-autocomplete-input')
searcher.send_keys('star wars')
submitbutton = driver.find_element_by_css_selector('#gh-button')
submitbutton.click()

time.sleep(5)

items = driver.find_elements_by_css_selector('a.vip')
print(items)
for item in items:
    print(item.text)
