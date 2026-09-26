from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import pandas as pd

def get_all_result(driver):
    time.sleep(3)
    while True:
        try:
            more_btn = driver.find_element(By.CSS_SELECTOR, 'button.MPProductsShowMoreButton')
            more_btn.click()
            time.sleep(2)
            print("Daha çox yükləndi...")
        except:
            print("Hamısı yükləndi!")
            break

    soup = BeautifulSoup(driver.page_source, 'lxml')
    products = soup.find_all('div', attrs={'data-product-id': True})
    print(f"Ümumi məhsul: {len(products)}")

    all_data = []
    for product in products:
        try:
            name = product.find('a', attrs={'aria-label': True})['aria-label']
            new_price = product.find(attrs={'data-info': 'item-desc-price-new'})
            new_price = new_price.text.strip() if new_price else None
            old_price = product.find(attrs={'data-info': 'item-desc-price-old'})
            old_price = old_price.text.strip() if old_price else None
            rating = product.find('span', class_='vue-star-rating-rating-text')
            rating = rating.text.strip() if rating else 'reytinq yoxdur'
            discount = product.find(class_='MPProductItem-Discount')
            discount = discount.text.strip() if discount else 'endirim yoxdur'

            all_data.append({
                "name": name,
                "new_price": new_price,
                "old_price": old_price,
                "rating": rating,
                "discount": discount
            })
        except:
            continue

    pd.DataFrame(all_data).to_csv('products.csv', index=False)
    print(f"CSV-ə yazıldı: {len(all_data)} məhsul")

    return all_data