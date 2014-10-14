#!/usr/bin/env python

from locators import locators

#Base class to be imported into all classes

class Base(object):
# Common base functions that are shared across all objects

    def _init_(self, driver):
        self.driver = driver
    
    def current_locator(self, locator):
        return locators[locator]

    def find(self, locator):
        return self.driver.find_element_by_xpath(self.current_locator(locator))

    def enter_text(self, locator, text):
        self.find(self.current_locator(locator).send_keys(text))

    def click_button(self, locator):
        self.find(self.current_locator(locator)).click()

