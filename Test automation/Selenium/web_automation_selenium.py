import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Fixture to initialize and quit the WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Test login functionality and verify product presence
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),  # Valid test credentials
])
def test_login(driver, username, password):
    # Open the website
    driver.get("https://www.saucedemo.com/")

    # Locate and fill the login form
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Assert login success by checking the inventory page
    assert "inventory" in driver.current_url, "Login failed!"

    # Verify the presence of a specific product
    product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    assert product.is_displayed(), "Product not found!"
