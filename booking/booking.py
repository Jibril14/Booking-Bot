import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# each instance inherit from webdriver.Chrome
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Chromedriver\chromedriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        # enable chromedriver keep browser context
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        # instanciate webdriver.Chrome along & pass in chrome option
        super(Booking, self).__init__(options=chrome_options)
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)
