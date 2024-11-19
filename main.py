from src.browser.setup import setup_chrome_driver
from src.scrapers.oplogin_scraper import login_to_oplogin
from src.utils.logging_utils import setup_logging
from dotenv import load_dotenv
import os
import time

def main():
    # Configurar logging primero
    logger = setup_logging()
    
    # Cargar variables de entorno
    load_dotenv()
    driver = None
    
    try:
        # Verificar credenciales
        credentials = {
            'user': os.getenv('OPLOGIN_USER'),
            'password': os.getenv('OPLOGIN_PASSWORD')
        }
        
        # Logging más detallado
        logger.info("Iniciando proceso con configuración:")
        logger.info(f"Usuario configurado: {'Sí' if credentials['user'] else 'No'}")
        logger.info(f"Contraseña configurada: {'Sí' if credentials['password'] else 'No'}")
        
        if not all(credentials.values()):
            logger.error("Credenciales incompletas en .env")
            return
            
        logger.info("Iniciando proceso de scraping")
        
        # Configurar y obtener el driver
        driver = setup_chrome_driver()
        
        if not driver:
            logger.error("No se pudo inicializar el driver")
            return
            
        # Intento de login con manejo explícito de ventana
        if login_to_oplogin(driver, **credentials):
            logger.info("Sesión iniciada correctamente")
            
            # Verificar que estamos en la ventana correcta
            try:
                current_url = driver.current_url
                logger.info(f"URL actual: {current_url}")
                
                # Mantener ventana abierta
                logger.info("Ventana mantenida abierta. Presiona Enter para cerrar...")
                input() # Esperar input del usuario
                
            except Exception as e:
                logger.error(f"Error verificando ventana: {str(e)}")
        else:
            logger.error("No se pudo iniciar sesión")
            
    except Exception as e:
        logger.error(f"Error en proceso principal: {str(e)}")
        
    finally:
        if driver:
            try:
                logger.info("Cerrando navegador...")
                driver.quit()
                logger.info("Navegador cerrado correctamente")
            except Exception as e:
                logger.error(f"Error cerrando navegador: {str(e)}")

if __name__ == "__main__":
    main()