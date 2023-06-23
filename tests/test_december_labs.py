import pytest
from selenium import webdriver
from pages.houston_page import HoustonPage
from pages.december_labs_page import DecemberLabsPage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    dec_labs_page = DecemberLabsPage(driver)
    request.cls.dec_labs_page = dec_labs_page
    houston_page = HoustonPage(driver)
    request.cls.houston_page = houston_page
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestDecemberLabs:

    def test_navigate_to_dec_labs(self):
        self.dec_labs_page.navigate_to_december_labs_page()

    def test_validate_title_dec_labs(self):
        self.dec_labs_page.validate_december_labs_page_title()

    def test_validate_menu_dec_labs(self):
        self.dec_labs_page.validate_menu_elements_visibility()

    def test_navigate_to_houston(self):
        self.dec_labs_page.navigate_to_houston_page()

    def test_houston_page_title(self):
        self.houston_page.validate_houston_page_title()

    def test_validate_url_houston(self):
        self.houston_page.validate_url_houston()

    def test_open_form_popup(self):
        self.houston_page.open_form()

    def test_close_form_popup(self):
        self.houston_page.close_form()
