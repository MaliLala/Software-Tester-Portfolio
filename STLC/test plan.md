Test Plan for GroceryMate Webshop


1. Analyze the Product

ObjectiveThe objective of this test plan is to make sure the new features of the GroceryMate webshop work as expected and that users don’t run into any weird issues. We want to make sure everything is smooth and makes sense for the customers.
User Base
Everyday people looking to buy groceries online.
Users of different ages, especially those buying alcoholic products.
People with accounts who leave reviews and ratings.
Visitors who just want to browse around.

Hardware and Software Specifications

Hardware Requirements
Devices: Computers, laptops, smartphones, tablets.
Specs: Standard configurations for Android and iOS devices, desktops with minimum 4GB RAM, 2GHz processor.

Software Requirements

OS: Windows, macOS, Android, iOS.
Browsers: Chrome, Firefox, Safari, Edge.
Dependencies: Backend services, third-party payment processing, authentication, etc.


Product Functionality

Existing Features:Register/login functionality.
Searching, sorting, filtering products.
Favoriting products.
Adding products to the basket.
Checking out, filling billing info, selecting payment methods.


New Features to be Tested:

Product Rating System - Users can rate products (1-5 stars) and leave written feedback.
Age Verification for Alcoholic Products - Users need to confirm they’re 18+ before seeing alcohol.
Shipping Cost Changes - Free shipping if a user spends enough; otherwise, a shipping fee applies.


2. Test Strategy

Scope of Testing

In Scope:Functional testing for the new features.
UI/UX testing to ensure good usability.
Security testing for age verification.
Performance testing.
Usability testing.

Out of Scope:

Deep backend security testing.
Extremely rare edge cases.

Type of Testing

Functional Testing
UI Testing
Security Testing
Regression Testing
Usability Testing
Performance Testing


Risks and Issues

Delays in development → Plan buffer time.
Lack of test data → Create mock data sets.
Resource unavailability → Identify backup resources.


3. Test Objectives
  
GoalsFunctionality: 

Ensure new features work correctly.
GUI: Ensure UI is intuitive and responsive.
Performance: Verify the site runs smoothly under expected loads.
Security: Ensure no loopholes in age verification.
Usability: Ensure ease of use for all users.


Expected ResultsFunctionality:

No unexpected errors.
GUI: Responsive and free of major UI defects.
Performance: Handles expected traffic without major slowdowns.
Security: No easy workarounds for age verification.
Usability: Users can navigate and complete tasks easily.


4. Test Criteria

Suspension Criteria

Testing will be suspended if critical defects block further testing.
Unavailability of required resources or test environment failures.

Exit Criteria

All planned tests have been executed.
At least 90% of executed test cases have passed.
No critical or high-priority defects remain unresolved.
User acceptance testing is completed and approved.


5. Resources
  
Human Resources: QA testers, developers, end users for UAT.
Hardware: Computers, tablets, and smartphones.
Software: Browsers, OSs, testing tools.
Test Environment: DEV, TEST, ACC, PROD.


6. Test EnvironmentReal devices for realistic testing.
    
Environments: Dev (DEV), Test (TEST), Acceptance (ACC), Production (PROD).

7.[test_schedule.xlsx](https://github.com/user-attachments/files/18660395/test_schedule.xlsx)



Test Cases & Test Scripts
Test Data
Test Reports
Defect Reports
UAT Sign-off Document
