from .base_page import BasePage
from locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_form(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert self.browser.find_element(*MainPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert self.browser.find_element(*MainPageLocators.REG_FORM), "Reg form not found"