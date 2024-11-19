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
         # 1. Guardar estado inicial
        original_window = driver.current_window_handle
        initial_windows = set(driver.window_handles)
        logger.info(f"Ventanas iniciales: {len(initial_windows)}")
        
        logger.info("Iniciando proceso de login en Oplogin")
        
        # Navegar a la página
        driver.get('http://172.19.216.21/oplogin')
        random_delay(2, 3)  # Reducido el delay ya que la página es interna
        
        # Diccionario de elementos y sus IDs
        elements = {
            'username': ('username', user),
            'password': ('password', password),
            'submit': ('btnLoginSubmit', None)
        }
        
        # Manejar inputs y submit
        for element_name, (element_id, value) in elements.items():
            try:
                # Esperar y encontrar elemento
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, element_id))
                )
                
                # Si es input, ingresar valor
                if value is not None:
                    element.clear()
                    for char in value:
                        element.send_keys(char)
                        time.sleep(0.05)  # Reducido el delay entre caracteres
                # Si es submit, hacer click
                else:
                    element.click()
                    
                logger.info(f"Completado: {element_name}")
                
            except Exception as e:
                logger.error(f"Error en elemento {element_name}: {str(e)}")
                raise
        
        # Esperar y cambiar a nueva ventana
        logger.info("Esperando nueva ventana...")
        WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)
        
        # Cambiar a la nueva ventana
        new_window = [window for window in driver.window_handles 
                     if window != original_window][0]
        driver.switch_to.window(new_window)
        
       
        logger.info("Login completado exitosamente")
        return True
        
    except Exception as e:
        logger.error(f"Error durante el proceso de login: {str(e)}")
        return False
    

    

