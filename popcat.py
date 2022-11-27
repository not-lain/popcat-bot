from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

Path = "./chromedriver.exe"

driver = webdriver.Chrome(Path)
driver.get("https://popcat.click/")

time.sleep(7)
while 1 : 
    search = driver.find_element(By.CLASS_NAME,"title")
    search.click()
    