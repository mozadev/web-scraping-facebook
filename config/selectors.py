OPLOGIN_SELECTORS = {
  'user': 'input#login[username]',
  'password': 'input#login[password]',
  'login_button':'btnLoginSubmit',
}


FB_SELECTORS = {
    'email': 'input#email',
    'password': 'input#pass',
    'login_button': 'button[name="login"]',
    'marketplace': '//span[contains(text(), "Marketplace")]',
    'search_box': '//input[@placeholder="Search Marketplace"]',
    'search_button': '//div[@aria-label="Search Marketplace"]',
    'product_items': '//div[@data-testid="marketplace_feed_item"]',
    'product_title': './/span[contains(@class, "title")]',
    'product_price': './/span[contains(@class, "price")]',
    'product_location': './/span[contains(@class, "location")]'
}

























FB_SELECTORS = {
    'email': 'input#email',
    'password': 'input#pass',
    'login_button': 'button[name="login"]',
    'marketplace': '//span[contains(text(), "Marketplace")]',
    'search_box': '//input[@placeholder="Search Marketplace"]',
    'search_button': '//div[@aria-label="Search Marketplace"]',
    'product_items': '//div[@data-testid="marketplace_feed_item"]',
    'product_title': './/span[contains(@class, "title")]',
    'product_price': './/span[contains(@class, "price")]',
    'product_location': './/span[contains(@class, "location")]'
}


AMAZON_SELECTORS = {
    'search_box': 'input#twotabsearchtextbox',
    'search_button': 'input.nav-search-submit',
    'product_list': 'div[data-component-type="s-search-result"]',
    'product_title': 'span.a-text-normal',
    'product_price': 'span.a-price-whole'
}

EBAY_SELECTORS = {
    'search_box': 'input#gh-ac',
    'search_button': 'input#gh-btn',
    'product_list': 'li.s-item',
    'product_title': 'h3.s-item__title',
    'product_price': 'span.s-item__price'
}