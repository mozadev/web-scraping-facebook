from src.browser.setup import setup_chrome_driver
from src.scrapers.oplogin_scraper import login_to_oplogin
from src.utils.logging_utils import setup_logging
from dotenv import load_dotenv
import os

def main():
   
    load_dotenv()
    logger = setup_logging()
    driver = None
    
  
    user = os.getenv('OPLOGIN_USER')
    password = os.getenv('OPLOGIN_PASSWORD')
    
    if not user or not password:
        logger.error(" Credenciales de Oplogin no fueron encontradas .env file")
        return
    
    try:
        logger.info("Empezando Oplogin scraping process")
        driver = setup_chrome_driver()
        
        login_to_oplogin(driver,user,password)
        
       
        
    except Exception as e:
        logger.error(f"No se pudo logear {str(e)}")
        
    finally:
        if driver:
            driver.quit()
            logger.info("Browser closed")

if __name__ == "__main__":
    main()