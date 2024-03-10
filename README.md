# Selenium WebDriver Test for Flipkart

This Python code uses Selenium WebDriver and pytest to automate a test scenario on the Flipkart website. The test scenario includes:

1. Launching different browsers (Chrome, Firefox, Edge) using fixtures.
2. Opening the Flipkart homepage.
3. Searching for a product (laptop) and selecting a random product from the search results.
4. Adding the selected product to the cart and navigating to the cart.
5. Verifying that the correct item is in the cart.
6. Clicking on the "Proceed to Checkout" button.



## How to Run

1. Save the code in a Python file (e.g., `test_flipkart.py`).
2. Open a terminal and navigate to the directory containing the Python file.
3. Run the following command to execute the test:
   pytest -s filename.py
4. The test will launch different browsers, perform the test scenario, and output the results.

Note: This test script uses implicit waits (`implicitly_wait`) and explicit waits (`WebDriverWait`) for synchronization. It also uses random selection of products from the search results. Adjustments may be needed based on the current state of the Flipkart website.
