from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def should_be_no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET)
    
    def should_be_basket_is_empty(self):
    	assert self.browser.find_element(*BasketPageLocators.YOUR_BASKET_EMPTY).text == "Your basket is empty. " \ "Continue shopping"
