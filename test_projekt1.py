#Import bibliotek
from selenium import webdriver

import unittest

class TestRegistration(unittest.TestCase):
    def setUp(self):
        ##przygotowanie testu
        #otwarta strona https://www.douglas.pl/pl/login
    def tearDown(self):
        pass
    def testInvalidEmail(self):
        pass

    if __name__== "__main__":

       unittest.main()
