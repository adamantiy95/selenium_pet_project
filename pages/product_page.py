from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")

    def add_product_to_basket(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.ADD_TO_BASKET_BUTTON)
        )
        button.click()

    def get_product_name(self):  
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        )
        return element.text

    def get_product_price(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.PRODUCT_PRICE)
        )
        return element.text

    def get_success_message(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )
        return element.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*self.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
    
    def get_basket_total(self):
        return self.browser.find_element(*self.BASKET_TOTAL).text

    def should_be_success_message_with_product_name(self):
        assert self.get_product_name() == self.get_success_message(), \
            "Product name in success message is incorrect"

    def should_be_correct_basket_total(self):
        assert self.get_product_price() == self.get_basket_total(), \
            "Basket total is incorrect"
