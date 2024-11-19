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
        
        logger.info(" Intentando login")
        driver.get('http://172.19.216.21/oplogin')
        random_delay(3, 5)
 
        user_input = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ['email']))
        )
        user_input.clear()
        for char in user:
            user_input.send_keys(char)
            time.sleep(0.1)
        

        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, OPLOGIN_SELECTORS['password']))
        )
        password_input.clear()
        for char in password:
            password_input.send_keys(char)
            time.sleep(0.1)
        
       
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, OPLOGIN_SELECTORS['login_button']))
        )
        login_button.click()
        
        
        logger.info("Login Exitoso")
        return True
        
    except Exception as e:
        logger.error(f"Login fallido: {str(e)}")
        return False

