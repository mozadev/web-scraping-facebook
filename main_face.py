from src.browser.setup import setup_chrome_driver
from src.scrapers.facebook_scraper import scrape_facebook_marketplace
from src.utils.logging_utils import setup_logging
from dotenv import load_dotenv
import os
def main():
    # Setup
    load_dotenv()
    logger = setup_logging()
    driver = None
    
    # Get credentials
    email = os.getenv('FACEBOOK_EMAIL')
    password = os.getenv('FACEBOOK_PASSWORD')
    
    if not email or not password:
        logger.error("Facebook credentials not found in .env file")
        return
    
    try:
        logger.info("Starting Facebook scraping process")
        driver = setup_chrome_driver()
        
        # Define search terms - cada término por separado
        search_terms = [
            "laptop",         # Buscar laptops
            "smartphone",     # Luego smartphones
            "headphones"      # Finalmente headphones
        ]
        
        # Ejecutar la búsqueda
        results = scrape_facebook_marketplace(
            driver,
            search_terms,
            email,
            password
        )
        
        logger.info(f"Total products found: {len(results)}")
        
    except Exception as e:
        logger.error(f"Error in main process: {str(e)}")
        
    finally:
        if driver:
            driver.quit()
            logger.info("Browser closed")
            
if __name__ == "__main__":
    main()