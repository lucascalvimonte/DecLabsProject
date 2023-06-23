from .base_page import BasePage


class HoustonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # Llamada al método __init__ de la clase base
        self.driver = driver
        self.btn_schedule_free_consultation = "//*[@class='button transparent-button launch-modal-schedule-consultation']"
        self.popup_form = "//*[@id='wpforms-form-876']"
        self.btn_close_form = "(//div[@class='btn-close-modal'])[2]"

    @staticmethod
    def get_base_url():
        return "https://inhouse.decemberlabs.com/locations/houston/"

    def validate_houston_page_title(self):
        expected_title = 'Houston Web & App Developers | December Labs'
        return self.validate_title(expected_title)

    def validate_url_houston(self):
        self.validate_url('https://inhouse.decemberlabs.com/locations/houston/')

    def open_form(self):
        self.click_element(self.btn_schedule_free_consultation)
        self.find_element(self.popup_form)

    def close_form(self):
        self.click_element(self.btn_close_form)
        self.element_is_not_visible(self.popup_form)

