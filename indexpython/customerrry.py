import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




class customerry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("http://10.4.4.20:6121/login")
        cls.driver.maximize_window()
        cls.driver.find_element(By.XPATH, "//input[@id='EmailID']").send_keys('samdr')
        time.sleep(2)
        cls.driver.find_element(By.ID, "EmailPassword").send_keys('cav0nhfVrvph')
        time.sleep(2)
        cls.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)
        cls.driver.find_element(By.XPATH, "//div[@class= 'side-navigation-menu-container half-content']").click()
        time.sleep(4)
        cls.driver.find_element(By.XPATH, "//p[normalize-space()='Customers & Receivables']").click()
        time.sleep(4)
        cls.driver.find_element(By.XPATH, "//p[@class='paragraph-text-3 active']").click()
        time.sleep(4)

    def testName(cust_elements):
            cust_detail_tabfront = cust_elements.driver.find_elements(By.XPATH, "//span[text()='CUST-000006']")

            cust_detail_viewtab = cust_elements.driver.find_elements(By.XPATH, "//div[text()='CUST-000006']")
            message= "no match"
            cust_elements.assertEqual(cust_detail_tabfront.text, cust_detail_viewtab.text, message)


if __name__ == '__main__':
    unittest.main()
#end