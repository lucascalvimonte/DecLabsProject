from .base_page import BasePage


class DecemberLabsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver) # Llamada al método __init__ de la clase base
        self.driver = driver
        self.lnk_houston = "//*[@href='/locations/houston']"
        self.elements = {
            'btn_about': "//*[@id='menu-item-839']",
            'btn_services': "//*[@id='menu-item-842']",
            'btn_our_work': "//*[@id='menu-item-841']",
            'btn_blog': "//*[@id='menu-item-840']",
            'btn_faq': "//*[@id='menu-item-843']",
            'btn_careers': "//*[@id='menu-item-838']",
            'btn_get_in_touch': "//*[@id='menu-item-846']"
        }

    @staticmethod
    def get_base_url():
        return "https://inhouse.decemberlabs.com/"

    def navigate_to_december_labs_page(self):
        self.driver.get(self.get_base_url())

    def validate_december_labs_page_title(self):
        expected_title = 'December Labs: UX/UI Design and Mobile App & Web Development'
        return self.validate_title(expected_title)

    def validate_menu_elements_visibility(self):
        self.find_elements(self.elements)

    def navigate_to_houston_page(self):
        self.scroll_down()
        self.click_element(self.lnk_houston)
