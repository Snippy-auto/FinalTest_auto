from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login'missing from current link "

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_AUTH), "Form auth is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FORM_REG), "Form reg is not present"

    def register_new_user(self, email, password):
        email1 = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
        email1.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_REG1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_REG2)
        password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        button.click()

