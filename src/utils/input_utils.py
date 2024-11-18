import time
import random

def random_delay(min_sec=2, max_sec=4):
    """Add random delay between actions"""
    time.sleep(random.uniform(min_sec, max_sec))

def human_like_typing(element, text):
    """Simulate human-like typing"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))