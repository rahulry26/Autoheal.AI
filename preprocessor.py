# utils/preprocessor.py

import re

def clean_log_text(log_text: str) -> str:
    """
    Cleans the raw log text by removing unnecessary whitespaces,
    timestamps, and unwanted characters.
    """
    # Remove timestamps (basic regex for 2024-04-26 15:23:45 kind of format)
    log_text = re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', '', log_text)
    
    # Remove multiple spaces
    log_text = re.sub(r'\s+', ' ', log_text)
    
    return log_text.strip()

