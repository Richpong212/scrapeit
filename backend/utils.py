from colorama import Fore, Style
from playwright.sync_api import sync_playwright

def setup_playwright_driver():
    """
    Sets up and returns a Playwright page instance for web scraping.
    Ensures a controlled environment and custom user-agent setup.
    """
    try:
        # Launch the browser
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
        page = context.new_page()

        print(Fore.GREEN + "Playwright setup successful!" + Style.RESET_ALL)
        return page, playwright, browser
    except Exception as e:
        print(Fore.RED + f"Error setting up Playwright: {e}" + Style.RESET_ALL)
        raise
