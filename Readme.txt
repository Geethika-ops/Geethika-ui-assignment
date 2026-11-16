Selenium Cart Automation

Project Overview:

This project automates a basic shopping cart workflow using Python and Selenium WebDriver.
Website:https://sauce-demo.myshopify.com/

Technologies Used:
- Python
- Selenium WebDriver
- Google Chrome

Test Scenarios:
The automation script performs the following steps:
1. Launches the Chrome browser.
2. Opens the Shopify website.
3. Selects the desired product.
4. Opens the product details page.
5. Clicks the Add to Cart button.
6. Navigates to the cart page.
7. Verifies that the expected product (Noir Jacket) is present in the cart.
8. Removes the product from the cart.
9. Verifies that the cart displays the empty-cart message.
10. Closes the browser.

Project Structure:
Geethika-ui-assignment
     ui-tests
          readme.txt
          requirements.txt
          test-cart-flow.py

Prerequisites:
- Python 3 installed
- Google Chrome installed
- Selenium installed

Installation:
Clone or download this repository.
Navigate to the project directory and install the required dependency:

# macOS
python3 -m pip install -r requirements.txt

# Windows
py -m pip install -r requirements.txt

Execution:
Run the automation script using:
python3 test_cart.py
Replace `test_cart.py` if your Python script has a different filename.

Assertions and Verification:
The script includes the following validations:
1. Product verification:
assert "Noir jacket" in cart_text.lower()
Verifies that the expected product is displayed in the cart.
2. Empty-cart verification:
assert "your cart is currently empty" in cart_text.lower()

Verifies that the cart displays the expected empty-cart message after the product is removed.

Note:
- The script uses CSS selectors to locate web elements.
- `time.sleep()` is used for basic execution delays.
- The cart page is opened directly using its URL.
- The script uses Selenium with Python for browser automation.
- The first matching product link is selected, so the expected product may change if the website's product order changes.
