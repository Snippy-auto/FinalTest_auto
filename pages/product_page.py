from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
import math
from .basket_page import BasketPage


class ProductPage(BasePage):

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "нет кнопки корзина"

    def should_be_button_add_to_basket_click(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def should_be_correct_name_product_on_massage_and_link(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text == self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_ALERT).text, "The name of the product in the basket does not match the real price of the product!"

    def should_be_correct_prace_product_on_massage_and_link(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text == self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_ALERT).text, "The price of the product in the basket does not match the real price of the product!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_PRODUCT_IN_ALERT), \
            "Success message is presented, but should not be"

    def should_element_dissappears(self):
        assert self.is_dissappeared(*ProductPageLocators.NAME_PRODUCT_IN_ALERT), \
           "Success message is presented, but should not be"
