# Test Scenario: Age Verification for Alcoholic Products

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
| 1 | Go to MarketMate homepage | Homepage appears | Homepage appears | ✅ | [MarketMate URL] | |
| 2 | Search for an alcoholic product | A prompt appears asking for Date of Birth input | A prompt appears asking for Date of Birth input | ✅ | `/search` | |
| 3a | Enter a valid Date of Birth (e.g., 18-08-2000, 18+ years) | The alcoholic product is displayed | The alcoholic product is displayed | ✅ | `/product/[ID]` | |
| 3b | Enter an invalid Date of Birth (e.g., 18-08-2006, exactly 17 years and 364 days old) | Access is denied with a message | Access is denied with a message | ✅ | | |
| 4 | Refresh or revisit the page | The system remembers the verified age (if applicable) | The system remembers the verified age | ✅ | | |
| 5 | Open the alcoholic product page in a new incognito window | The system should prompt for age verification again | The system prompts for age verification again | ✅ | `/product/[ID]` | |
| 6 | Use browser back/forward buttons after verification | The system should maintain the verified status | The system maintains the verified status | ✅ | | |

## Expected Result  
The system should properly verify the user’s age, allow or deny access accordingly, and remember the verified status for future visits (except in incognito mode).  

## Actual Result  
The system behaves as expected, correctly verifying the user’s age, allowing or denying access based on the input, and maintaining the verification status where applicable.  

![DOB 17y 364d](https://github.com/user-attachments/assets/6e1e6267-e2b0-4985-b1bb-ed3980e1a895)
![Under 18 Notification](https://github.com/user-attachments/assets/833a93d3-1e75-4958-b89a-e954acd3f2c7)





# Test Scenario: Shipping Cost Calculation  

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
|-------|--------|-----------------|----------------|--------|-----|-------|  
| 1 | Go to MarketMate homepage | Homepage appears | Homepage appears | ✅ | [MarketMate URL] | |  
| 2 | Add items to the basket totaling **less than 20 EUR** | Shipping cost is **5 EUR** | Shipping cost is **5 EUR** | ✅ | `/cart` | |  
| 3 | Add more items to reach **20 EUR or more** | Shipping cost is **0 EUR (free shipping applied)** | Shipping cost is **0 EUR** | ✅ | `/cart` | |  
| 4 | Remove items so that the total is **below 20 EUR again** | Shipping cost **should update back to 5 EUR** | Shipping cost **does not update back to 5 EUR** | ❌ | `/cart` | Issue found |  

## Expected Result  
- If the total basket value is **below 20 EUR**, a **5 EUR shipping fee** should apply.  
- If the total reaches **20 EUR or more**, **free shipping** should be applied.  
- If the total drops below **20 EUR again**, the **5 EUR shipping fee** should be reapplied.  

## Actual Result  
❌ The system **fails to reapply the 5 EUR shipping cost** when the basket value drops below 20 EUR. **Issue needs investigation.**  

![Shipping cost under 20Eur](https://github.com/user-attachments/assets/2ffa8f32-3429-4457-a033-b9a42f40aa3f)
![Shipping cost over 20Eur](https://github.com/user-attachments/assets/8a8b23b1-fbfe-4942-b8a7-fc5838c99346)
![Shipping cost error when taking out items](https://github.com/user-attachments/assets/6bbba49f-060d-4551-bc96-a306b52c7851)



# Test Scenario: Review Text not being saved when leaving a review.

**Priority:** Medium  
**Reporter:** Goran  
**Date:** 05.02.2025  

**Environment:** Test  
**Application:** Market Mate  
**Page:** Product Review  
**Browser:** Chrome  
**Operating System:** Windows  

### Steps to Reproduce  

| Step# | Action | Expected Outcome | Actual Outcome | OK/NOK | URL | Link to Issue |  
|-------|--------|-----------------|----------------|--------|-----|--------------|  
| 1 | Go to the Market Mate example Product page. | Product page appears | Product page appears | OK | [(https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e)] | |  
| 2 | Click on "Leave Review" | Review section opens | Review section opens | OK | /product/[ID] | |  
| 3 | Fill in any review text and save review. | Review text is saved with stars | Only star evaluation is saved, no text saved | NOK | /product/[ID] | [Link to issue] |  

### Expected Result:  
Product review text should be saved in the review body.

### Actual Result:  
No text is saved in the review body.


![Review 1](https://github.com/user-attachments/assets/a802242b-d7d8-4915-aab5-cd1e98f94fbd)
![Review 2](https://github.com/user-attachments/assets/1029bea2-4d18-470b-90d1-9d5b6e31057f)
![Review 3](https://github.com/user-attachments/assets/ca3dfb46-4048-49be-8629-758ebbf4327d)
![Review 4](https://github.com/user-attachments/assets/364a39e5-2799-4bc8-9464-214ab28e0f34)



### Test Case: Valid Rating Submission (4-Star Rating)

**Description:**  
This test case verifies that when a user submits a 4-star rating for a product, the rating is successfully saved and persists after the page is refreshed.

| Step# | Action                                        | Expected Outcome                                | OK/NOK | URL                                          | Link to Issue |
|-------|-----------------------------------------------|------------------------------------------------|--------|----------------------------------------------|---------------|
| 1     | Go to the product page                        | Product page appears                            | OK     | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e) |               |
| 2     | Select a 4-star rating                        | 4-star rating is selected                       | OK     | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e) |               |
| 3     | Submit the rating                             | Rating is successfully saved                    | OK     | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e) |               |
| 4     | Refresh the page                              | The 4-star rating is still displayed            | OK     | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a4e) |               |

**Result:** The 4-star rating is successfully saved and persists after page refresh.



![Image](https://github.com/user-attachments/assets/81af3235-a687-43a9-b1db-a574e75aa4e3)
![Image](https://github.com/user-attachments/assets/dcc53a49-16c7-4f7a-ac5b-f431d126a5d8)
![Image](https://github.com/user-attachments/assets/71c1bc8f-290d-4cc0-b335-a38497b456a2)



### Test Case: Lowest Valid Rating (1-Star Rating)

**Description:**  
This test case verifies that when a user submits a 1-star rating for a product, the rating is successfully saved and displayed correctly.

| Step# | Action                                        | Expected Outcome                                | OK/NOK | URL                                          | Link to Issue |
|-------|-----------------------------------------------|------------------------------------------------|--------|----------------------------------------------|---------------|
| 1     | Go to the product page                        | Product page appears                            | OK     | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c8) |               |
| 2     | Select a 1-star rating                        | 1-star rating is selected                       | OK     | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c8) |               |
| 3     | Submit the rating                             | Rating is successfully saved                    | OK     | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c8) |               |
| 4     | Refresh the page                              | The 1-star rating is still displayed            | OK     | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c8) |               |

**Result:** The 1-star rating is successfully saved and persists after page refresh.

![Image](https://github.com/user-attachments/assets/34e89b9e-2cfa-4197-91c4-f64f504e5b02)
![Image](https://github.com/user-attachments/assets/2bf043fc-2ee9-46f6-b48c-bc12b1178cf9)
![Image](https://github.com/user-attachments/assets/3ea6cc97-6641-4ff7-8c0b-e4f5ce7b789e)
![Image](https://github.com/user-attachments/assets/0326ba7d-b1c8-4b8f-b157-928b508ec442)



# Test Scenario: No Rating Selected  

**Date:** 05.02.2025  
**Tester:** Goran  
**Priority:** Medium  

## Environment  
- **Application:** MarketMate  
- **Feature:** Product Review Submission  
- **Browser:** Chrome  
- **Operating System:** Windows  

## Test Steps  

| Step# | Action                                        | Expected Outcome                                        | Actual Outcome | OK/NOK | URL | Notes |  
|-------|-----------------------------------------------|--------------------------------------------------------|----------------|--------|-----|-------|  
| 1 | Go to the product page                        | Product page appears                                    | Product page appears | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c6) | |  
| 2 | Leave the rating section unselected           | Rating is not selected                                  | Rating is not selected | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c6) | |  
| 3 | Submit the review without selecting a rating  | The system shows the error message: "Invalid input for the field 'Rating'. Please check your input." | The system shows the error message: "Invalid input for the field 'Rating'. Please check your input." | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c6) | |  
| 4 | Verify that the error message is displayed    | The error message "Invalid input for the field 'Rating'. Please check your input." is shown | The error message "Invalid input for the field 'Rating'. Please check your input." is shown | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479c6) | |

## Expected Result  
The system should prevent the submission of a product review without selecting a rating and should display an error message:  
"Invalid input for the field 'Rating'. Please check your input."  

## Actual Result  
The system correctly prevents submitting a review without selecting a rating and displays the expected error message:  
"Invalid input for the field 'Rating'. Please check your input."  

## Screenshots  
![Image](https://github.com/user-attachments/assets/0747a61e-a0df-4662-9da4-d1f41f957c89)  
![Image](https://github.com/user-attachments/assets/c3e8a455-e61a-46d1-86cb-8cafd40a92d6)



# Test Scenario: Average Rating Calculation (Multiple User Ratings)

**Date:** 05.02.2025  
**Tester:** Goran  
**Priority:** Medium  

## Environment  
- **Application:** MarketMate  
- **Feature:** Average Rating Calculation  
- **Browser:** Chrome  
- **Operating System:** Windows  

## Test Steps  

| Step# | Action                                                   | Expected Outcome                                          | Actual Outcome | OK/NOK | URL | Notes |  
|-------|----------------------------------------------------------|----------------------------------------------------------|----------------|--------|-----|-------|  
| 1 | Go to the product page                                   | Product page appears successfully.                        | Product page appears successfully.                         | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1) | |  
| 2 | Check the current average rating (calculated from 8 reviews: 5, 1, 1, 4, 2, 5, 3, 4) | The average rating is displayed as 3.3 stars (rounded to one decimal place). | The average rating is displayed as 3.3 stars.             | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1) | |  
| 3 | Submit a 5-star review for the product                    | A 5-star review is submitted and saved.                   | A 5-star review is successfully saved and submitted.        | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1) | |  
| 4 | Check the updated average rating after the new 5-star review | The new average rating should be 3.3 stars (calculated as (5 + 1 + 1 + 4 + 2 + 5 + 3 + 4 + 5) / 9 = 3.3). | The average rating correctly updates to 3.3 stars.        | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1) | |

## Expected Result  
The system should correctly calculate and update the average rating based on the existing reviews and any new submissions. After submitting a 5-star review, the average should reflect the updated value of 3.3 stars.  

## Actual Result  
The system correctly calculates and updates the average rating after a new 5-star review is submitted. The updated average rating is correctly displayed as 3.3 stars.  

## Screenshots  
![Image](https://github.com/user-attachments/assets/295bcb45-1104-437a-a229-c7a92e1d105f)  
![Image](https://github.com/user-attachments/assets/de7dd737-7e01-44d0-a0f6-aa27f31d323a)  
![Image](https://github.com/user-attachments/assets/f84305be-a794-4a65-8b0c-d1149473f26f)



# Test Scenario: Age Verification Field Left Blank

**Date:** 05.02.2025  
**Tester:** Goran  
**Priority:** Medium  

## Environment  
- **Application:** MarketMate  
- **Feature:** Age Verification for Restricted Products  
- **Browser:** Chrome  
- **Operating System:** Windows  

## Test Steps  

| Step# | Action                                                     | Expected Outcome                                            | Actual Outcome                                             | OK/NOK | URL | Notes |  
|-------|------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------|--------|-----|-------|  
| 1 | Go to the homepage of MarketMate                            | Homepage appears                                            | Homepage appears                                             | ✅ | [Homepage](https://grocerymate.masterschool.com/store) | |  
| 2 | Search for a restricted product (e.g., alcoholic beverage) | A prompt asking for date of birth appears                   | Prompt asking for date of birth appears                      | ✅ | [Search Page](https://grocerymate.masterschool.com/search) | |  
| 3 | Leave the Date of Birth field blank and attempt to proceed | Error message: "You need to be +18 to see some products. Please enter your birth date." is displayed | Error message: "You need to be +18 to see some products. Please enter your birth date." is displayed | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb479a1) | |

## Expected Result  
If the **Date of Birth** field is left blank during the **age verification process**, the system should display the error message:  
"You need to be +18 to see some products. Please enter your birth date."

## Actual Result  
The system correctly displays the error message:  
"You need to be +18 to see some products. Please enter your birth date." when the **Date of Birth** field is left blank.

## Screenshots  
![Image](https://github.com/user-attachments/assets/f6facc2a-f675-46e7-8e24-4acf12fb579d)  
![Image](https://github.com/user-attachments/assets/bbc837dd-783b-4afb-8ad0-ef7ca51fa757)  
![Image](https://github.com/user-attachments/assets/95def9aa-e1fd-4c88-90cb-3c764a12b163)



# Test Scenario: Maximum Review Character Limit Validation

**Date:** 05.02.2025  
**Tester:** Goran  
**Priority:** Medium  

## Environment  
- **Application:** MarketMate  
- **Feature:** Product Review Character Limit  
- **Browser:** Chrome  
- **Operating System:** Windows  

## Test Steps  

| Step# | Action | Expected Outcome | Actual Outcome | OK/NOK | URL | Notes |  
|-------|--------|-----------------|---------------|--------|-----|-------|  
| 1 | Go to the product description input field | The input field is displayed and allows text entry | The input field is displayed and allows text entry | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a8e) | |  
| 2 | Enter characters up to the maximum allowed limit | The system accepts input up to the limit | The system accepts input up to the limit | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a8e) | |  
| 3 | Try entering additional characters beyond the limit | The system prevents further input and displays the notification: "You cannot tell us more about this product." | The system prevents further input and displays the notification: "You cannot tell us more about this product." | ✅ | [Product Page](https://grocerymate.masterschool.com/product/66b3a57b3fd5048eacb47a8e) | |

## Expected Result  
When the user enters more characters than the allowed maximum in the **product description input field**, the system should display a notification:  
"You cannot tell us more about this product."

## Actual Result  
The system prevents additional input and displays the correct notification:  
"You cannot tell us more about this product" when the character limit is exceeded.

## Screenshots  
![Image](https://github.com/user-attachments/assets/f76e1bfb-c19b-441a-bd25-46352ef4f8ae)  
![Image](https://github.com/user-attachments/assets/432df989-6622-47aa-9afa-d08a5b935e67)
