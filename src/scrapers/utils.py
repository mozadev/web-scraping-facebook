from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..utils.input_utils import random_delay

def wait_for_element(driver, by, selector, timeout=10):
   
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, selector))
    )

def safe_click(driver, element):
   
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)

def clean_price(price_text):
    
    try:
        return float(''.join(filter(str.isdigit, price_text)))
    except:
        return None