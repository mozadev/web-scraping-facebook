# config/selectors.py

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
    'product_container': 'div.x9f619.x78zum5.x1r8uery.xdt5ytf.x1iyjqo2.xs83m0k.x1e558r4',
    'product_title': 'span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6',
    'product_price': 'span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x676frb.x1lkfr7t.x1lbecb7.x1s688f.xzsf02u',
    'product_location': 'span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft'
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