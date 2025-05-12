from pages.product_page import ProductPage
import math
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


# def test_guest_can_add_product_to_basket(browser):
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket()
#    page.should_be_success_message_with_product_name()
#    page.should_be_correct_basket_total()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_disappear()
