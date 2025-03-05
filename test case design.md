# **Test Case Design – MarketMate Webshop**

This document outlines the planned test cases for the upcoming release of new features in the MarketMate webshop. The goal is to ensure that each feature functions correctly, meets business requirements, and provides a seamless user experience.

The focus is on testing the following features:

- Product Rating System
- Age Verification for Alcoholic Products
- Shipping Cost Adjustments
- User Registration

---

## **1. Product Rating System**

**Technique:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), and Error Guessing.  
**Purpose:** Ensure users can leave accurate ratings and that ratings are calculated and displayed correctly.

---

### **Test Case 1: Valid Rating Submission (4-Star Rating)**

**Test Case Objective:**  
To verify that users can successfully submit a 4-star rating for a product, and that this rating is saved and displayed properly.

**Test Case Steps:**  
1. Navigate to the product page.  
2. Select the 4-star rating option (this should highlight the 4th star).  
3. Submit the rating.  
4. Refresh the page to ensure the rating persists.

**Expected Result:**  
After refreshing the page, the 4-star rating should be displayed, confirming that it was successfully saved.

---

### **Test Case 2: Lowest Valid Rating (1-Star Rating)**

**Test Case Objective:**  
To ensure that users can submit a 1-star rating, and that it is correctly saved and displayed in the system.

**Test Case Steps:**  
1. Navigate to the product page.  
2. Select the 1-star rating option (only the first star should be filled).  
3. Submit the rating.  
4. Refresh the page to confirm that the 1-star rating persists.

**Expected Result:**  
The 1-star rating should remain visible after the page refresh, confirming that the system correctly saved and displayed the lowest rating.

---

### **Test Case 3: No Rating Selected**

**Test Case Objective:**  
To ensure that the system prevents users from submitting a review without selecting a rating, and provides an appropriate error message.

**Test Case Steps:**  
1. Navigate to the product page.  
2. Leave the rating section unselected (do not choose a star).  
3. Attempt to submit the review.

**Expected Result:**  
The system should display an error message that says, "Invalid input for the field 'Rating'. Please check your input."

---

### **Test Case 4: Average Rating Calculation (Multiple User Ratings)**

**Test Case Objective:**  
To confirm that the system correctly calculates the average rating based on multiple submitted ratings. Ensure that the average is updated accurately when a new rating is added.

**Test Case Steps:**  
1. Navigate to the product page and note the current average rating (calculated from 8 previous reviews: 5, 1, 1, 4, 2, 5, 3, 4).  
2. Submit a 5-star review for the product.  
3. After submitting, refresh the page and check the updated average rating.

**Expected Result:**  
The new average rating should be calculated correctly based on the new total of ratings. The correct average will be displayed as 3.3 stars after the addition of the 5-star rating.

---

## **2. Age Verification for Alcoholic Products**

**Technique:** Equivalence Partitioning (EP) and Boundary Value Analysis (BVA).  
**Purpose:** Ensure that users are properly verified for age before accessing alcoholic products.

---

### **Test Case 5: Access Granted for Exactly 18 Years Old**

**Test Case Objective:**  
To verify that users who are exactly 18 years old are granted access to view and purchase alcoholic products.

**Test Case Steps:**  
1. Go to the homepage of MarketMate.  
2. Search for an alcoholic product (e.g., wine or beer).  
3. Enter a valid date of birth (e.g., 18 years old).

**Expected Result:**  
The system should grant access and allow the user to view and purchase the alcoholic product.

---

### **Test Case 6: Access Denied for Underage User**

**Test Case Objective:**  
To ensure that users who are underage (less than 18 years old) are denied access to alcoholic products and prevented from proceeding to the product page.

**Test Case Steps:**  
1. Go to the homepage of MarketMate.  
2. Search for an alcoholic product.  
3. Enter an invalid date of birth (e.g., 17 years old).

**Expected Result:**  
The system should block access to the product and display a message stating that the user must be 18 or older to access the product.

---

### **Test Case 7: Age Verification Field Left Blank**

**Test Case Objective:**  
To check how the system handles the scenario when the user leaves the Date of Birth field blank during the age verification process.

**Test Case Steps:**  
1. Go to the homepage of MarketMate.  
2. Search for an alcoholic product.  
3. Leave the Date of Birth field blank and attempt to proceed to the product page.

**Expected Result:**  
The system should display the error message: "You need to be +18 to see some products. Please enter your birth date."

---

## **3. Shipping Cost Calculation**

**Technique:** Equivalence Partitioning (EP) and Boundary Value Analysis (BVA).  
**Purpose:** Ensure that shipping costs are applied correctly based on the cart total.

---

### **Test Case 8: Shipping Fee for Orders Below $20**

**Test Case Objective:**  
To ensure that the system correctly applies a shipping fee for orders with a total below $20.

**Test Case Steps:**  
1. Add items to the shopping basket, ensuring the total is less than $20.  
2. Check the shipping cost during checkout.

**Expected Result:**  
The shipping fee should be correctly applied as 5 EUR (shipping cost for orders below $20).

---

### **Test Case 9: Free Shipping at $20 Threshold**

**Test Case Objective:**  
To verify that no shipping cost is applied when the total value of the cart reaches or exceeds $20.

**Test Case Steps:**  
1. Add items to the shopping basket, ensuring the total is $20 or more.  
2. Check the shipping cost during checkout.

**Expected Result:**  
Free shipping should apply, meaning the shipping cost will be 0 EUR.

---

### **Test Case 10: Shipping Fee Adjustment When Order Total Changes**

**Test Case Objective:**  
To ensure that the shipping cost dynamically adjusts when the order total changes, crossing the $20 threshold.

**Test Case Steps:**  
1. Add items to the basket totaling less than $20 and check the shipping cost (should be 5 EUR).  
2. Add more items to reach a total of $20 or more and check the updated shipping cost (should be 0 EUR).  
3. Remove items to bring the total back below $20 and verify that the shipping cost changes back to 5 EUR.

**Expected Result:**  
The shipping fee should adjust automatically based on the total value of the cart, and should be correctly reflected at each stage of adding or removing items.

---

## **4. User Registration**

**Technique:** Error Guessing.  
**Purpose:** Ensure that the system prevents multiple users from registering with the same email address.

---

### **Test Case 11: Multiple Users Can Register with the Same Email Address**

**Test Case Objective:**  
To verify that the system does not allow multiple users to register with the same email address to prevent data duplication or misuse.

**Test Case Steps:**  
1. Go to the registration page of MarketMate.  
2. Register a new user account with a valid email address (e.g., "user@example.com").  
3. Log out and attempt to register another user with the same email address.  
4. Try to complete the registration process.

**Expected Result:**  
The system should prevent the second registration attempt and display an error message, such as "This email address is already in use."

---

