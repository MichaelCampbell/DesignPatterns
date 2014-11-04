require 'selenium-webdriver'
require_relative '../pageObjects/examplePage'

def setup
  @driver = Selenium::WebDriver.for :firefox
  ENV['base_url'] = 'http://www.example.com'
end

def teardown
  @driver.quit
end

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
