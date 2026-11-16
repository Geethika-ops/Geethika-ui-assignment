from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open the browser
driver = webdriver.Chrome()

# Step 2: Open the website
driver.get("https://sauce-demo.myshopify.com/")

# Step 3: Maximize the browser
driver.maximize_window()
time.sleep(3)

# Step 4: Select the first product
product = driver.find_element(By.CSS_SELECTOR,"img[alt='Noir jacket']")
product.click()
time.sleep(3)

# Step 5: Click Add to Cart
add_button = driver.find_element(By.ID, "add")
add_button.click()
time.sleep(3)

# Step 6: Open the cart
driver.get("https://sauce-demo.myshopify.com/cart")
time.sleep(3)

# Step 7: Verify the cart
cart_text = driver.find_element(By.TAG_NAME, "body").text
assert "Noir jacket" in cart_text, "Noir Jacket was not added to the cart!"
print("PASS: Noir Jacket is successfully added to the cart!")

# Step 7: Remove product from cart
remove_button = driver.find_element(By.CSS_SELECTOR, "a[href*='/cart/change']:not(.removeLine)")
remove_button.click()
time.sleep(3)

# Step 8: Verify cart is empty
time.sleep(3)
cart_text = driver.find_element(By.TAG_NAME, "body").text
assert "your cart is currently empty" in cart_text.lower()
print("Product removed successfully!")
print("Cart is empty!")
