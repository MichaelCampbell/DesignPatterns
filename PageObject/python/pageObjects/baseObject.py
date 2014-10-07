class Base(object):
    
    def _init_(self, wd):
        self.wd = wd
    
    def find(self, locator):
        return self.wd.find_element_by_xpath(self.current_locator(locator)

