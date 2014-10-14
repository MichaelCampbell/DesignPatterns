#!/usr/bin/env python

from pageObjects.pageObjectA import PageA 
from resources.config import Config

from selenium import webdriver

from unittest import TestCase

class TestCaseBase(TestCase):

# The setup method whould kick off before everytest
    def setUp(self):
        self.setup = Config()
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', self.setup.config())
        self.pageA = PageA(self.driver)
        pass

# The tear down method should kickoff everytime at the end of your method
    def tearDown(self):
        self.driver.quit()
        pass

