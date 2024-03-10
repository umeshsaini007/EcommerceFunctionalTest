import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browsers = ["chrome","firefox","edge"]

@pytest.fixture(params=browsers)
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        print(f"{request.param} Browser launched successfully!")
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        print(f"{request.param} Browser launched successfully!")
    elif request.param == "edge":
        driver = webdriver.Edge()
        print(f"{request.param} Browser launched successfully!")
    driver.implicitly_wait(10)


    yield driver
    driver.quit()

def test_flow(driver):
    # Opening https://www.flipkart.com/ URL
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    currentURL = driver.current_url

    # 1st Asserstion: Verify that the homepage loads successfully.
    assert "https://www.flipkart.com/" in currentURL
    print(f"""1st Asserstion: Verify that the homepage loads successfully
          Homepage Successfully Loaded in: {driver.name}""")

    # Searching for a product
    driver.find_element(By.XPATH,"//input[@name='q']").send_keys("laptop", Keys.ENTER)

    # Generating random number to open any random product from the search results webelements
    search_results = driver.find_elements(By.XPATH, "//div/a[@target=\"_blank\" and @class=\"_1fQZEK\"]")
    random_index = random.randint(0, len(search_results)-1)
    selected_result = search_results[random_index]
    selected_result.click()

    # Switching to window at 1
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    # Storing the Product Name
    wait = WebDriverWait(driver, 10)
    product_name_element = wait.until(EC.presence_of_element_located((By.XPATH,"//h1[@class='yhB1nd']/span")))
    product_name = product_name_element.text

    time.sleep(1)
    # Adding product to the cart
  
    driver.find_element(By.XPATH,"//button[normalize-space()='Add to cart']").click()

     # Navigate to the Cart
    driver.find_element(By.XPATH,"//span[normalize-space()='Cart']").click()

    # 2nd Assertion: Verify that the correct item is in the cart. 
    product_in_cart = driver.find_element(By.XPATH,"//div[@class='_2-uG6-']/a")
    product_in_cart = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_2-uG6-']/a")))
    assert product_in_cart.text in product_name
    print("""2nd Assertion: Verify that the correct item is in the cart.
          Correct product is added to the cart""")

    # Click on the "Proceed to Checkout" button.
    driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2ObVJD _3AWRsL']").click()

    # On the login page, enter valid credentials (username and password) to log in. ------- Flipkart has Login with OTP functionality---------------
    # Verify that the user is successfully logged in.
    # Enter valid shipping information (address, city, state, and zip code).
    # Proceed to the next step.
    # Choose a payment method (credit card, for example).
    # Review Order:
    # Verify the order summary.


if __name__=="__main__":
    pytest.main([__file__])
