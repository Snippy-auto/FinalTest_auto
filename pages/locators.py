from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    FORM_REG = (By.CSS_SELECTOR, "#register_form")
    FORM_AUTH = (By.CSS_SELECTOR, "#login_form")
    EMAIL_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REG1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REG2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REG = (By.NAME, "registration_submit")

class ProductPageLocators():
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
	NAME_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
	PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main > .price_color")
	PRICE_PRODUCT_IN_ALERT = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn-default")
    GOODS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-6")
    YOUR_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
