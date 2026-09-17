import time
import json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class AmazonMobileScraper:
    def __init__(self):
        self.driver = None
        self.mobiles = []

    def setup_driver(self):
        """Initialize the Chrome WebDriver"""
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        self.driver = webdriver.Chrome(options=options)
        print("[OK] WebDriver initialized")

    def navigate_to_amazon(self):
        """Navigate to Amazon India"""
        try:
            self.driver.get("https://www.amazon.in")
            print("[OK] Navigated to Amazon.in")
            time.sleep(2)
        except Exception as e:
            print(f"[FAIL] Error navigating to Amazon: {e}")

    def search_mobiles(self, search_query="mobile under 100000"):
        """Search for mobiles on Amazon"""
        try:
            # Wait for search box to be visible
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
            search_box.clear()
            search_box.send_keys(search_query)
            print(f"[OK] Entered search query: '{search_query}'")

            # Click search button
            search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
            search_button.click()
            print("[OK] Search initiated")

            # Wait for results to load
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-component-type='s-search-result']"))
            )
            print("[OK] Search results loaded")

        except TimeoutException:
            print("[FAIL] Timeout waiting for search elements")
        except Exception as e:
            print(f"[FAIL] Error during search: {e}")

    def extract_product_details(self):
        """Extract mobile names, ratings, and prices"""
        try:
            products = self.driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")
            print(f"[OK] Found {len(products)} products")

            for idx, product in enumerate(products, 1):
                try:
                    # Extract product name
                    name_element = product.find_element(By.CSS_SELECTOR, "h2 span")
                    name = name_element.text

                    # Extract price
                    try:
                        price_element = product.find_element(By.CSS_SELECTOR, ".a-price-whole")
                        price = price_element.text.replace(',', '')
                    except NoSuchElementException:
                        price = "N/A"

                    # Extract rating
                    try:
                        rating_element = product.find_element(By.CSS_SELECTOR, ".a-star-small span")
                        rating = rating_element.text.split()[0]
                    except NoSuchElementException:
                        rating = "No rating"

                    # Extract number of reviews
                    try:
                        reviews_element = product.find_element(By.CSS_SELECTOR, ".a-size-base")
                        reviews = reviews_element.text
                    except NoSuchElementException:
                        reviews = "0"

                    # Filter products under 100k if price is available
                    if price != "N/A":
                        try:
                            price_value = float(price.replace('₹', '').strip())
                            if price_value <= 100000:
                                mobile_data = {
                                    "name": name,
                                    "price": price,
                                    "rating": rating,
                                    "reviews": reviews
                                }
                                self.mobiles.append(mobile_data)
                                print(f"  [{idx}] {name[:50]}... | Price: {price} | Rating: {rating}")
                        except ValueError:
                            pass

                except NoSuchElementException as e:
                    continue
                except Exception as e:
                    print(f"  Error extracting product {idx}: {e}")
                    continue

        except Exception as e:
            print(f"[FAIL] Error extracting product details: {e}")

    def scroll_and_load_more(self, scrolls=3):
        """Scroll down to load more products"""
        try:
            for i in range(scrolls):
                self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
                print(f"[OK] Scrolled down ({i+1}/{scrolls})")
                time.sleep(2)
        except Exception as e:
            print(f"[FAIL] Error scrolling: {e}")

    def save_results(self, filename="mobile_results.json"):
        """Save results to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.mobiles, f, ensure_ascii=False, indent=2)
            print(f"[OK] Results saved to {filename}")
        except Exception as e:
            print(f"[FAIL] Error saving JSON: {e}")

    def save_to_csv(self, filename="mobile_results.csv"):
        """Save results to CSV file"""
        try:
            if not self.mobiles:
                print("[FAIL] No data to save")
                return

            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['name', 'price', 'rating', 'reviews'])
                writer.writeheader()
                writer.writerows(self.mobiles)
            print(f"[OK] Results saved to {filename}")
        except Exception as e:
            print(f"[FAIL] Error saving CSV: {e}")

    def print_results(self):
        """Print results in a formatted table"""
        if not self.mobiles:
            print("\n[FAIL] No mobiles found")
            return

        print("\n" + "="*100)
        print(f"{'Product Name':<50} {'Price':<15} {'Rating':<10} {'Reviews':<15}")
        print("="*100)

        for mobile in self.mobiles:
            try:
                name = mobile['name'][:47] + "..." if len(mobile['name']) > 50 else mobile['name']
                price = mobile['price'][:12] if len(mobile['price']) <= 12 else mobile['price'][:12]
                rating = mobile['rating'][:8]
                reviews = mobile['reviews'][:12]
                print(f"{name:<50} {price:<15} {rating:<10} {reviews:<15}")
            except UnicodeEncodeError:
                # Fallback for encoding issues
                print(f"Product: {mobile['name'][:50]}... | Price: INR | Rating: {mobile['rating']}")

        print("="*100)
        print(f"Total mobiles found: {len(self.mobiles)}")

    def close_driver(self):
        """Close the WebDriver"""
        if self.driver:
            self.driver.quit()
            print("\n[OK] WebDriver closed")

    def run(self):
        """Run the complete scraping process"""
        try:
            print("\n" + "="*50)
            print("Amazon Mobile Scraper Started")
            print("="*50 + "\n")

            self.setup_driver()
            self.navigate_to_amazon()
            self.search_mobiles("mobile under 100000")

            # Extract from initial results
            self.extract_product_details()

            # Scroll and load more products
            self.scroll_and_load_more(scrolls=2)

            # Extract again after scrolling
            self.extract_product_details()

            # Save results
            self.save_results("mobile_results.json")
            self.save_to_csv("mobile_results.csv")

            # Print results
            self.print_results()

            print("\n" + "="*50)
            print("Scraping completed successfully!")
            print("="*50 + "\n")

        except Exception as e:
            print(f"\n[FAIL] Fatal error: {e}")
        finally:
            self.close_driver()

if __name__ == "__main__":
    scraper = AmazonMobileScraper()
    scraper.run()
