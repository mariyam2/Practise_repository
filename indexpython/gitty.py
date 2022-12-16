print("heelo")

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://10.4.4.20:6121/login")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='login-email']").send_keys('luke@gmail.com')
time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Enter Password']").send_keys('123')
driver.find_element(By.XPATH,"//span[@class='p-button-label']").click()
#//input[@placeholder='Enter Password']
time.sleep(10)
driver.find_element(By.XPATH,"//div[@class='hide-show-element']").click()

driver.find_element(By.XPATH,'//body[1]/app-root[1]/app-features[1]/div[1]/div[1]/app-side-navigation[1]/div[1]/div[1]/p-tree[1]/div[1]/div[1]/ul[1]/p-treenode[4]/li[1]').click()
time.sleep(10)
#//p[@class='paragraph-text-3 active']

