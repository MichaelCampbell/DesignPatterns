# imports baseObject
require './baseObject'

# inherits from base
class PageA < Base
  
  def initialize(driver)
    super
    visit
    verify_page
  end
  
end
