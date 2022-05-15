#Import bibliotek

import unittest
from selenium import webdriver
from selenium.webdriver.common import actions
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

        #Kliknij profil - otwiera się menu z opcjami zalogowania/utworzenia konta
        profile = driver.find_element(By.LINK_TEXT, "Konto")
        webdriver.ActionChains(driver).move_to_element(profile).perform()

        # Utwórz konto
        registracion = driver.find_element(By.LINK_TEXT, "UTWÓRZ KONTO")
        registracion.click()
        #otwiera się strona rejestracji - NIE AŁA
        self.assertIn("UTWÓRZ KONTO", driver.title)

        # Jeśli uruchamiam ten plik
if __name__ == "__main__":
         # Uruchom testy
     unittest.main()