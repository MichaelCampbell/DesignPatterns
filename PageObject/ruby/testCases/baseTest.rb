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

