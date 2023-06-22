base_url = "https://inhouse.decemberlabs.com/locations/houston/"


class HoustonPage:

    def __init__(self, driver):
        self.driver = driver
        self.btn_schedule_free_consultation = "//*[@class='button transparent-button launch-modal-schedule-consultation']"
        self.popup_form = "wpforms-form-876"
        self.btn_close_form = "(//div[@class='btn-close-modal'])[2]"

    @staticmethod
    def get_base_url():
        return base_url
