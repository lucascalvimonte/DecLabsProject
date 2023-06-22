base_url = "https://inhouse.decemberlabs.com/"

class DecemberLabsPage:

    def __init__(self, driver):
        self.driver = driver
        self.lnk_houston = "//*[@href='/locations/houston']"
        self.elements = {
            'btn_about': "menu-item-839",
            'btn_services': "menu-item-842",
            'btn_our_work': "menu-item-841",
            'btn_blog': "menu-item-840",
            'btn_faq': "menu-item-843",
            'btn_careers': "menu-item-838",
            'btn_get_in_touch': "menu-item-846"
        }

    @staticmethod
    def get_base_url():
        return base_url