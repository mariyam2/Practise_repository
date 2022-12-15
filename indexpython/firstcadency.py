import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://10.4.4.20:6121/login")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='login-email']").send_keys('luke@gmail.com')
driver.find_element(By.XPATH,"//input[@placeholder='Enter Password']").send_keys('123')
driver.find_element(By.XPATH,"//span[@class='p-button-label']").click()
#//input[@placeholder='Enter Password']
time.sleep(10)
driver.find_element(By.XPATH,"//div[@class='side-navigation-menu-container half-content']").click()
onboard = driver.find_element(By.XPATH,"//p-treenode[4]//li[1]//div[1]//span[2]//span[1]//div[1]")
onboard.click()
time.sleep(15)
merchantlist = driver.find_elements(By.CLASS_NAME ,"flex align-items-center")
print("this is the number of merchants", len(merchantlist))
time.sleep(10)
driver.quit()
driver.close()
#//p[@class='paragraph-text-3 active']


