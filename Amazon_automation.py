from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ask user for product to search for
product_name = input("Enter the name of the product you want to buy: ")

# Ask user for payment method
payment_method = input("Enter payment method (1 for credit card, 2 for gift card): ")

# Initialize the webdriver and go to Amazon's homepage
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

# Find the search bar and enter the product name
search_bar = driver.find_element_by_id("twotabsearchtextbox")
search_bar.send_keys(product_name)
search_bar.send_keys(Keys.RETURN)

# Wait for the search results page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "search")))

# Find the first product and click on it
product = driver.find_element_by_xpath("//div[@data-index='0']//h2/a")
product.click()

# Wait for the product page to load
wait.until(EC.presence_of_element_located((By.ID, "productTitle")))

# Find the "Add to Cart" button and click it
add_to_cart = driver.find_element_by_id("add-to-cart-button")
add_to_cart.click()

# Wait for the cart page to load
wait.until(EC.presence_of_element_located((By.ID, "hlb-view-cart-announce")))

# Find the "Proceed to checkout" button and click it
proceed_to_checkout = driver.find_element_by_name("proceedToRetailCheckout")
proceed_to_checkout.click()

# Wait for the checkout page to load
wait.until(EC.presence_of_element_located((By.ID, "enterAddressFullName")))

# Find the "Continue" button to proceed with the default shipping address
continue_button = driver.find_element_by_name("shipToThisAddress")
continue_button.click()

# Wait for the payment page to load
wait.until(EC.presence_of_element_located((By.ID, "payOptionDropDown")))

# Select a payment method from the dropdown list
payment_dropdown = Select(driver.find_element_by_id("payOptionDropDown"))
if payment_method == "1":
    payment_dropdown.select_by_value("VISA")
elif payment_method == "2":
    payment_dropdown.select_by_value("gc-redemption")

# Find the "Continue" button to proceed with the payment method
continue_button = driver.find_element_by_name("ppw-widgetEvent:SetPaymentPlanSelectContinueEvent")
continue_button.click()

# Wait for the order review page to load
wait.until(EC.presence_of_element_located((By.ID, "order-summary-box")))

# Quit the webdriver
driver.quit()
