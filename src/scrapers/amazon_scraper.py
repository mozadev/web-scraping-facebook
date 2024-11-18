from selenium.webdriver.common.by import By
from .utils import wait_for_element, clean_price
from ..utils.input_utils import random_delay
from config.selectors import AMAZON_SELECTORS
import logging

def scrape_amazon(driver, search_term):
   
    logger = logging.getLogger('amazon_scraper')
    results = []
    
    try:
        # Navigate to Amazon
        driver.get("https://www.amazon.com")
        random_delay()
        
        # Search for products
        search_box = wait_for_element(
            driver, 
            By.CSS_SELECTOR, 
            AMAZON_SELECTORS['search_box']
        )
        search_box.send_keys(search_term)
        
        search_button = wait_for_element(
            driver,
            By.CSS_SELECTOR,
            AMAZON_SELECTORS['search_button']
        )
        search_button.click()
        random_delay()
        
        # Get product list
        products = driver.find_elements(
            By.CSS_SELECTOR,
            AMAZON_SELECTORS['product_list']
        )
        
        # Extract product data
        for product in products[:10]:
            try:
                title = product.find_element(
                    By.CSS_SELECTOR,
                    AMAZON_SELECTORS['product_title']
                ).text
                
                price = product.find_element(
                    By.CSS_SELECTOR,
                    AMAZON_SELECTORS['product_price']
                ).text
                
                results.append({
                    'source': 'Amazon',
                    'title': title.strip(),
                    'price': clean_price(price),
                    'search_term': search_term
                })
                
            except Exception as e:
                logger.error(f"Error extracting product: {str(e)}")
                
        return results
        
    except Exception as e:
        logger.error(f"Error scraping Amazon: {str(e)}")
        return results