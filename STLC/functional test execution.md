
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
