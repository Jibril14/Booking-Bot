# information grab the needs to be report

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, first_hotel_box: WebElement): # typeof driver = WebElement
        self.first_hotel_box = first_hotel_box
        self.box_elements = self.all_box_elements()
    
    def all_box_elements(self):
        return self.first_hotel_box.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    def hotel_deals(self):
        data_to_display = []
        for box_element in self.box_elements:
            hotel_name = box_element.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute(
                'innerHTML').strip()
            hotel_price = deal_box.find_element(By.CSS_SELECTOR, 'span[class="fcab3ed991 bd73d13072"]').get_attribute(
                'innerHTML').strip()
            hotel_rating = deal_box.find_element(By.CSS_SELECTOR, 'div[class="b5cd09854e d10a6220b4"]').get_attribute(
                'innerHTML').strip()
            data_to_display.append(
                [hotel_name, hotel_price, hotel_rating]
            )
        return data_to_display
        