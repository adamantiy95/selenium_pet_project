from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def add_to_basket(self):
        self.browser.find_element(*self.ADD_TO_BASKET).click()

    def should_be_success_message(self, expected_name):
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert expected_name == success_message, \
        f"Ожидаемое название товара '{expected_name}' в успешном сообщении, но получено '{success_message}'"

    def should_be_correct_basket_total(self, expected_price):
        basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
        assert expected_price == basket_total, \
        f"Ожидаемая итоговая сумма '{expected_price}', но получено '{basket_total}'"
