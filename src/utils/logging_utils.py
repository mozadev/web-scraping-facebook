# src/utils/logging_utils.py

import logging
from datetime import datetime
import os

def setup_logging():
    """Configurar sistema de logging"""
    
    # Crear directorio de logs si no existe
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Nombre del archivo de log con timestamp
    log_filename = f'logs/scraping_{datetime.now():%Y%m%d_%H%M%S}.log'
    
    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # Handler para archivo
            logging.FileHandler(log_filename),
            # Handler para consola
            logging.StreamHandler()
        ]
    )
    
    # Crear y retornar logger
    logger = logging.getLogger('web_scraper')
    logger.setLevel(logging.INFO)
    
    # Logging inicial
    logger.info("Sistema de logging iniciado")
    logger.info(f"Archivo de log: {log_filename}")
    
    return logger