import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


    def cust_elements(self):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://10.4.4.20:6121/login")
    driver.find_element(By.XPATH, "//input[@id='EmailID']").send_keys('samdr')
    time.sleep(2)
    driver.find_element(By.ID, "EmailPassword").send_keys('cav0nhfVrvph')
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(4)
    driver.find_element(By.XPATH,"//div[@class= 'side-navigation-menu-container half-content']").click()
    time.sleep(4)
    driver.find_element(By.XPATH,"//p[normalize-space()='Customers & Receivables']").click()
    time.sleep(4)
    driver.find_element(By.XPATH,"//p[@class='paragraph-text-3 active']").click()
    time.sleep(4)
#     will be continued by samra, more elements to be added
    cust_detail_tabfront = driver.find_elements(By.Xpath, "//span[text()='CUST-000006']")
    cust_detail_viewtab = driver.find_elements(By.Xpath, "//div[text()='CUST-000006']")

class customerry(unittest.TestCase)
         def testName(cust_elements):
        # cust_detail_tabfront = driver.find_elements(By.Xpath, "//span[text()='CUST-000006']")
        # cust_detail_viewtab = driver.find_elements(By.Xpath, "//div[text()='CUST-000006']")
        message= "no match"
        self.assertTrue(cust_detail_tabfront or cust_detail_viewtab, message)


if __name__ == '__main__':
    unittest.main()
#end