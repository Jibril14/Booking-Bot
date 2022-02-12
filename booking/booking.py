import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# each instance inherit from webdriver.Chrome
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Chromedriver\chromedriver", tear_down=False):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        # enable chromedriver keep browser context
        self.tear_down = tear_down
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        # instanciate webdriver.Chrome along & pass in chrome option
        super(Booking, self).__init__(options=chrome_options)
        self.implicitly_wait(15)
        self.maximize_window()

    # exit the web browser on tear down
    def __exit__(self, exe_type, exc_val, exc_tb):
        if self.tear_down:
            self.quit()
            
    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR,
                                                'button[data-tooltip-text="Choose your currency"]'
                                                )
        currency_element.click()
        selected_currency = self.find_element(By.CSS_SELECTOR,
                                                f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
                                                )
        selected_currency.click()

    def select_place_to_go(self, place):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place)
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

   