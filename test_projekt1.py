#Import bibliotek
from selenium import webdriver
import unittest

class TestRegistration(unittest.TestCase):
    def setUp(self):
        #Przygotowanie testu
        #1. Otwarta strona https://www.douglas.pl/pl
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.douglas.pl/pl")

    def tearDown(self):
        # Zakończenie testu
        self.driver.quit(15)

    def testInvalidEmail(self):
        #1.Kliknij utwórz konto - otwiera się strona rejestracji
        driver.find.element(By.)
#Jeśli uruchamiam ten plik
if __name__== "__main__":
#Uruchom testy
    unittest.main()
