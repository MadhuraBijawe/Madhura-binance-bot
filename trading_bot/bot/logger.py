import logging
import os
import sys

def setup_logger(name):
    """
    Sets up a logger that executes to both console and file.
    
    Args:
        name (str): The name of the logger.
        
    Returns:
        logging.Logger: The configured logger instance.
    """
    # Ensure logs directory exists
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, 'bot.log')

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Check if handlers are already added to avoid duplicates
    if not logger.handlers:
        # File Handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        
        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger
