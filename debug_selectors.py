"""
Debug script to inspect Amazon page structure and find correct selectors
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def debug_amazon():
    # Setup
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in")
    print("[OK] Opened Amazon.in\n")
    time.sleep(2)

    # Search
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("mobile under 100000")
    driver.find_element(By.ID, "nav-search-submit-button").click()
    print("[OK] Searched for 'mobile under 100000'\n")
    time.sleep(3)

    # Find products
    products = driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    print(f"[OK] Found {len(products)} products\n")
    print("="*80)
    print("ANALYZING FIRST 3 PRODUCTS")
    print("="*80 + "\n")

    for idx, product in enumerate(products[:3], 1):
        print(f"\n--- PRODUCT {idx} ---\n")

        # Get HTML content
        html = product.get_attribute('outerHTML')

        # Try different selectors
        selectors_to_try = {
            "Name (h2 a span)": "h2 a span",
            "Name (h2 span)": "h2 span",
            "Name (a span)": "a span",
            "Name (span)": "span",
            "Price (.a-price-whole)": ".a-price-whole",
            "Price (.a-price)": ".a-price",
            "Price (span.a-price)": "span.a-price",
            "Rating (.a-star-small)": ".a-star-small",
            "Rating (span.a-icon)": "span.a-icon",
            "Reviews (.a-size-base)": ".a-size-base",
        }

        for selector_name, selector in selectors_to_try.items():
            try:
                elements = product.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    for i, elem in enumerate(elements[:2]):
                        text = elem.text[:100] if elem.text else "[empty]"
                        print(f"  [{selector_name}] (elem {i}): {text}")
            except Exception as e:
                pass

        print(f"\n  [HTML Preview - first 500 chars]:\n  {html[:500]}...\n")

    # Close
    driver.quit()
    print("[OK] Done!")

if __name__ == "__main__":
    debug_amazon()
