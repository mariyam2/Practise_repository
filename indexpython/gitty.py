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
time.sleep(3)
#merchantlist = driver.find_elements(By.CLASS_NAME ,"flex align-items-center")
#print("this is the number of merchants", len(merchantlist))
time.sleep(3)
driver.execute_script("window.scrollBy(0,2000)","")
time.sleep(4)
#driver.find_element(By.XPATH,"//input[@placeholder='Search by name or email'").send_keys('Datasoft QA')
#time.sleep(3)
#//input[@placeholder='Search by name or email'
driver.find_element(By.XPATH, "//span[normalize-space()='Add Merchant']").click()
time.sleep(3)
# drop-down driver.find_element(By.XPATH, "//span[@class='p-dropdown-trigger-icon ng-tns-c52-119 pi pi-chevron-down']").click()
driver.find_element(By.XPATH,"//div[@aria-label='dropdown trigger']").click()
time.sleep(3)
#driver.find_element(By.XPATH,"//li[@id aria-label='Charity pr association']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[@aria-label='Partnership']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='businesstype'][3]").send_keys("jjjj")

time.sleep(3)
