# Amazon Mobile Scraper (Selenium)

Automates browser actions to search for mobiles under 100k INR on Amazon.in and extracts product details.

## Features

✓ Automated browser automation using Selenium  
✓ Searches for "mobile under 100000" on Amazon.in  
✓ Extracts product names, prices, ratings, and review counts  
✓ Filters products under ₹100,000  
✓ Handles dynamic page loading and scrolling  
✓ Saves results in JSON and CSV formats  
✓ Displays formatted output in terminal  

## Prerequisites

- Python 3.7+
- Chrome browser installed
- ChromeDriver (automatically handled)

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install selenium==4.15.2
pip install webdriver-manager==4.0.1
```

## Usage

Run the scraper:
```bash
python amazon_mobile_scraper.py
```

## Output

The script generates:
- **mobile_results.json** - Detailed product data in JSON format
- **mobile_results.csv** - Results in spreadsheet format
- **Console output** - Formatted table with all products

## Sample Output

```
====================================================================================================
Product Name                                           Price           Rating     Reviews        
====================================================================================================
Apple iPhone 15...                                     ₹69,999         4.5 out of 5    250 ratings
Samsung Galaxy A54...                                  ₹45,999         4.3 out of 5    180 ratings
OnePlus 12...                                          ₹55,999         4.6 out of 5    320 ratings
...
====================================================================================================
Total mobiles found: 45
```

## How It Works

1. **Setup WebDriver** - Initializes Chrome WebDriver with options to avoid detection
2. **Navigate to Amazon** - Opens amazon.in
3. **Search** - Types search query and submits search
4. **Extract Products** - Scrapes product names, prices, ratings, and reviews
5. **Filter** - Keeps only products under ₹100,000
6. **Scroll & Load** - Scrolls down to load additional products
7. **Save Results** - Stores data in JSON and CSV formats

## CSS Selectors Used

- Search box: `#twotabsearchtextbox`
- Search button: `#nav-search-submit-button`
- Product container: `[data-component-type='s-search-result']`
- Product name: `h2 a span`
- Price: `.a-price-whole`
- Rating: `.a-star-small span`
- Reviews: `.a-size-base`

## Notes

- The script includes anti-detection measures to avoid being blocked
- Page load delays are included for stable scraping
- Prices are extracted in ₹ currency format
- Rating format: "X.X out of 5"
- Script handles missing/unavailable fields gracefully

## Troubleshooting

**ChromeDriver not found:**
```bash
pip install webdriver-manager
```

**"Element not found" errors:**
- Amazon's HTML structure may change - CSS selectors might need updating
- Try running again as some elements load dynamically

**Timeout errors:**
- Increase wait times in the script (WebDriverWait timeout values)
- Check your internet connection

## Advanced Usage

To search for different products, modify the search query:
```python
scraper.search_mobiles("your search query")
```

To scroll more pages:
```python
scraper.scroll_and_load_more(scrolls=5)  # More scrolls = more products
```

## Legal Notice

- Respect Amazon's Terms of Service
- Use responsibly and avoid excessive requests
- This is for educational purposes
- Check if web scraping is allowed per your local regulations
