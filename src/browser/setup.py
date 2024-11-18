from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import BROWSER_SETTINGS

def setup_chrome_driver():
    """Set up and return a Chrome WebDriver instance"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    if BROWSER_SETTINGS['headless']:
        options.add_argument("--headless")
    
    # Anti-bot detection settings
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    driver.implicitly_wait(BROWSER_SETTINGS['timeout'])
    driver.set_page_load_timeout(BROWSER_SETTINGS['page_load_timeout'])
    
    # Disable webdriver detection
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    
    return driver