from selenium.webdriver.common.by import By
from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, '.basket-items'), "Корзина не пуста, хотя должна быть"

    def should_have_empty_basket_text(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#content_inner > p"), "Нет сообщения о пустой корзине"
