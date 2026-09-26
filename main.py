from birmarket_selenium.birmarket_filter import BirmarketFilter
from birmarket_selenium.get_all_result import get_all_result
import time

with BirmarketFilter() as b:
    b.get_first_page()
    b.get_meiset()
    b.get_iri_meiset()
    time.sleep(5)
    
    data = get_all_result(b)
    print(len(data))
    print(data[0])
    
    input("Press click to close")