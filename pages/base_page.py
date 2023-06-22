from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def validate_title(self, expected_title):
        assert self.get_page_title() == expected_title

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))

    def click_element(self, locator):
        return self.find_element(locator).click()

    def validate_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"La URL actual ({current_url}) no coincide con la URL esperada ({expected_url})"

    def find_elements(self, elements):
        for element_key in elements:
            locator = elements[element_key]
            element = self.find_element(locator)
            self.visible_element(element)

    @staticmethod
    def visible_element(element):
        return element.is_displayed()

    def scroll_down(self):
        # Hacer scroll down hasta el final de la página
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def element_is_not_visible(self, element):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, element)))