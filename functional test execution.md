
# 1. Test Scenario: Age Verification for Alcoholic Products  

**Description:** Verifies correct age validation and access control for alcoholic products.  

**Priority:** Medium  
**Reporter:** Goran  
**Date:** 05.02.2025  

## Environment  
- **Application:** MarketMate  
- **Page:** Age Verification for Alcoholic Products  
- **Browser:** Chrome  
- **Operating System:** Windows  

## Steps to Reproduce  

| Step# | Action | Expected Outcome | Actual Outcome | OK/NOK | URL | Link to Issue |
|-------|--------|------------------|----------------|--------|-----|---------------|
| 1 | Go to MarketMate homepage | Homepage appears | Homepage appears | OK | [MarketMate URL] | |
| 2 | Search for an alcoholic product | A prompt appears asking for Date of Birth input | A prompt appears asking for Date of Birth input | OK | `/search` | |
| 3 | Enter a valid Date of Birth (e.g., 18-08-2000, 18+ years) | The alcoholic product is displayed | The alcoholic product is displayed | OK | `/product/[ID]` | |
| 4 | Enter an invalid Date of Birth (e.g., 18-08-2006, under 18) | Access is denied with a message | Access is denied with a message | OK | | |
| 5 | Refresh or revisit the page | The system remembers the verified age (if applicable) | The system remembers the verified age | OK | | |
| 6 | Open the alcoholic product page in a new incognito window | The system should prompt for age verification again | The system prompts for age verification again | OK | `/product/[ID]` | |
| 7 | Use browser back/forward buttons after verification | The system should maintain the verified status | The system maintains the verified status | OK | | |

## Expected Result  
The system should properly verify the user’s age, allow or deny access accordingly, and remember the verified status for future visits (except in incognito mode).  

## Actual Result  
The system behaves as expected, correctly verifying the user’s age, allowing or denying access based on the input, and maintaining the verification status where applicable.  

![DOB 17y 364d](https://github.com/user-attachments/assets/6e1e6267-e2b0-4985-b1bb-ed3980e1a895)  
![Under 18 Notification](https://github.com/user-attachments/assets/833a93d3-1e75-4958-b89a-e954acd3f2c7)  

---

# 2. Test Scenario: Shipping Cost Calculation  

**Description:** Validates if shipping cost adjusts dynamically based on basket total (threshold 20 EUR).  

**Date:** 05.02.2025  
**Tester:** Goran  
**Priority:** Medium  

## Environment  
- **Application:** MarketMate  
- **Feature:** Shipping Cost Calculation  
- **Browser:** Chrome  
- **Operating System:** Windows  

## Test Steps  

| Step# | Action | Expected Outcome | Actual Outcome | OK/NOK | URL | Notes |  
|-------|--------|------------------|----------------|--------|-----|-------|  
| 1 | Go to MarketMate homepage | Homepage appears | Homepage appears | OK | [MarketMate URL] | |  
| 2 | Add items to the basket totaling **less than 20 EUR** | Shipping cost is **5 EUR** | Shipping cost is **5 EUR** | OK | `/cart` | |  
| 3 | Add more items to reach **20 EUR or more** | Shipping cost is **0 EUR (free shipping applied)** | Shipping cost is **0 EUR** | OK | `/cart` | |  
| 4 | Remove items so that the total is **below 20 EUR again** | Shipping cost **should update back to 5 EUR** | Shipping cost **does not update back to 5 EUR** | NOK | `/cart` | Issue found |  

## Expected Result  
- If the total basket value is **below 20 EUR**, a **5 EUR shipping fee** should apply.  
- If the total reaches **20 EUR or more**, **free shipping** should be applied.  
- If the total drops below **20 EUR again**, the **5 EUR shipping fee** should be reapplied.  

## Actual Result  
NOK The system **fails to reapply the 5 EUR shipping cost** when the basket value drops below 20 EUR. **Issue needs investigation.**  

![Shipping cost under 20Eur](https://github.com/user-attachments/assets/2ffa8f32-3429-4457-a033-b9a42f40aa3f)  
![Shipping cost over 20Eur](https://github.com/user-attachments/assets/8a8b23b1-fbfe-4942-b8a7-fc5838c99346)  
![Shipping cost error when taking out items](https://github.com/user-attachments/assets/6bbba49f-060d-4551-bc96-a306b52c7851)  

---


# 3. Test Scenario: Review Text Not Being Saved When Leaving a Review  

**Description:** Checks if the review text is correctly stored when a user submits a product review.  

**Priority:** Medium  
**Reporter:** Goran  
**Date:** 05.02.2025  

## Environment  
- **Application:** MarketMate  
- **Page:** Product Review  
- **Browser:** Chrome  
- **Operating System:** Windows  

## Steps to Reproduce  

| Step# | Action | Expected Outcome | Actual Outcome | OK/NOK | URL | Link to Issue |  
|-------|--------|-----------------|----------------|--------|-----|--------------|  
| 1 | Go to the Market Mate example Product page | Product page appears | Product page appears | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e | |  
| 2 | Click on "Leave Review" | Review section opens | Review section opens | OK | /product/[ID] | |  
| 3 | Fill in any review text and save review | Review text is saved with stars | Only star evaluation is saved, no text saved | NOK | /product/[ID] | [Link to issue] |  

## Expected Result  
Product review text should be saved in the review body.  

## Actual Result  
No text is saved in the review body.  

![Review 1](https://github.com/user-attachments/assets/a802242b-d7d8-4915-aab5-cd1e98f94fbd)  
![Review 2](https://github.com/user-attachments/assets/1029bea2-4d18-470b-90d1-9d5b6e31057f)  

---  

# 4. Test Scenario: Valid Rating Submission (4-Star Rating)  

**Description:** Ensures that a 4-star rating is successfully saved and persists after a page refresh.  

## Steps to Reproduce  

| Step# | Action | Expected Outcome | OK/NOK | URL | Link to Issue |  
|-------|-----------------------------------------------|---------------------------------|--------|----------------------------------------------|---------------|  
| 1 | Go to the product page | Product page appears | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e | |  
| 2 | Select a 4-star rating | 4-star rating is selected | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e | |  
| 3 | Submit the rating | Rating is successfully saved | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e | |  
| 4 | Refresh the page | The 4-star rating is still displayed | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e | |  

## Expected Result  
The 4-star rating should be saved and persist after refreshing the page.  

## Actual Result  
The rating is successfully saved and displayed correctly after page refresh.  

![Image](https://github.com/user-attachments/assets/81af3235-a687-43a9-b1db-a574e75aa4e3)  

---  

# 5. Test Scenario: Lowest Valid Rating (1-Star Rating)  

**Description:** Ensures that a 1-star rating is correctly saved and displayed.  

## Steps to Reproduce  

| Step# | Action | Expected Outcome | OK/NOK | URL | Link to Issue |  
|-------|-----------------------------------------------|---------------------------------|--------|----------------------------------------------|---------------|  
| 1 | Go to the product page | Product page appears | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c8 | |  
| 2 | Select a 1-star rating | 1-star rating is selected | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c8 | |  
| 3 | Submit the rating | Rating is successfully saved | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c8 | |  
| 4 | Refresh the page | The 1-star rating is still displayed | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c8 | |  

## Expected Result  
The 1-star rating should be saved and persist after refreshing the page.  

## Actual Result  
The rating is successfully saved and displayed correctly after page refresh.  

![Image](https://github.com/user-attachments/assets/34e89b9e-2cfa-4197-91c4-f64f504e5b02)  

---  


# 6. Test Scenario: No Rating Selected  

**Description:** Verifies that a user cannot submit a product review without selecting a rating.  

**Priority:** Medium  
**Tester:** Goran  
**Date:** 05.02.2025  

## Environment  
- **Application:** MarketMate  
- **Feature:** Product Review Submission  
- **Browser:** Chrome  
- **Operating System:** Windows  

## Test Steps  

| Step# | Action | Expected Outcome | Actual Outcome | OK/NOK | URL | Notes |  
|-------|-----------------------------------------------|--------------------------------------------------------|----------------|--------|-----|-------|  
| 1 | Go to the product page | Product page appears | Product page appears | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c6 | |  
| 2 | Leave the rating section unselected | Rating is not selected | Rating is not selected | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c6 | |  
| 3 | Submit the review without selecting a rating | The system shows the error message: "Invalid input for the field 'Rating'. Please check your input." | The system shows the error message | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c6 | |  

## Expected Result  
The system should prevent the submission of a product review without selecting a rating and display an error message.  

## Actual Result  
The system correctly prevents submitting a review without selecting a rating and displays the expected error message.  

![Image](https://github.com/user-attachments/assets/0747a61e-a0df-4662-9da4-d1f41f957c89)  

---  

# 7. Test Scenario: Average Rating Calculation (Multiple User Ratings)  

**Description:** Ensures that the average rating is correctly calculated and updated after new ratings.  

## Test Steps  

| Step# | Action | Expected Outcome | Actual Outcome | OK/NOK | URL | Notes |  
|-------|----------------------------------------------------------|----------------------------------------------------------|----------------|--------|-----|-------|  
| 1 | Go to the product page | Product page appears successfully | Product page appears successfully | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1 | |  
| 2 | Check the current average rating (calculated from 8 reviews: 5, 1, 1, 4, 2, 5, 3, 4) | The average rating is displayed as 3.3 stars | The average rating is displayed as 3.3 stars | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1 | |  
| 3 | Submit a 5-star review for the product | A 5-star review is submitted and saved | A 5-star review is successfully saved and submitted | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1 | |  
| 4 | Check the updated average rating after the new 5-star review | The new average rating should be 3.3 stars | The average rating correctly updates to 3.3 stars | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1 | |  

## Expected Result  
The system should correctly calculate and update the average rating based on existing reviews and new submissions.  

## Actual Result  
The system correctly calculates and updates the average rating after a new 5-star review is submitted.  

![Image](https://github.com/user-attachments/assets/295bcb45-1104-437a-a229-c7a92e1d105f)  

---  

# 8. Test Scenario: Age Verification Field Left Blank  

**Description:** Ensures that users cannot proceed without entering a birthdate when required.  

## Test Steps  

| Step# | Action | Expected Outcome | Actual Outcome | OK/NOK | URL | Notes |  
|-------|------------------------------------------------------------|------------------------------------------------------------|----------------|--------|-----|-------|  
| 1 | Go to the homepage of MarketMate | Homepage appears | Homepage appears | OK | [https://grocerymate.masterschool.com/store | |  
| 2 | Search for a restricted product (e.g., alcoholic beverage) | A prompt asking for date of birth appears | Prompt appears | OK | [https://grocerymate.masterschool.com/search | |  
| 3 | Leave the Date of Birth field blank and attempt to proceed | Error message: "You need to be +18 to see some products. Please enter your birth date." | Error message displayed | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1 | |  

## Expected Result  
If the Date of Birth field is left blank, an error message should appear.  

## Actual Result  
The system correctly displays the error message.  

![Image](https://github.com/user-attachments/assets/f6facc2a-f675-46e7-8e24-4acf12fb579d)  

---  

# 9. Test Scenario: Maximum Review Character Limit Validation  

**Description:** Ensures that users cannot enter more characters than allowed in product reviews.  

## Test Steps  

| Step# | Action | Expected Outcome | Actual Outcome | OK/NOK | URL | Notes |  
|-------|--------|-----------------|---------------|--------|-----|-------|  
| 1 | Go to the product description input field | The input field is displayed and allows text entry | The input field is displayed and allows text entry | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a8e | |  
| 2 | Enter characters up to the maximum allowed limit | The system accepts input up to the limit | The system accepts input up to the limit | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a8e | |  
| 3 | Try entering additional characters beyond the limit | The system prevents further input and displays the notification: "You cannot tell us more about this product." | The system prevents further input and displays the notification | OK | [https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a8e | |  

## Expected Result  
The system should prevent additional input beyond the allowed character limit and show a notification.  

## Actual Result  
The system prevents additional input and displays the correct notification.  

![Image](https://github.com/user-attachments/assets/f76e1bfb-c19b-441a-bd25-46352ef4f8ae)  

---  


https://github.com/user-attachments/assets/364a39e5-2799-4bc8-9464-214ab28e0f34

https://github.com/user-attachments/assets/c3e8a455-e61a-46d1-86cb-8cafd40a92d6

https://github.com/user-attachments/assets/95def9aa-e1fd-4c88-90cb-3c764a12b163

https://github.com/user-attachments/assets/3ea6cc97-6641-4ff7-8c0b-e4f5ce7b789e

https://github.com/user-attachments/assets/de7dd737-7e01-44d0-a0f6-aa27f31d323a

https://github.com/user-attachments/assets/432df989-6622-47aa-9afa-d08a5b935e67

https://github.com/user-attachments/assets/71c1bc8f-290d-4cc0-b335-a38497b456a2

https://github.com/user-attachments/assets/dcc53a49-16c7-4f7a-ac5b-f431d126a5d8

https://github.com/user-attachments/assets/2bf043fc-2ee9-46f6-b48c-bc12b1178cf9

https://github.com/user-attachments/assets/bbc837dd-783b-4afb-8ad0-ef7ca51fa757

https://github.com/user-attachments/assets/0326ba7d-b1c8-4b8f-b157-928b508ec442

https://github.com/user-attachments/assets/ca3dfb46-4048-49be-8629-758ebbf4327d

https://github.com/user-attachments/assets/f84305be-a794-4a65-8b0c-d1149473f26f
