from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ..utils.input_utils import random_delay
from config.selectors import FB_SELECTORS
import logging
import time

def login_to_facebook(driver, email, password):
    """Handle Facebook login process"""
    logger = logging.getLogger('facebook_scraper')
    
    try:
        logger.info("Attempting Facebook login")
        driver.get("https://www.facebook.com")
        random_delay(3, 5)
        
        # Enter email
        email_input = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, FB_SELECTORS['email']))
        )
        email_input.clear()
        for char in email:
            email_input.send_keys(char)
            time.sleep(0.1)
        
        # Enter password
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, FB_SELECTORS['password']))
        )
        password_input.clear()
        for char in password:
            password_input.send_keys(char)
            time.sleep(0.1)
        
        # Click login
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, FB_SELECTORS['login_button']))
        )
        login_button.click()
        
        # Wait for login completion
        WebDriverWait(driver, 20).until(
            EC.any_of(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Facebook"]')),
                EC.presence_of_element_located((By.XPATH, '//div[@role="navigation"]'))
            )
        )
        
        logger.info("Login successful")
        return True
        
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        return False

def scrape_marketplace_term(driver, search_term):
    """Search and scrape a single term from Marketplace"""
    logger = logging.getLogger('facebook_scraper')
    results = []
    
    try:
        # Navigate to Marketplace with the search term properly formatted
        # Reemplazar espacios con %20 o + para la URL
        formatted_term = search_term.replace(' ', '%20')
        search_url = f"https://www.facebook.com/marketplace/lima/search?query={formatted_term}"
        driver.get(search_url)
        random_delay(3, 5)
        
        # Wait for results or "no results" message
        try:
            WebDriverWait(driver, 15).until(
                EC.any_of(
                    EC.presence_of_element_located((By.XPATH, FB_SELECTORS['product_items'])),
                    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'No se encontrar')]"))
                )
            )
        except Exception as e:
            logger.error(f"Error waiting for results: {str(e)}")
            return results
            
        # Rest of the code stays the same...
        
    except Exception as e:
        logger.error(f"Error searching for {search_term}: {str(e)}")
        return results

def scrape_facebook_marketplace(driver, search_terms, email, password):
    """Main function to handle all Facebook Marketplace scraping"""
    logger = logging.getLogger('facebook_scraper')
    all_results = []

    try:
        # Login once at the beginning
        if not login_to_facebook(driver, email, password):
            logger.error("Failed to login to Facebook")
            return all_results
            
        # Process each search term separately
        for term in search_terms:
            logger.info(f"Searching for: {term}")
            results = scrape_marketplace_term(driver, term)
            all_results.extend(results)
            random_delay(2, 3)
            
        return all_results
        
    except Exception as e:
        logger.error(f"Error in Facebook scraping: {str(e)}")
        return all_results