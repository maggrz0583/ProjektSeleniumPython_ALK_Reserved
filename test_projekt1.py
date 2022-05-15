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
        self.driver.quit()

    def testInvalidEmail(self):
        pass
#Jeśli uruchamiam ten plik
if __name__== "__main__":
#Uruchom testy
    unittest.main()
