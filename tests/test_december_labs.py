import pytest
from selenium import webdriver
from pages.houston_page import HoustonPage
from pages.december_labs_page import DecemberLabsPage
from pages.base_page import BasePage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestDecemberLabs:

    def test_validate_web(self):
        self.base_page = BasePage(self.driver)
        self.december_lab_page = DecemberLabsPage(self.driver)
        self.driver.get(DecemberLabsPage.get_base_url())
        expected_title = 'December Labs: UX/UI Design and Mobile App & Web Development'
        current_title = self.base_page.get_page_title()
        assert current_title == expected_title
        self.base_page.find_elements(self.december_lab_page.elements)

    def test_navigate_pages(self):
        self.driver.get(DecemberLabsPage.get_base_url())
        self.base_page = BasePage(self.driver)
        self.december_lab_page = DecemberLabsPage(self.driver)
        self.base_page.scroll_down()
        self.base_page.find_element_by_xpath(self.december_lab_page.lnk_houston).click()
        title_expected = 'Houston Web & App Developers | December Labs'
        title_qurrent = self.base_page.get_page_title()
        assert title_qurrent == title_expected
        current_url = self.driver.current_url
        expected_url = "https://inhouse.decemberlabs.com/locations/houston/"
        assert current_url == expected_url, f"La URL actual ({current_url}) no coincide con la URL esperada ({expected_url})"
        self.houston_page = HoustonPage(self.driver)
        self.base_page.find_element_by_xpath(self.houston_page.btn_schedule_free_consultation).click()
        self.base_page.find_element_by_id(self.houston_page.popup_form)
        self.base_page.find_element_by_xpath(self.houston_page.btn_close_form).click()
        self.base_page.element_is_not_visible_by_xpath(self.houston_page.popup_form)
