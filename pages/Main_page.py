from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    SECONDARY_MENU = (By.XPATH, '//a[div[text()="Secondary"]]')

    def click_secondary_option(self):
        self.click_element(*self.SECONDARY_MENU)

    # def verify_page_loaded(self):
    #     self.wait_for_url_contains('main')
