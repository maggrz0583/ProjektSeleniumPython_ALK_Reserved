#Import bibliotek
from selenium import webdriver
import unittest

class TestRegistration(unittest.TestCase):
    def setUp(self):
        pass
        #przygotowanie testu
        #otwarta strona https://www.douglas.pl/pl/login
    def tearDown(self):
        pass
    def testInvalidEmail(self):
        pass
#Jeśli uruchamiam ten plik
if __name__== "__main__":
#Uruchom testy
    unittest.main()
