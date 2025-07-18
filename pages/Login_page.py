from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
class LoginPage(Page):
    URL = "https://soft.reelly.io"

    EMAIL_INPUT = (By.CSS_SELECTOR, "#email-2")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#field")
    CONTINUE_BTN = (By.CSS_SELECTOR, 'a[wized="loginButton"]')

    def open(self):
        self.driver.get(self.URL)

        sleep (3)

    def login(self, email, password):
        self.wait_for_element(*self.EMAIL_INPUT)
        self.input_text(email, *self.EMAIL_INPUT)

        self.wait_for_element(*self.PASSWORD_INPUT)
        self.input_text(password, *self.PASSWORD_INPUT)

        self.wait_for_element_click(*self.CONTINUE_BTN)
        self.click_element(*self.CONTINUE_BTN)


