from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker

# Initialize Faker to generate random data
fake = Faker()


def accept_cookie_consent(driver):
    """Handles cookie consent modal if it appears."""
    try:
        time.sleep(3)  # Wait for the consent modal to load
        consent_modal = driver.find_element(By.CLASS_NAME, "fc-dialog-container")
        if consent_modal.is_displayed():
            print("✅ Consent modal detected!")
            consent_button = consent_modal.find_element(By.XPATH, "//button[contains(@class, 'fc-cta-consent')]")
            consent_button.click()
            print("✅ Clicked on 'Consent' button successfully!")
            time.sleep(2)
        else:
            print("✅ No consent modal detected.")
    except Exception as e:
        print(f"❌ Could not handle cookie consent: {e}")


def delete_user_account(driver):
    """Delete the user account."""
    try:
        # Wait for the "Delete Account" button to be clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Delete Account')]")))
        delete_account_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Delete Account')]")
        delete_account_button.click()
        print("✅ Clicked 'Delete Account' successfully!")
        time.sleep(3)  # Allow time for deletion

        # Verify 'ACCOUNT DELETED!' message
        account_deleted_message = driver.find_element(By.TAG_NAME, "h2")
        assert account_deleted_message.is_displayed(), "❌ 'ACCOUNT DELETED!' message is not visible!"
        print("✅ 'ACCOUNT DELETED!' message verified successfully!")

        # Click continue after deletion
        continue_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]")
        continue_button.click()
        print("✅ Clicked 'Continue' after account deletion!")
        time.sleep(3)  # Allow page transition
    except Exception as e:
        print(f"❌ Error in account deletion: {e}")


def navigate_to_signup_page(driver):
    """Navigate to the signup page."""
    try:
        signup_login_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Signup / Login")
        signup_login_button.click()
        print("✅ Clicked on 'Signup / Login' button successfully!")
    except Exception as e:
        print(f"❌ Could not click on 'Signup / Login': {e}")


def signup_user(driver):
    """Complete the signup process."""
    try:
        sign_up_form = driver.find_element(By.CLASS_NAME, "signup-form")
        assert sign_up_form.is_displayed(), "Form is not visible"
        print("✅ Register form is visible!")

        # Generate random user data
        name = fake.name()
        email = fake.email()

        name_field = sign_up_form.find_element(By.NAME, "name")
        email_field = sign_up_form.find_element(By.NAME, "email")
        submit_button = sign_up_form.find_element(By.TAG_NAME, "button")

        name_field.send_keys(name)
        email_field.send_keys(email)
        submit_button.click()
        print("✅ Signup form submitted successfully!")

    except Exception as e:
        print(f"❌ Could not complete signup: {e}")


def fill_account_info(driver):
    """Fill account creation information."""
    try:
        sign_up_form = driver.find_element(By.CLASS_NAME, "login-form")

        gender_label = sign_up_form.find_element(By.XPATH, "//label[@for='id_gender1']")  # Clicking the label
        gender_label.click()
        time.sleep(3)  # Keeping the delay as requested

        gender_input = sign_up_form.find_element(By.ID, "id_gender1")
        assert gender_input.is_selected(), "❌ Gender selection failed!"
        print("✅ Clicked on 'Mr.' successfully!")

        password_input = sign_up_form.find_element(By.ID, "password")
        password_input.send_keys("1234!!!Tai")
        time.sleep(3)
        print("✅ Added password")

        day_dropdown = sign_up_form.find_element(By.ID, "days")
        month_dropdown = sign_up_form.find_element(By.ID, "months")
        year_dropdown = sign_up_form.find_element(By.ID, "years")

        day_dropdown.send_keys("26")
        month_dropdown.send_keys("August")
        year_dropdown.send_keys("1991")
        time.sleep(2)
        print("✅ Added birthdate")

    except Exception as e:
        print(f"❌ Could not fill in details: {e}")


def fill_address_info(driver):
    """Fill address information during signup."""
    try:
        sign_up_form = driver.find_element(By.CLASS_NAME, "login-form")

        first_name_input = sign_up_form.find_element(By.ID, "first_name")
        first_name_input.send_keys(fake.first_name())
        print("✅ First name added!")

        last_name_input = sign_up_form.find_element(By.ID, "last_name")
        last_name_input.send_keys(fake.last_name())
        print("✅ Last name added!")

        company_input = sign_up_form.find_element(By.ID, "company")
        company_input.send_keys(fake.company())
        print("✅ Company name added!")

        address1_input = sign_up_form.find_element(By.ID, "address1")
        address1_input.send_keys(fake.address())
        print("✅ Address 1 added!")

        address2_input = sign_up_form.find_element(By.ID, "address2")
        address2_input.send_keys(fake.address())
        print("✅ Address 2 added!")

        country_dropdown = sign_up_form.find_element(By.ID, "country")
        country_dropdown.send_keys("Canada")
        time.sleep(2)
        print("✅ Selected Canada!")

        state_input = sign_up_form.find_element(By.ID, "state")
        state_input.send_keys(fake.state())
        print("✅ Added state!")

        city_input = sign_up_form.find_element(By.ID, "city")
        city_input.send_keys(fake.city())
        print("✅ Added city!")

        zipcode_input = sign_up_form.find_element(By.ID, "zipcode")
        zipcode_input.send_keys(fake.zipcode())
        print("✅ Added zipcode!")

        mobile_input = sign_up_form.find_element(By.ID, "mobile_number")
        mobile_input.send_keys(fake.phone_number())
        print("✅ Added mobile number!")

    except Exception as e:
        print(f"❌ Error fulfilling the table: {e}")


def complete_signup(driver):
    """Complete the signup process and submit."""
    try:
        sign_up_form = driver.find_element(By.CLASS_NAME, "login-form")
        submit_button = sign_up_form.find_element(By.TAG_NAME, "button")
        submit_button.click()
        print("✅ Successful register!")
        time.sleep(1)
    except Exception as e:
        print(f"❌ Could not complete signup: {e}")


def verify_account_creation(driver):
    """Verify that the 'Account Created!' message is visible."""
    try:
        account_created = driver.find_element(By.TAG_NAME, "h2")
        if account_created.is_displayed():
            print("✅ 'ACCOUNT CREATED!' message verified successfully!")
        else:
            print("❌ 'ACCOUNT CREATED!' message not displayed!")
    except Exception as e:
        print(f"❌ Could not verify 'ACCOUNT CREATED!' message: {e}")


def click_continue_after_creation(driver):
    """Click the continue button after account creation."""
    try:
        continue_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]")
        continue_button.click()
        print("✅ Clicked 'Continue' after account creation!")
        time.sleep(3)
    except Exception as e:
        print(f"❌ Could not click 'Continue': {e}")


def check_logged_in(driver):
    """Verify that the 'Logged in as username' message is visible."""
    try:
        logged_in_message = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]")
        assert logged_in_message.is_displayed(), "❌ 'Logged in as username' message is not visible!"
        print("✅ 'Logged in as username' message is visible successfully!")
    except Exception as e:
        print(f"❌ 'Logged in as username' not visible: {e}")


def main():
    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Step 1: Navigate to the URL
    driver.get("http://automationexercise.com")

    # Handle cookie consent
    accept_cookie_consent(driver)

    # Step 2: Verify the home page is visible
    try:
        logo = driver.find_element(By.CSS_SELECTOR, "div.logo.pull-left")
        assert logo.is_displayed(), "Home page is not visible!"
        print("✅ Home page is visible successfully!")
    except Exception as e:
        print(f"❌ Test failed: {e}")

    # Step 3: Navigate to signup page
    navigate_to_signup_page(driver)

    # Step 4: Signup process
    signup_user(driver)
    fill_account_info(driver)
    fill_address_info(driver)
    complete_signup(driver)

    # Step 5: Verify account creation
    verify_account_creation(driver)
    click_continue_after_creation(driver)

    # Step 6: Check logged-in status
    check_logged_in(driver)

    # Step 7: Delete the user account
    delete_user_account(driver)

    # Cleanup
    driver.quit()


if __name__ == "__main__":
    main()
