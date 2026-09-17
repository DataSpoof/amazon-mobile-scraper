"""
Simplified Amazon Mobile Scraper
A beginner-friendly version of the mobile scraper
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Configuration
AMAZON_URL = "https://www.amazon.in"
SEARCH_QUERY = "mobile under 100000"
PRICE_LIMIT = 100000

def scrape_amazon_mobiles():
    # Setup
    driver = webdriver.Chrome()
    driver.get(AMAZON_URL)
    print("[OK] Opened Amazon.in")
    time.sleep(2)

    # Search
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys(SEARCH_QUERY)
    driver.find_element(By.ID, "nav-search-submit-button").click()
    print(f"[OK] Searched for '{SEARCH_QUERY}'")
    time.sleep(3)

    # Extract products
    products_data = []
    products = driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    print(f"[OK] Found {len(products)} products")

    for product in products:
        try:
            # Get product name - try multiple selectors
            try:
                name = product.find_element(By.CSS_SELECTOR, "h2 span").text
            except:
                name = product.find_element(By.CSS_SELECTOR, "h2 a span").text

            # Get price
            try:
                price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                price_value = float(price.replace('₹', '').replace(',', '').strip())
            except:
                price = "N/A"
                price_value = 0

            # Get rating
            try:
                rating = product.find_element(By.CSS_SELECTOR, ".a-star-small span").text.split()[0]
            except:
                try:
                    rating = product.find_element(By.CSS_SELECTOR, ".a-icon-star-small span").text.split()[0]
                except:
                    rating = "N/A"

            # Filter by price
            if price_value > 0 and price_value <= PRICE_LIMIT:
                products_data.append({
                    "name": name,
                    "price": price,
                    "rating": rating
                })
                print(f"  • {name[:60]:<60} | {price:<12} | {rating}")

        except Exception as e:
            continue

    # Save results
    with open("mobile_results_simple.json", "w", encoding='utf-8') as f:
        json.dump(products_data, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Saved {len(products_data)} mobiles to mobile_results_simple.json")

    # Cleanup
    driver.quit()
    print("[OK] Done!")

if __name__ == "__main__":
    scrape_amazon_mobiles()
