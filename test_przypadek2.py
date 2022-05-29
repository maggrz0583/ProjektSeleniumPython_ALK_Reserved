#Import bibliotek

import unittest
from hashlib import new

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
        driver.implicitly_wait(20)
        accept_btn = driver.find_element(By.ID,"cookiebotDialogOkButton")
        accept_btn.click()

        #Najedź w menu głównym na pozycję "kobieta"
        kobieta = driver.find_element(By.XPATH, '//*[@id="navigation-wrapper"]/div/ul/li[2]/a')
        driver.implicitly_wait(30)
        webdriver.ActionChains(driver).move_to_element(kobieta).perform()

        #Kliknij w podmenu na pozycję "sukienki"
        sukienki = driver.find_element(By.LINK_TEXT, 'Sukienki')
        sukienki.click()



       # Jeśli uruchamiam ten plik
if __name__ == "__main__":
         # Uruchom testy
     unittest.main()


