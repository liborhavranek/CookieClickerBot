from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

ser = Service(r"C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

driver.maximize_window()
cookie = driver.find_element(By.XPATH, r"//*[@id='cookie']")
money = driver.find_element(By.XPATH, r"//*[@id='money']")
cps = driver.find_element(By.CSS_SELECTOR, "#cps")


def buy_item():
    store_items = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed) b")
    store_prices = [float((item.text.split()[2]).replace(",", ".")) for item in store_items]
    max_index = store_prices.index(max(store_prices))
    store_items[max_index].click()


buy_interval = time.time() + 5
#measure_interval = time.time() + 60 * 5

while True:
    cookie.click()
    if time.time() >= buy_interval:
        buy_item()
        buy_interval = time.time() + 5
