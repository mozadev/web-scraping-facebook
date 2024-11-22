import logging
from datetime import datetime
import os

def setup_logging():
    
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    log_filename = f'logs/scraping_{datetime.now():%Y%m%d_%H%M%S}.log'
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[   
            logging.FileHandler(log_filename),    
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger('web_scraper')
    logger.setLevel(logging.INFO)
    logger.info("Sistema de logging iniciado")
    logger.info(f"Archivo de log: {log_filename}")
    return logger