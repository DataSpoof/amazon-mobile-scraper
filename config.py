"""
Configuration file for Amazon Mobile Scraper
Modify these settings to customize the scraper behavior
"""

# ============= AMAZON SETTINGS =============
AMAZON_URL = "https://www.amazon.in"
SEARCH_QUERY = "mobile under 100000"
PRICE_LIMIT = 100000  # Maximum price in INR

# ============= SCRAPING SETTINGS =============
# Number of times to scroll down (each scroll loads more products)
SCROLL_COUNT = 2

# Timeouts (in seconds)
DRIVER_WAIT_TIMEOUT = 10
PAGE_LOAD_DELAY = 2
SCROLL_DELAY = 2

# ============= OUTPUT SETTINGS =============
# Output file names
JSON_OUTPUT = "mobile_results.json"
CSV_OUTPUT = "mobile_results.csv"

# ============= BROWSER SETTINGS =============
# Set to True to run browser in headless mode (no window)
HEADLESS_MODE = False

# Add custom headers to avoid detection
CHROME_OPTIONS = [
    '--start-maximized',
    '--disable-blink-features=AutomationControlled',
    '--disable-dev-shm-usage',
    '--no-sandbox',
]

# ============= LOGGING SETTINGS =============
# Set to True for verbose output
VERBOSE = True

# ============= ADVANCED SETTINGS =============
# Retry settings for failed extractions
MAX_RETRIES = 2

# CSS Selectors (update these if Amazon changes their structure)
SELECTORS = {
    'search_box': '#twotabsearchtextbox',
    'search_button': '#nav-search-submit-button',
    'product_container': "[data-component-type='s-search-result']",
    'product_name': 'h2 a span',
    'product_price': '.a-price-whole',
    'product_rating': '.a-star-small span',
    'product_reviews': '.a-size-base',
}

# ============= CUSTOMIZATION EXAMPLES =============
"""
Example 1: Search for laptops instead of mobiles
    SEARCH_QUERY = "laptop under 50000"
    PRICE_LIMIT = 50000

Example 2: Increase number of products scraped
    SCROLL_COUNT = 5
    DRIVER_WAIT_TIMEOUT = 15

Example 3: Run in headless mode (faster, no window)
    HEADLESS_MODE = True

Example 4: Search for tablets
    SEARCH_QUERY = "tablet 4g under 20000"
    PRICE_LIMIT = 20000
"""
