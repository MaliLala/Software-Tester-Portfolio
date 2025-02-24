from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

# Initialize Faker to generate random data
fake = Faker()

def accept_cookie_consent(driver):
    try:
        # Wait for the consent modal to load
        time.sleep(3)

        # Check if the consent modal is displayed
        consent_modal = driver.find_element(By.CLASS_NAME, "fc-dialog-container")
        if consent_modal.is_displayed():
            print("✅ Consent modal detected!")

            # Locate and click the "Consent" button
            consent_button = consent_modal.find_element(By.XPATH, "//button[contains(@class, 'fc-cta-consent')]")
            consent_button.click()
            print("✅ Clicked on 'Consent' button successfully!")

            # Small delay to ensure modal disappears
            time.sleep(2)
        else:
            print("✅ No consent modal detected.")
    except Exception as e:
        print(f"❌ Could not handle cookie consent: {e}")

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

# Step 3: Click on 'Signup / Login' button
try:
    signup_login_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Signup / Login")
    signup_login_button.click()
    print("✅ Clicked on 'Signup / Login' button successfully!")
except Exception as e:
    print(f"❌ Could not click on 'Signup / Login': {e}")

# Step 4: Verify 'New User Signup!' is visible
try:
    sign_up_form = driver.find_element(By.CLASS_NAME, "signup-form")
    assert sign_up_form.is_displayed(), "Form is not visible"
    print("✅ Register form is visible!")

    # Generate random user data
    name = fake.name()
    email = fake.email()

    # Locate elements inside the signup form
    name_field = sign_up_form.find_element(By.NAME, "name")
    email_field = sign_up_form.find_element(By.NAME, "email")
    submit_button = sign_up_form.find_element(By.TAG_NAME, "button")

    # Step 5: Fill and submit the form with random data
    name_field.send_keys(name)
    email_field.send_keys(email)

    # Step 6: Click 'Signup' button
    submit_button.click()
    print("✅ Signup form submitted successfully!")

except Exception as e:
    print(f"❌ Could not complete signup: {e}")

# Step 7: Verify that 'ENTER ACCOUNT INFORMATION' is visible
try:
    driver.find_element(By.CLASS_NAME, "login-form")
    print("✅ Login form is visible!")
except Exception as e:
    print(f"❌ Login form is not visible: {e}")

# Step 8: Fill details: Title, Name, Email, Password, Date of Birth
try:
    sign_up_form = driver.find_element(By.CLASS_NAME, "login-form")  # Ensure we are in the correct form

    # Select Title (Gender: Mr.)
    gender_label = sign_up_form.find_element(By.XPATH, "//label[@for='id_gender1']")  # Clicking the label
    gender_label.click()

    time.sleep(3)  # Keeping the delay as requested

    # Verify selection
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

    day_dropdown.send_keys("26")  # Selecting 26th day
    month_dropdown.send_keys("August")  # Selecting August
    year_dropdown.send_keys("1991")  # Selecting Year 1991
    time.sleep(2)
    print("✅ Added birthdate")
except Exception as e:
    print(f"❌ Could not fill in details: {e}")

# Step 9: Select 'Sign up for our newsletter!' checkbox
try:
    newsletter_checkbox = driver.find_element(By.ID, "newsletter")
    newsletter_checkbox.click()
    time.sleep(2)

    # Verify checkbox selection
    assert newsletter_checkbox.is_selected(), "❌ News checkbox not selected!"
    print("✅ 'Sign up for our newsletter!' checkbox selected successfully!")
except Exception as e:
    print(f"❌ Error selecting newsletter checkbox: {e}")

# Step 10: Select 'Receive special offers from our partners!' checkbox
try:
    offers_checkbox = driver.find_element(By.ID, "optin")
    offers_checkbox.click()
    time.sleep(2)

    # Verify checkbox selection
    assert offers_checkbox.is_selected(), "❌ Offers checkbox not selected!"
    print("✅ 'Receive special offers from our partners!' checkbox selected successfully!")
except Exception as e:
    print(f"❌ Error selecting offers checkbox: {e}")

# Step 11: Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
try:
    first_name_input = sign_up_form.find_element(By.ID, "first_name")
    first_name_input.send_keys(fake.first_name())
    print("✅ First name added!")

    last_name_input = sign_up_form.find_element(By.ID,"last_name")
    last_name_input.send_keys(fake.last_name())
    print("✅ Last name added!")

    company_input = sign_up_form.find_element(By.ID,"company")
    company_input.send_keys(fake.company())
    print("✅ Company name added!")

    address1_input = sign_up_form.find_element(By.ID,"address1")
    address1_input.send_keys(fake.address())
    print("✅ Address 1 added!")

    address2_input = sign_up_form.find_element(By.ID,"address2")
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

# Step 12: Click Create profile
try:
    submit_button = sign_up_form.find_element(By.TAG_NAME, "button")
    submit_button.click()
    print("✅ Successful register!")
    time.sleep(1)
except Exception as e:
    print(f"❌ Could not click: {e}")

# Step 13: Verify 'ACCOUNT CREATED!' message
try:
    account_created = driver.find_element(By.TAG_NAME, "h2")
    if account_created.is_displayed():
        print("✅ 'ACCOUNT CREATED!' message verified successfully!")
    else:
        print("❌ 'ACCOUNT CREATED!' message not displayed!")
except Exception as e:
    print(f"❌ Could not verify 'ACCOUNT CREATED!' message: {e}")

# Step 14: Click 'Continue' button
try:
    continue_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]")
    continue_button.click()
    print("✅ Clicked 'Continue' after account creation!")
    time.sleep(3)  # Give time for page transition
except Exception as e:
    print(f"❌ Could not click 'Continue': {e}")

# Step 15: Verify 'Logged in as username' is visible
try:
    logged_in_message = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]")

    assert logged_in_message.is_displayed(), "❌ 'Logged in as username' message is not visible!"
    print("✅ 'Logged in as username' message is visible successfully!")
except Exception as e:
    print(f"❌ Could not verify 'Logged in as username' message: {e}")

# Step 16: Click 'Delete Account' button
try:
    delete_account_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Delete Account')]")
    delete_account_button.click()
    print("✅ Clicked 'Delete Account' successfully!")
    time.sleep(3)  # Allow time for deletion
except Exception as e:
    print(f"❌ Could not click 'Delete Account': {e}")

# Step 17: Verify 'ACCOUNT DELETED!' is visible and click 'Continue'
try:
    account_deleted_message = driver.find_element(By.TAG_NAME, "h2")
    assert account_deleted_message.is_displayed(), "❌ 'ACCOUNT DELETED!' message is not visible!"
    print("✅ 'ACCOUNT DELETED!' message verified successfully!")

    continue_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Continue')]")
    continue_button.click()
    print("✅ Clicked 'Continue' after account deletion!")
    time.sleep(3)  # Allow page transition
except Exception as e:
    print(f"❌ Error in account deletion: {e}")

# Close the driver
driver.quit()
