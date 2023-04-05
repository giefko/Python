from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run the webdriver in headless mode (no GUI)
driver = webdriver.Chrome(options=options)

# Open the website
driver.get("https://temp-mail.org/")

# Wait for the email address to load
email_address = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "mail"))).get_attribute("value")

# Print the email address
print(f"Temporary email address: {email_address}")

# Close the webdriver
driver.quit()
