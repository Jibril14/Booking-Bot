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
    

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR,
                                              f'td[data-date="{check_in_date}"]'    
                                            )
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR,
                                                f'td[data-date="{check_out_date}"]'
                                             )
        check_out_element.click()
   
    def select_adults(self, num=1):
        adult_element = self.find_element(By.ID, 'xp__guests__toggle')
        adult_element.click()

        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR,
                                                        'button[aria-label="Decrease number of Adults"]'
                                                        )
            decrease_adults_element.click()
            # if the default adult number is more than one, keep decreasing it until it's one
            adults_value_element = self.find_element(By.ID, "group_adults")
            current_adults_value = adults_value_element.get_attribute('value')  # return current adult number
            if int(current_adults_value) == 1:
                break

        increase_adults_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
        for i in range(num - 1):
            increase_adults_element.click()
        
    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()
   