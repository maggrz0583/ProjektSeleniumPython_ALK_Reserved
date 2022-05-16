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

        #Kliknij profil - otwiera się menu z opcjami zalogowania/utworzenia konta
        profile_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[3]/div[2]")
        driver.implicitly_wait(10)
        #profile_button.click()
        webdriver.ActionChains(driver).move_to_element(profile_button).perform()

        # Utwórz konto
        register = driver.find_element(By.LINK_TEXT, "Zarejestruj się")
        register.click()
        #otwiera się strona rejestracji
        #self.assertIn("Utwórz konto", driver.title)
#
        # Jeśli uruchamiam ten plik
if __name__ == "__main__":
         # Uruchom testy
     unittest.main()