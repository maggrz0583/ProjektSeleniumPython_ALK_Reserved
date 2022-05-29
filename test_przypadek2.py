#Import bibliotek

import unittest
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from time import sleep

class TestSortowanie(unittest.TestCase):
    def setUp(self):
        #Przygotowanie testu
        #1. Otwarta strona https://www.reserved.com/pl/pl/
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.reserved.com/pl/pl/")

    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()

    def testByPrice(self, span=None):
        driver = self.driver
        # Zaakceptuj popup
        driver.implicitly_wait(15)
        accept_btn = driver.find_element(By.ID,"cookiebotDialogOkButton")
        accept_btn.click()

        # Kliknij w menu "kobieta"
        kobieta = driver.find_element(By.ID, "category-link")
        kobieta.click()



       # Jeśli uruchamiam ten plik
if __name__ == "__main__":
         # Uruchom testy
     unittest.main()


