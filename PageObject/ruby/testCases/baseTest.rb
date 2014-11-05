# imports selenium
require 'selenium-webdriver'
# imports pageObject examplePage
require_relative '../pageObjects/examplePage'

# occurs before every test
def setup
  @driver = Selenium::WebDriver.for :firefox
  ENV['base_url'] = 'http://www.example.com'
end

# occurs at the end of every test
def teardown
  @driver.quit
end

# calls the setup and teardown methods, then the run block below
def run
  setup
  yield
  teardown
end

# will run block during yield
run {
  example = ExampleA.new(@driver)
  example.send_text_to_pageA()
  send_text_to_pageB()
  # assertions 
}
