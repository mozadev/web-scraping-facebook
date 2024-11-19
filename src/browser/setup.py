from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import BROWSER_SETTINGS

def setup_chrome_driver():
   
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    if BROWSER_SETTINGS['headless']:
        options.add_argument("--headless")
    
   
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors-skipi-list')

    # prefs ={
    #         "safebrowsing.enabled": True  # Desactiva la protección de navegación segura
    #     } 

    # options.add_experimental_option('prefs', prefs)

    


       
        

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    driver.implicitly_wait(BROWSER_SETTINGS['timeout'])
    driver.set_page_load_timeout(BROWSER_SETTINGS['page_load_timeout'])
    

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    
    return driver