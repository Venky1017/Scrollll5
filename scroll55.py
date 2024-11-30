from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()  # or use webdriver for your browser (e.g., Firefox)
driver.get('https://privatekeyfinder.io/private-keys/bitcoin/1229782938247303444')

try:
    while True:
        # Wait for the page to load
        time.sleep(2)

        # Find all Bitcoin addresses and their balances (update selector as needed)
        addresses = driver.find_elements(By.CSS_SELECTOR, '.address')  # Replace with actual CSS selector for addresses
        balances = driver.find_elements(By.CSS_SELECTOR, '.balance')  # Replace with actual CSS selector for balances

        # Loop through the addresses and balances
        for address, balance in zip(addresses, balances):
            # Check if the balance is exactly 6.7 BTC
            if '6.7 BTC' in balance.text:
                print("Found address with 6.7 BTC:", address.text)
                print("Page URL:", driver.current_url)

                # Save the URL to a file
                with open('found_address_urls.txt', 'a') as file:
                    file.write(driver.current_url + '\n')

                # Stop the loop once found
                raise Exception("Address with 6.7 BTC found, stopping the script.")

        # Find the 'Next' button and click it to go to the next page
        try:
            next_button = driver.find_element(By.LINK_TEXT, 'Next')
            next_button.click()
        except Exception:
            print("No more pages or error occurred.")
            break

except Exception as e:
    print("Error or found address:", e)

finally:
    driver.quit()
