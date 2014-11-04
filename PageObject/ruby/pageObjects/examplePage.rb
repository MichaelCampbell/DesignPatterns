# imports baseObject
require_relative './baseObject'
require_relative '../resources/locators'

# inherits from base
class ExampleA < Base
  
  def initialize(driver)
    super
    visit
  end

  def send_text_to_pageA()
    send_text_to_page(locator["page A button"], locator["page A text field"], 'example text a')
  end 

  def send_text_to_pageB()
    send_text_to_page(locator["page B button"], locator["page A text field"], 'example text b')
  end

  def send_text_to_page(button, textfield, input)
    click_on(button)
    type(textfield, input)
  end
  
end
