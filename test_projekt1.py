#Import bibliotek

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestRegistration(unittest.TestCase):
    def setUp(self):
        #Przygotowanie testu
        #1. Otwarta strona https://www.douglas.pl/pl
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.sephora.pl/")

    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()

    def testInvalidEmail(self):
        driver = self.driver
        # Zaakceptuj popup
        driver.implicitly_wait(15)
        accept_btn = driver.find_element(By.ID,"footer_tc_privacy_button_2")
        accept_btn.click()

        #Jeśli uruchamiam ten plik
if __name__== "__main__":
#Uruchom testy
    unittest.main()
