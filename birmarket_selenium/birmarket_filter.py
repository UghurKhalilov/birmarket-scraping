from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from birmarket_selenium.birmarket import Birmarket
import time


class BirmarketFilter(Birmarket):
    def get_meiset(self):
        wait = WebDriverWait(self, 10)
        try:
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.mr-2.whitespace-nowrap'))
            ).click()
            print("Mehsul katalogu found")
            time.sleep(3)
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/categories/106-meishet-texnikasi"]'))
            ).click()
            print("Meiset texnikasi found")
            time.sleep(2)
        except:
            print("not found")

    def get_iri_meiset(self):
        time.sleep(2)
        wait = WebDriverWait(self, 10)
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/categories/107-iri-meishet-texnikasi"]'))
        ).click()
        print("Iri meiset texnikasi found")
