#!/usr/bin/env python

from baseObject import Base

class PageA(Base):

    def __init__(self, driver, foo, bar):
        super(PageA, self).__init__(driver)
        self.foo = foo
        self.bar = bar

# Function created from helper methods below

def enter_text_and_submit(self):
        self.enter_test_on_pageA()
        self.submit_button_on_PageA()

# Helper methods

    def enter_text_on_pageA(self,locator):
        self.enter_text("PAGE_A_TEXTFIELD") # <- locators there are no css ids or xpaths in pageobjects

    def submit_button_on_pageA(self, locator):
        self.click_button("PAGE_A_BUTTON") # <- locators - there are no css ids or xpaths in pageobjects. 

