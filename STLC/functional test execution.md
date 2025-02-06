
# MarketMate - Age Verification Test Case  

## Scenario: Age Verification for Alcoholic Products  

### Steps  

| Step# | Action | Expected Outcome | OK/NOK | URL | Link to Issue |  
|-------|--------|-----------------|--------|-----|--------------|  
| 1 | Go to MarketMate homepage | Homepage appears | OK | [[MarketMate URL](https://grocerymate.masterschool.com/store)] | |  
| 2 | Search for an alcoholic product | A prompt appears asking for Date of Birth input | OK | /search | |  
| 3a | Enter a valid Date of Birth (e.g., 18-08-2000, 18+ years) | The alcoholic product is displayed | OK | /product/[ID] | |  
| 3b | Enter an invalid Date of Birth (e.g., 18-08-2006, exactly 17 years and 364 days old) | Access is denied with a message | OK | | |  
| 4 | Refresh or revisit the page | The system remembers the verified age (if applicable) | OK | | |  

**Result:** The system behaved as expected, correctly allowing or denying access based on the entered date of birth.
![DOB 17y 364d](https://github.com/user-attachments/assets/6e1e6267-e2b0-4985-b1bb-ed3980e1a895)
![Under 18 Notification](https://github.com/user-attachments/assets/833a93d3-1e75-4958-b89a-e954acd3f2c7)





# MarketMate - Shipping Cost Test Case  

## Scenario: Shipping Cost Calculation  

### Steps  

| Step# | Action | Expected Outcome | OK/NOK | URL | Link to Issue |  
|-------|--------|-----------------|--------|-----|--------------|  
| 1 | Go to MarketMate homepage | Homepage appears | OK | [MarketMate URL] | |  
| 2 | Add items to the basket totaling **less than 20 EUR** | Shipping cost is **5 EUR** | OK | /cart | |  
| 3 | Add more items to reach **20 EUR or more** | Shipping cost is **0 EUR (free shipping applied)** | OK | /cart | |  
| 4 | Remove items so that the total is **below 20 EUR again** | Shipping cost **does not update back to 5 EUR (Issue found)** | NOK | /cart | [Link to issue] |  

**Result:** The system **fails to reapply the 5 EUR shipping cost** when the basket value drops below 20 EUR. Issue needs investigation.
![Shipping cost under 20Eur](https://github.com/user-attachments/assets/2ffa8f32-3429-4457-a033-b9a42f40aa3f)
![Shipping cost over 20Eur](https://github.com/user-attachments/assets/8a8b23b1-fbfe-4942-b8a7-fc5838c99346)
![Shipping cost error when taking out items](https://github.com/user-attachments/assets/6bbba49f-060d-4551-bc96-a306b52c7851)




# Bug Report  
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
| 1 | Go to the Market Mate example Product page. | Product page appears | Product page appears | OK | [MarketMate URL] | |  
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


