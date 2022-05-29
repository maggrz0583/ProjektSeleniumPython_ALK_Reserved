#Import bibliotek

import unittest
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from time import sleep

class TestRegistration(unittest.TestCase):
    def setUp(self):
        #Przygotowanie testu
        #1. Otwarta strona https://www.reserved.com/pl/pl/
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.reserved.com/pl/pl/")

    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()

    def testInvalidEmail(self, span=None):
        driver = self.driver
        # Zaakceptuj popup
        driver.implicitly_wait(15)
        accept_btn = driver.find_element(By.ID,"cookiebotDialogOkButton")
        accept_btn.click()

        #Kliknij w menu "kobieta"
        kobieta = driver.find_element(By.XPATH, "//*[@id="navigation-wrapper"]/div/ul/li[2]/a")
        kobieta.click()
        # Jeśli uruchamiam ten plik
if __name__ == "__main__":
         # Uruchom testy
     unittest.main()


