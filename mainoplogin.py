from src.browser.setup import setup_chrome_driver
from src.scrapers.oplogin_scrapercopy import scrape_oplogin_page
from src.utils.logging_utils import setup_logging
from dotenv import load_dotenv
import os
import time

def main():

    load_dotenv()
    logger = setup_logging()
    driver = None

    user = os.getenv('OPLOGIN_USER')
    password = os.getenv('OPLOGIN_PASSWORD')

    if not user or not password:
        logger.error("Oplogin credenciales no encontradas .env file")
        return
        
    try:
        logger.info('Empezando scraping de Oplogin')
        driver = setup_chrome_driver()
        scrape_oplogin_page(driver, user, password)

        while True:
            try:
                driver.current_url
                time.sleep(1)
            except:
                break
        
    except Exception as e:
        logger.error(f"Error en scraping de Oplogin: {str(e)}")

    finally:
        if driver:
            driver.quit()
            logger.info("OPLOGIN CERRADO")

if __name__ == "__main__":
    main()