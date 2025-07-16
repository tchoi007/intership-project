from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SecondaryPage(Page):
    URL_PART = "/secondary-listings"

    FILTERS_BUTTON = (By.CSS_SELECTOR, 'div[wized="openFiltersWindow"]')
    WANT_TO_SELL_SWITCH = (By.CSS_SELECTOR, 'div[wized="ListingTypeSell"]')
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, 'a[wized="applyFilterButtonMLS"]')
    FOR_SALE_TAGS = (By.CSS_SELECTOR, 'div[wized="saleTagBoxMLS"]')
    LISTING_CARDS = (By.CSS_SELECTOR, 'div[wized="listingCardMLS"]')

    def verify_page_loaded(self):
        self.wait_for_url_contains(self.URL_PART)
        sleep(5)

    def click_filters(self):
        self.click_element(*self.FILTERS_BUTTON)


    def apply_filter(self, filter_name):
        if filter_name.lower() == "want to sell":
            self.click_element(*self.WANT_TO_SELL_SWITCH)


    def click_apply_filter(self):
        self.wait.until(
            EC.visibility_of_element_located(self.APPLY_FILTER_BUTTON),
            message="Apply Filter button is not visible"
        )

        element = self.driver.find_element(*self.APPLY_FILTER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

        sleep(5)

    def all_cards_have_tag(self, tag_text):
        cards = self.find_elements(*self.LISTING_CARDS)
        for card in cards:
            tag_elements = card.find_elements(*self.FOR_SALE_TAGS)
            if all(tag_text not in el.text for el in tag_elements):
                return False
        return True
