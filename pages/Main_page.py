from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SECONDARY_MENU = (By.XPATH, '//button[normalize-space(text())="Secondary"]')
    off_plan_btn = (By.XPATH, '//a[.//div[@class="menu-text" and normalize-space(text())="Off-plan"]]')



    def click_secondary_option(self):
        self.click_element(*self.SECONDARY_MENU)

    # def verify_page_loaded(self):
    #     self.wait_for_url_contains('main')

    def click_off_plan(self):
        self.click_element(*self.off_plan_btn)
