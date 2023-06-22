from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def find_element_by_id(self, element):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, element)))

    def find_element_by_xpath(self, element):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))

    def find_elements(self, elements):
        for element_key in elements:
            element_id = elements[element_key]
            element = self.find_element_by_id(element_id)
            self.visible_element(element)

    def visible_element(self, element):
        return element.is_displayed()

    def scroll_down(self):
        # Hacer scroll down hasta el final de la página
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def element_is_not_visible_by_xpath(self, element):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, element)))