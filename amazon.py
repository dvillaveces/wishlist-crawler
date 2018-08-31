import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

wish_list_url = "https://www.amazon.com/gp/registry/wishlist/28Q24IH2QSNHU/"

browser = webdriver.Chrome()

browser.get(wish_list_url)
#time.sleep(1)

elems = browser.find_elements(By.CSS_SELECTOR, "a[id^='itemName']")
prices = browser.find_elements(By.CSS_SELECTOR, "span[id^='itemPrice']")


for elem in elems:
    print(elem.text)
for price in prices:
    print(price.text)
