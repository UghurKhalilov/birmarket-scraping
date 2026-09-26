from selenium import webdriver
from dotenv import load_dotenv
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()


class Birmarket(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        super(Birmarket, self).__init__(options=options)
        self.base_url = os.getenv("BASE_URL")
        self.implicitly_wait(20)
        self.maximize_window()

    def get_first_page(self):
        self.get(self.base_url)
        time.sleep(3)
        self.select_city()

    def select_city(self):
        WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-info="select-city-item-selected"]'))
        ).click()

    def subscription_reject(self):
        try:
            WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Close"]'))
            ).click()
            print("notification rejected")
        except:
            print("no notification")

   

    



    