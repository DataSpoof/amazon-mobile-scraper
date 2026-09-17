# Amazon Mobile Scraper - Workflow Diagram

## Program Flow

```
┌─────────────────────────────────────────────────────────────┐
│          AMAZON MOBILE SCRAPER WORKFLOW                     │
└─────────────────────────────────────────────────────────────┘

START
  │
  ├─► 1. Initialize Chrome WebDriver
  │      └─► [Browser opens]
  │
  ├─► 2. Navigate to amazon.in
  │      └─► [Page loads]
  │
  ├─► 3. Find & Fill Search Box
  │      ├─► Locate: #twotabsearchtextbox
  │      └─► Type: "mobile under 100000"
  │
  ├─► 4. Click Search Button
  │      ├─► Locate: #nav-search-submit-button
  │      └─► [Results load]
  │
  ├─► 5. Wait for Results
  │      └─► Explicit wait: [data-component-type='s-search-result']
  │
  ├─► 6. Extract Products (Pass 1)
  │      ├─► Find all product containers
  │      ├─► For each product:
  │      │    ├─► Get name (h2 a span)
  │      │    ├─► Get price (.a-price-whole)
  │      │    ├─► Get rating (.a-star-small span)
  │      │    └─► Get reviews (.a-size-base)
  │      │
  │      └─► Filter: price <= ₹100,000
  │            └─► Store in list
  │
  ├─► 7. Scroll Down
  │      ├─► window.scrollBy(0, innerHeight)
  │      ├─► Wait 2 seconds
  │      └─► Repeat 2 times
  │
  ├─► 8. Extract Products (Pass 2)
  │      └─► [Same as Step 6]
  │
  ├─► 9. Save to JSON
  │      └─► mobile_results.json
  │
  ├─► 10. Save to CSV
  │       └─► mobile_results.csv
  │
  ├─► 11. Display Results
  │       └─► [Formatted table in console]
  │
  ├─► 12. Close Browser
  │       └─► driver.quit()
  │
  └─► END ✓

```

---

## Data Extraction Detail

```
┌─────────────────────────────────────────────────────────┐
│         PRODUCT EXTRACTION PROCESS                      │
└─────────────────────────────────────────────────────────┘

For each product found:

┌─────────────────────────┐
│ Product Container       │  [data-component-type='s-search-result']
│                         │
│ ┌─────────────────────┐ │
│ │ Product Name        │ │  CSS: h2 a span
│ │ "Apple iPhone 15"   │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ Price               │ │  CSS: .a-price-whole
│ │ "₹69,999"           │ │  Extract & clean
│ └─────────────────────┘ │  Convert to number
│                         │
│ ┌─────────────────────┐ │
│ │ Rating              │ │  CSS: .a-star-small span
│ │ "4.5 out of 5"      │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ Reviews             │ │  CSS: .a-size-base
│ │ "3,245 ratings"     │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ Price Filter        │ │  If price <= 100,000
│ │ ≤ ₹100,000?         │ │  Then INCLUDE
│ │ YES → INCLUDE       │ │  Else SKIP
│ │ NO  → SKIP          │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ Add to Results      │ │
│ │ List                │ │
│ └─────────────────────┘ │
└─────────────────────────┘
         │
         ▼
    [Next Product]

```

---

## File & Output Relationship

```
┌──────────────────────────────────┐
│   INPUT: Configuration            │
│                                   │
│  config.py                        │
│  - SEARCH_QUERY                   │
│  - PRICE_LIMIT                    │
│  - SCROLL_COUNT                   │
│  - SELECTORS (CSS/XPath)          │
└──────────────────────────────────┘
         │
         ▼
┌──────────────────────────────────┐
│   PROCESSING: Scraper Script      │
│                                   │
│  amazon_mobile_scraper.py         │
│  1. Browser automation            │
│  2. Data extraction               │
│  3. Filtering & cleaning          │
│  4. Error handling                │
└──────────────────────────────────┘
         │
    ┌────┴────┬──────────┐
    │          │          │
    ▼          ▼          ▼
┌─────┐  ┌────────┐  ┌─────────┐
│JSON │  │ CSV    │  │Console  │
│File │  │File    │  │Output   │
└─────┘  └────────┘  └─────────┘
    │          │          │
    └──────────┴──────────┘
            │
            ▼
    [User Analysis]
    (Excel, Sheets, etc.)

```

---

## Decision Tree

```
┌─────────────────────────────────────┐
│ WHICH SCRIPT TO RUN?                │
└─────────────────────────────────────┘
              │
              │
         ┌────┴────┐
         │          │
         ▼          ▼
    Beginner   Experienced
         │          │
         ▼          ▼
   Simple.py  Mobile_scraper.py
         │          │
    60 lines   400+ lines
    Basic      Advanced
    Features   Features
    Limited    Full
    Options    Options
         │          │
         └────┬─────┘
              ▼
        RUN & GET DATA

```

---

## Time Breakdown

```
┌──────────────────────────────────────┐
│ EXECUTION TIME BREAKDOWN             │
│ (Total: ~30-45 seconds)              │
└──────────────────────────────────────┘

  Browser startup:      [====] 3s    8%
  Navigate Amazon:      [======] 5s   14%
  Search & wait:        [========] 8s  21%
  Extract Pass 1:       [=====] 4s    11%
  Scroll & wait:        [====] 3s     8%
  Extract Pass 2:       [=====] 4s    11%
  Save JSON/CSV:        [====] 3s     8%
  Close browser:        [====] 3s     8%
  ──────────────────────────────────────
  TOTAL:                ≈ 35 seconds  100%

Performance depends on:
  • Internet connection speed (5-15% impact)
  • System performance (5-10% impact)
  • Number of products (10-20% impact)

```

---

## Error Handling Flow

```
┌─────────────────────────────┐
│ ERROR HANDLING              │
└─────────────────────────────┘
          │
          ▼
    ┌─────────────┐
    │ Error Type? │
    └─────────────┘
       │  │  │
   ┌───┘  │  └────┐
   │      │       │
   ▼      ▼       ▼
Timeout  Element  Network
  │        │        │
  │        │        │
  ▼        ▼        ▼
Retry   Skip    Retry
3x      Item    Wait
        &       &
Result  Log    Continue
        Error
```

---

## CSS Selector Cheat Sheet

```
┌──────────────────────────────────────────────┐
│ IMPORTANT CSS SELECTORS USED                 │
└──────────────────────────────────────────────┘

ID Selectors (#):
  #twotabsearchtextbox         → Search input box
  #nav-search-submit-button    → Search button

Class Selectors (.):
  .a-price-whole               → Product price
  .a-star-small                → Rating container
  .a-size-base                 → Review count

Attribute Selectors ([ ]):
  [data-component-type='s-search-result']  → Product containers

Nested Selectors:
  h2 a span                    → Product name
  .a-star-small span           → Rating text

Priority to update if Amazon changes:
  1. Product containers [data-component-type...]
  2. Product name h2 a span
  3. Price .a-price-whole
  4. Rating .a-star-small span

```

---

## Output Format Examples

### JSON Output
```json
[
  {
    "name": "Samsung Galaxy A55 5G",
    "price": "₹42,999",
    "rating": "4.6 out of 5",
    "reviews": "3,245 ratings"
  },
  {
    "name": "OnePlus 12R",
    "price": "₹39,999",
    "rating": "4.7 out of 5",
    "reviews": "1,890 ratings"
  }
]
```

### CSV Output
```csv
name,price,rating,reviews
Samsung Galaxy A55 5G,₹42999,4.6 out of 5,3245 ratings
OnePlus 12R,₹39999,4.7 out of 5,1890 ratings
```

### Console Output
```
====================================================================================================
Product Name                                           Price           Rating     Reviews        
====================================================================================================
Samsung Galaxy A55 5G...                              ₹42,999         4.6 out... 3,245 ratings
OnePlus 12R...                                        ₹39,999         4.7 out... 1,890 ratings
====================================================================================================
Total mobiles found: 2
```

---

## Troubleshooting Decision Tree

```
    Problem Occurred?
              │
              ▼
    ┌─────────────────────┐
    │ What went wrong?    │
    └─────────────────────┘
         │  │  │  │
    ┌────┘  │  │  └──────┐
    │       │  │         │
    ▼       ▼  ▼         ▼
  Module  Element Network Browser
  Import  Not   Error   Won't
  Error   Found          Open
    │       │     │       │
    ▼       ▼     ▼       ▼
  pip   Update  Check  Install
 install CSS  Internet Chrome
 pkgs   Selector Speed
```

---

## Next Steps After Scraping

```
1. GET DATA
   └─► python amazon_mobile_scraper.py

2. REVIEW RESULTS
   └─► Open mobile_results.csv or .json

3. ANALYZE DATA
   ├─► Import to Excel/Sheets
   ├─► Sort by price/rating
   ├─► Filter by brand
   └─► Create charts/graphs

4. MAKE DECISION
   ├─► Compare specifications
   ├─► Read reviews
   ├─► Check warranty
   └─► Make purchase decision
```

---

## Version Compatibility

```
┌────────────────────────────────┐
│ COMPATIBLE VERSIONS            │
└────────────────────────────────┘

Python:          3.7, 3.8, 3.9, 3.10, 3.11, 3.12+
Selenium:        4.15.2 (latest stable)
WebDriver Mgr:   4.0.1 (latest stable)
Chrome:          Latest (auto-updated)
OS:              Windows, macOS, Linux

```

---

This workflow diagram provides a complete visual understanding of how the scraper works!
