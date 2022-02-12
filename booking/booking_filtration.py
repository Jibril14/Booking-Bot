# This flie is responsible for applying filter to the properties found
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class  BookingFiltration: 
    def __init__(self, driver: WebDriver):  # typeof driver = WebDriver
        self.driver = driver

    def apply_star_rating(self, *stars):
        self.driver.implicitly_wait(15)
        filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        filtration_box_children = filteration_box.find_elements(By.CSS_SELECTOR, "*")
        
        # choose multiple star ratings
        for star in stars:
            # go through each child of the html elements and click a match rating
            for child_el in filtration_box_children:
                if str(child_el.get_attribute('innerHTML')).strip() == f"{star} stars":
                    child_el.click()
                   
