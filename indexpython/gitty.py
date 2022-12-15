print("heelo")
print("samra branchddgdgeg")
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
driver.find_element(By.XPATH,"//a[@class='toogle-icon full-content']")
driver.find_element(By.CLASS_NAME,'paragrapgh-text-3 active')
time.sleep(10)
#//p[@class='paragraph-text-3 active']

