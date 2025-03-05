
# Test Plan for GroceryMate & Market Mate

## Objective

The purpose of this test plan is to ensure that key features of the GroceryMate and Market Mate platforms, including the Product Rating System, Age Verification for Alcoholic Products, and Shipping Cost Calculation, function correctly. Additionally, we will test how the system handles errors to ensure a smooth user experience.

## Scope

### Features to be Tested

- **Product Rating System**: Ensure ratings can be submitted, displayed, and calculated correctly.
- **Age Verification for Alcoholic Products**: Verify that age-related restrictions are enforced properly.
- **Shipping Cost Calculation**: Ensure that the correct shipping fee is applied based on the value of items in the cart.
- **Error Handling**: Validate how the system responds to incorrect or unexpected user inputs.

### Excluded from Testing

- **Cross-Browser Compatibility Testing**: Testing will only be conducted on Google Chrome, excluding other browsers like Firefox, Edge, and Safari.
- **Localization & Language Testing**: The platform’s multilingual support will not be tested in this phase.

## Test Environment

- **Browser**: Google Chrome
- **Operating System**: Windows

## Testing Approach

Testing will be manual, focusing on functional tests to ensure that the core features work as expected, as well as error handling tests to verify that incorrect inputs do not cause system failures.

## Test Cases

### 1. Product Rating System

The product rating system allows users to submit and view reviews for products. The following test cases will be covered:

- **Valid Rating Submissions**: Ensure users can submit valid ratings (e.g., a 4-star rating).
- **Lowest Valid Ratings**: Ensure users can submit a 1-star rating.
- **Handling of Cases Where No Rating Is Selected**: Ensure the system properly handles cases where a user tries to submit a review without selecting a rating.
- **Average Rating Calculation**: Verify that the system correctly calculates and displays average ratings based on user reviews.

### 2. Age Verification for Alcoholic Products

Age verification ensures that only users who are 18 years old or older can access and purchase alcoholic products. The test cases include:

- **Granting Access for Users Exactly 18 Years Old**: Ensure that users who enter an age of exactly 18 are granted access.
- **Denying Access to Users Under 18**: Ensure that users who enter an age under 18 are denied access.
- **Properly Handling Empty Fields During Age Verification**: Ensure that the system prevents users from proceeding if they leave the age verification field blank.

### 3. Shipping Cost Calculation

Shipping costs should be applied correctly based on the cart total. The test cases include:

- **Shipping Fee Application for Orders Below $20**: Ensure that a shipping fee is correctly applied to orders totaling less than $20.
- **Free Shipping Eligibility for Orders Above $20**: Ensure that free shipping is correctly applied when the cart total exceeds $20.
- **Proper Adjustment of Shipping Costs When Items Are Added or Removed**: Verify that the shipping fee updates dynamically when items are added or removed from the cart.

### 4. Error Handling

Error handling ensures that users receive clear messages and that incorrect inputs do not cause system failures. The test cases include:

- **Invalid Input for Age Verification**: Ensure that entering a negative number, non-numeric characters, or an unrealistic age (e.g., 200 years old) is properly handled with an error message.
- **Invalid Rating Submission**: Verify that submitting an empty rating or an out-of-range rating (e.g., 6 stars) does not break the system and returns an appropriate error message.
- **Incorrect Shipping Cost Calculation**: Ensure that removing items from the cart updates the shipping cost correctly without displaying incorrect fees.
- **Form Validation Errors**: Ensure that all required fields in checkout, registration, and payment forms show appropriate error messages when left empty or incorrectly filled.

## Test Strategy

### Scope of Testing

- **In Scope**:
  - Functional Testing of core features
  - UI/UX Testing to ensure usability
  - Error Handling Testing to verify system stability

- **Out of Scope**:
  - Cross-Browser Compatibility Testing
  - Localization & Language Testing

### Risks and Issues

- **Delays in Development** → Plan buffer time.
- **Test Data Availability** → Ensure mock data sets are available for testing.
- **Resource Availability** → Identify backup resources in case of unavailability.
- **Edge Case Handling** → Ensure adaptability to unforeseen edge cases.

### Test Criteria

#### Suspension Criteria

- Testing will be suspended if critical defects block further testing.
- Unavailability of test environment or resources.

#### Exit Criteria

- All planned test cases have been executed.
- At least 90% of executed test cases have passed.
- No blocking or high-priority defects remain.

## Schedule (Estimated)

| Activity                        | Start   | End     | Responsible  |
|----------------------------------|---------|---------|--------------|
| Test Design                      | 06/08   | 15/08   | QA Team      |
| Functional Testing               | 16/08   | 25/08   | QA Team      |
| Error Handling Testing           | 26/08   | 30/08   | QA Team      |
| Usability Testing                | 26/09   | 30/09   | End Users    |
| Production Release               | 01/10   | 01/10   | DevOps       |

## Test Deliverables

- Test Plan Document
- Test Cases & Test Reports
- Defect Reports
- UAT Sign-off Document
