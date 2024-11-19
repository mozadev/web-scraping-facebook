import logging
from datetime import datetime
import os
from config.settings import OUTPUT_SETTINGS

def setup_logging():
  
    if not os.path.exists(OUTPUT_SETTINGS['logs_folder']):
        os.makedirs(OUTPUT_SETTINGS['logs_folder'])
    
    log_file = f"{OUTPUT_SETTINGS['logs_folder']}/scraping_{datetime.now():%Y%m%d_%H%M%S}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger('web_scraper')