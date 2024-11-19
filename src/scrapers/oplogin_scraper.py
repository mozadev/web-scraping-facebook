from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ..utils.input_utils import random_delay
from config.selectors import OPLOGIN_SELECTORS
import logging
import time

def login_to_oplogin(driver, user, password):

    logger = logging.getLogger('oplogin_scraper')
    
    try:
        original_window = driver.current_window_handle
        initial_windows = set(driver.window_handles)
        logger.info(f"Ventanas iniciales: {len(initial_windows)}")
        
        logger.info("Iniciando proceso de login en Oplogin")
        
        driver.get('http://172.19.216.21/oplogin')
        random_delay(2, 3)  
        
        elements = {
            'username': ('username', user),
            'password': ('password', password),
            'submit': ('btnLoginSubmit', None)
        }
        
        for element_name, (element_id, value) in elements.items():
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, element_id))
                )
                
                if value is not None:
                    element.clear()
                    for char in value:
                        element.send_keys(char)
                        time.sleep(0.05)  
                
                else:
                    element.click()
                    
                logger.info(f"Completado: {element_name}")
                
            except Exception as e:
                logger.error(f"Error en elemento {element_name}: {str(e)}")
                raise
        
        logger.info("Esperando nueva ventana...")
        WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)
        
        new_window = [window for window in driver.window_handles 
                     if window != original_window][0]
        driver.switch_to.window(new_window)
        
       
        logger.info("Login completado exitosamente")
        return True
        
    except Exception as e:
        logger.error(f"Error durante el proceso de login: {str(e)}")
        return False
    

def scrape_oplogin_term(driver, search_term):
    logger=logging.getLogger('Oplogin Scrapper')
    results = []

    return results

def scrape_oplogin_page(driver, user, password):
    logger= logging.getLogger('Oplogin_scrapper')
    all_results = []

    try:
        if not login_to_oplogin(driver, user, password):
            logger.error("Falló login a Oplogin ")
            return all_results
        
    except Exception as e :
        logger.error(f"Error in Oplogin scraping: {str(e)}")
        return all_results

    

