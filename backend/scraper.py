import re
from colorama import Fore, Style
from utils import setup_playwright_driver
from time import sleep
import random

# Refined email regex pattern
email_format = r"(?<!\w)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?!\w)"
phone_format = r"\+?1?\d{9,15}"

class Scraper:
    def __init__(self, interest, country):
        """
        Initialize the scraper with the search term and country.
        """
        self.page, self.playwright, self.browser = setup_playwright_driver()
        self.interest = interest
        self.country = country
        self.search_term = (
            f'"{self.interest}" intext:"@gmail.com" OR intext:"@yahoo.com" intext:"+1" "{self.country}"'
        )
        self.unique_emails = set()
        self.unique_phone_numbers = set()

    def introduce_human_like_behavior(self):
        """
        Introduce human-like behavior by adding random delays.
        """
        delay = random.uniform(2, 5)  # Random delay between 2 to 5 seconds
        print(Fore.CYAN + f"Simulating human behavior with a delay of {delay:.2f} seconds." + Style.RESET_ALL)
        sleep(delay)

    def detect_and_handle_recaptcha(self):
        """
        Detect and handle reCAPTCHA challenges.
        """
        try:
            captcha_present = self.page.locator("iframe[title*='reCAPTCHA']").count()
            if captcha_present > 0:
                print(Fore.RED + "reCAPTCHA detected! Please solve it manually or Change you IP." + Style.RESET_ALL)
                input("Press Enter after solving the reCAPTCHA...")
                return True
            return False
        except Exception as e:
            print(Fore.RED + f"Error detecting reCAPTCHA: {e}" + Style.RESET_ALL)
            return False

    def google_search(self):
        """
        Perform a Google search for the specified interest and country.
        """
        try:
            print(Fore.YELLOW + f"Starting Google search for: {self.search_term}" + Style.RESET_ALL)
            google_url = f"https://www.google.com/search?q={self.search_term.replace(' ', '+')}"
            print(Fore.CYAN + f"Searching: {google_url}" + Style.RESET_ALL)

            self.page.goto(google_url, timeout=15000)
            self.page.wait_for_load_state("networkidle")

            # Check and handle reCAPTCHA
            if self.detect_and_handle_recaptcha():
                return {"error": "reCAPTCHA encountered and handled."}

            results = []
            self.extract_data(results)
            self.handle_pagination(results)

            return results

        except Exception as e:
            if "Error extracting data for result 1: Locator.get_attribute: Error: strict mode violation" in str(e):
                print(Fore.RED + "reCAPTCHA encountered and handled." + Style.RESET_ALL)
                return {"error": "reCAPTCHA encountered and handled."}
            return 
        finally:
            self.cleanup()

    def extract_data(self, results):
        """
        Extract valid emails, phone numbers, and source links from the current page.
        """
        print(Fore.CYAN + "Extracting data from the current page..." + Style.RESET_ALL)

        # Find all search result containers
        results_locator = self.page.locator("div.tF2Cxc")  # Google's search result container class
        count = results_locator.count()
        print(Fore.LIGHTBLUE_EX + f"Found {count} results on this page." + Style.RESET_ALL)

        for i in range(count):
            try:
                # Introduce human-like delay
                self.introduce_human_like_behavior()

                # Extract the title (name)
                title = results_locator.nth(i).locator("h3").inner_text(timeout=3000)

                # Extract the snippet (may contain emails/phones)
                snippet = results_locator.nth(i).locator(".VwiC3b").inner_text(timeout=3000)

                # Extract the source link
                link = results_locator.nth(i).locator("a").get_attribute("href")

                # Find and validate emails and phone numbers
                raw_emails = re.findall(email_format, snippet)
                valid_emails = [email for email in raw_emails if self.is_valid_email(email)]
                phone_numbers = list(set(re.findall(phone_format, snippet)))

                # Add unique emails and phone numbers to sets
                self.unique_emails.update(valid_emails)
                self.unique_phone_numbers.update(phone_numbers)

                if valid_emails or phone_numbers:
                    # Log extracted details
                    print(Fore.GREEN + f"Name: {title}" + Style.RESET_ALL)
                    print(Fore.GREEN + f"Valid Emails: {valid_emails}" + Style.RESET_ALL)
                    print(Fore.GREEN + f"Phone Numbers: {phone_numbers}" + Style.RESET_ALL)
                    print(Fore.GREEN + f"Source Link: {link}" + Style.RESET_ALL)

                    # Append to results
                    results.append({
                        "name": title,
                        "emails": list(self.unique_emails),
                        "phone_numbers": list(self.unique_phone_numbers),
                        "source_link": link
                    })

            except Exception as e:
                print(Fore.RED + f"Error extracting data for result {i}: {e}" + Style.RESET_ALL)

    def is_valid_email(self, email):
        """
        Validate email to ensure it doesn't end with a period and follows general email rules.
        """
        if email.endswith("."):
            return False
        return True

    def handle_pagination(self, results):
        """
        Handle pagination to extract data from additional pages.
        """
        print(Fore.YELLOW + "Handling pagination..." + Style.RESET_ALL)
        while True:
            try:
                next_button = self.page.query_selector("a#pnnext")
                if next_button:
                    next_button.click()
                    self.page.wait_for_load_state("networkidle")

                    # Check and handle reCAPTCHA
                    if self.detect_and_handle_recaptcha():
                        return

                    self.extract_data(results)
                else:
                    print(Fore.YELLOW + "No more pages." + Style.RESET_ALL)
                    break
            except Exception as e:
                print(Fore.RED + f"Error handling pagination: {e}" + Style.RESET_ALL)
                break

    def cleanup(self):
        """
        Cleanup browser resources.
        """
        sleep(5)
        self.browser.close()
        self.playwright.stop()
