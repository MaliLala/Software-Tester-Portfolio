# Test Case Design – GroceryMate Webshop  

This document outlines the planned test cases for the upcoming release of new features in the GroceryMate webshop. The goal is to ensure that each feature functions correctly, meets business requirements, and provides a seamless user experience.  

The focus is on testing the following features:  
- Product Rating System  
- Age Verification for Alcoholic Products  
- Shipping Cost Adjustments  

---

## 1. Product Rating System  

**Technique:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), and Error Guessing.  
**Purpose:** Ensure users can leave accurate ratings and that ratings are calculated and displayed correctly.  

### Test Cases  

1. **Valid Rating Submission**  
   - **Input:** Submit a 4-star rating for a product.  
   - **Expected Outcome:** Rating is successfully saved and displayed as 4 stars.  

2. **Lowest Valid Rating**  
   - **Input:** Submit a 1-star rating.  
   - **Expected Outcome:** Rating is accepted without issues.  

3. **Invalid Rating Submission**  
   - **Input:** Submit a 6-star rating.  
   - **Expected Outcome:** Error message: "Invalid rating value."  

4. **No Rating Selected**  
   - **Input:** Attempt to submit without selecting any rating.  
   - **Expected Outcome:** Error message: "Please choose a rating."  

5. **Average Rating Calculation**  
   - **Input:** Three users leave ratings of 3, 4, and 5 stars.  
   - **Expected Outcome:** The product displays an average rating of 4 stars.  

---

## 2. Age Verification for Alcoholic Products  

**Technique:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), and Error Guessing.  
**Purpose:** Ensure age verification works as expected and blocks underage users from accessing restricted products.  

### Test Cases  

1. **Access Granted for Exactly 18 Years Old**  
   - **Input:** Date of birth set to exactly 18 years ago.  
   - **Expected Outcome:** Access to alcoholic products is granted.  

2. **Access Denied for Underage User**  
   - **Input:** Date of birth set to 17 years and 364 days ago.  
   - **Expected Outcome:** Access denied with a message: "You must be 18+ to view this content."  

3. **Date of Birth Field Left Blank**  
   - **Input:** Leave the Date of Birth field empty.  
   - **Expected Outcome:** Error message: "Date of Birth is required."  

---

## 3. Shipping Cost Changes  

**Technique:** Equivalence Partitioning (EP), Boundary Value Analysis (BVA), and Error Guessing.  
**Purpose:** Verify that shipping fees are applied correctly based on the order total and that free shipping is granted at the threshold.  

### Test Cases  

1. **Shipping Fee for Orders Below $20**  
   - **Input:** Order total = $30.  
   - **Expected Outcome:** Shipping fee is applied.  

2. **Free Shipping at $20 Threshold**  
   - **Input:** Order total = $20.  
   - **Expected Outcome:** No shipping fee is applied.  

3. **Service Unavailability During Checkout**  
   - **Input:** Attempt to check out when the shipping service is down.  
   - **Expected Outcome:** Error message: "Unable to calculate shipping. Try again later."  
