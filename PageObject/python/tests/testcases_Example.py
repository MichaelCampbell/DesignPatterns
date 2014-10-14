#!/usr/bin/env python

# The only required module to import should be the TestCaseBase
# All other modules should have already been imported into TestCaseBase if needed
from testcases_Base import TestCaseBase

class TestCaseExample(TestCaseBase):

# Test examples using the page objects functions imported into TestCaseBas

    def test_1_example(self):
        self.pageA.enter_text_and_submit()

    def test_2_example(self):
        self.pageA.enter_text_on_pageA()
        self.pageA.submit_button_on_pageA()

# etc... additional test cases as need.

