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


# Test login with multiple usernames using parameterization
@pytest.mark.parametrize("username", [
    "standard_user", "locked_out_user", "problem_user", "performance_glitch_user"
])
def test_multiple_logins(driver, username):
    # Open the website
    driver.get("https://www.saucedemo.com/")

    # Locate and fill the login form
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Special handling for locked-out user
    if username == "locked_out_user":
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "locked out" in error_message, "Locked out user should not be able to log in!"
    else:
        # Assert successful login for other users
        assert "inventory" in driver.current_url, "Login failed!"
