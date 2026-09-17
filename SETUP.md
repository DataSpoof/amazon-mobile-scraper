# Quick Start Guide

## Step 1: Install Dependencies

Open PowerShell or Command Prompt in this directory and run:

```bash
pip install -r requirements.txt
```

## Step 2: Run the Scraper

```bash
python amazon_mobile_scraper.py
```

## What Happens

The script will:
1. Open Chrome browser automatically
2. Navigate to amazon.in
3. Search for "mobile under 100000"
4. Extract product information (name, price, rating, reviews)
5. Scroll down to load more products
6. Save results to:
   - `mobile_results.json` (detailed data)
   - `mobile_results.csv` (spreadsheet format)
7. Display formatted output in the terminal

## Expected Runtime

- **First run:** 30-45 seconds (depends on internet speed)
- **Subsequent runs:** 20-30 seconds

## Output Files

After running, you'll have:

### mobile_results.csv
```
name,price,rating,reviews
Apple iPhone 15,₹69999,4.5 out of 5,250 ratings
Samsung Galaxy A54,₹45999,4.3 out of 5,180 ratings
```

### mobile_results.json
```json
[
  {
    "name": "Apple iPhone 15",
    "price": "₹69,999",
    "rating": "4.5 out of 5",
    "reviews": "250 ratings"
  },
  ...
]
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'selenium'"
**Solution:** 
```bash
pip install selenium==4.15.2
```

### Issue: "ChromeDriver not found"
**Solution:** The script should auto-download it. If not:
```bash
pip install webdriver-manager
```

### Issue: Connection timeout
**Solution:** 
- Check internet connection
- Increase wait times in the script:
  - Find `WebDriverWait(self.driver, 10)` 
  - Change `10` to `20` or higher

### Issue: Elements not found
**Solution:**
- Amazon's website structure might have changed
- CSS selectors in the script may need updating
- Try running again

## Customization

### Search Different Products

Open `amazon_mobile_scraper.py` and find this line:
```python
self.search_mobiles("mobile under 100000")
```

Change it to:
```python
self.search_mobiles("laptop under 50000")
```

### Scroll More Pages

Find this line:
```python
self.scroll_and_load_more(scrolls=2)
```

Change `2` to a higher number like `5` to get more products.

### Change Price Filter

Find this line in the extraction logic:
```python
if price_value <= 100000:
```

Change `100000` to your desired price limit.

## Browser Control

The script opens Chrome in a normal window. You can:
- Watch what it's doing in real-time
- It will automatically close after completion
- Do NOT close the browser manually during execution

## Performance Tips

1. **Close other Chrome tabs** - Reduces system load
2. **Check internet speed** - Faster connection = faster scraping
3. **Adjust wait times** - Can increase timeouts if you have slow connection

## Next Steps

Once you have the data in `mobile_results.csv`:
1. Open in Excel or Google Sheets
2. Sort by price or rating
3. Filter by preferred brand
4. Compare specifications

---

**Need help?** Check README.md for more details and advanced usage.
