"""
Test Setup Script
Verify that all dependencies and configurations are correct
"""

import sys
import os

def test_python_version():
    """Check Python version"""
    print("=" * 60)
    print("TESTING SETUP FOR AMAZON MOBILE SCRAPER")
    print("=" * 60)

    version = sys.version_info
    print(f"\n[OK] Python Version: {version.major}.{version.minor}.{version.micro}")

    if version.major >= 3 and version.minor >= 7:
        print("  [OK] Python version is compatible (3.7+)")
        return True
    else:
        print("  [FAIL] Python 3.7+ required")
        return False

def test_selenium():
    """Check if Selenium is installed"""
    try:
        import selenium
        print(f"\n[OK] Selenium: {selenium.__version__}")
        return True
    except ImportError:
        print("\n[FAIL] Selenium not installed")
        print("  Install with: pip install selenium==4.15.2")
        return False

def test_webdriver_manager():
    """Check if webdriver-manager is installed"""
    try:
        import webdriver_manager
        print(f"[OK] WebDriver Manager: Installed")
        return True
    except ImportError:
        print("[FAIL] WebDriver Manager not installed")
        print("  Install with: pip install webdriver-manager==4.0.1")
        return False

def test_chrome_installed():
    """Check if Chrome is installed"""
    import platform

    if platform.system() == "Windows":
        import shutil
        chrome_path = shutil.which("chrome") or shutil.which("chrome.exe")

        # Also check common installation paths
        possible_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]

        chrome_found = chrome_path is not None
        for path in possible_paths:
            if os.path.exists(path):
                chrome_found = True
                break

        if chrome_found:
            print("\n[OK] Google Chrome: Installed")
            return True
        else:
            print("\n[FAIL] Google Chrome: Not found")
            print("  Download from: https://www.google.com/chrome/")
            return False
    else:
        print("\n[WARN] Could not verify Chrome on this platform")
        return True

def test_config_files():
    """Check if configuration files exist"""
    files = [
        "config.py",
        "amazon_mobile_scraper.py",
        "requirements.txt",
    ]

    print("\n[OK] Configuration Files:")
    all_exist = True
    for file in files:
        if os.path.exists(file):
            print(f"  [OK] {file}")
        else:
            print(f"  [FAIL] {file} (MISSING)")
            all_exist = False

    return all_exist

def test_import_config():
    """Test if config can be imported"""
    try:
        import config
        print("\n[OK] Config module: Imported successfully")
        print(f"  - Search Query: {config.SEARCH_QUERY}")
        print(f"  - Price Limit: {config.PRICE_LIMIT}")
        print(f"  - Scroll Count: {config.SCROLL_COUNT}")
        return True
    except Exception as e:
        print(f"\n[FAIL] Config module error: {e}")
        return False

def main():
    """Run all tests"""
    results = []

    results.append(("Python Version", test_python_version()))
    results.append(("Selenium", test_selenium()))
    results.append(("WebDriver Manager", test_webdriver_manager()))
    results.append(("Chrome Browser", test_chrome_installed()))
    results.append(("Config Files", test_config_files()))
    results.append(("Config Import", test_import_config()))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "[PASS]" if result else "[FAIL]"
        print(f"{status}: {test_name}")

    print(f"\nResult: {passed}/{total} tests passed")

    if passed == total:
        print("\n[OK] All tests passed! You can run the scraper now.")
        print("\nRun scraper with:")
        print("  python amazon_mobile_scraper.py")
        print("or")
        print("  python amazon_mobile_scraper_simple.py")
    else:
        print("\n[ERROR] Some tests failed. Please fix the issues above.")
        print("\nFor help, see SETUP.md")

    print("=" * 60)

if __name__ == "__main__":
    main()
