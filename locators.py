from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REG_FORM = (By.CLASS_NAME, "register_form")