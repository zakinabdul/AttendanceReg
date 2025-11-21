import logging
import sys
import os
# Import the settings we just created
from src.core.config import settings 

# Create logs folder only if we are in DEBUG mode (Local)
if settings.DEBUG and not os.path.exists("logs"):
    os.makedirs("logs")

def setup_logger():
    logger = logging.getLogger("attendance_backend")
    
    # --- SMART LEVEL SETTING ---
    # If DEBUG=True (Local), show everything.
    # If DEBUG=False (Production), only show INFO and Errors.
    if settings.DEBUG:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # --- HANDLER 1: THE TERMINAL (Essential for Render) ---
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO) # Keep terminal clean-ish
    console_format = logging.Formatter("%(levelname)s:    %(message)s")
    console_handler.setFormatter(console_format)
    
    # Add console handler (This is what shows up in Render Dashboard)
    if not logger.handlers:
        logger.addHandler(console_handler)

    # --- HANDLER 2: THE FILE (Local Only) ---
    # Only add the file handler if we are working locally
    if settings.DEBUG:
        file_handler = logging.FileHandler("logs/server.log")
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
    
    return logger

logger = setup_logger()