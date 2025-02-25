# System Requirements

## 1. Product Rating System

### Overview
This feature enables users to rate products using a 5-star system and leave written reviews. Only registered users can submit ratings, but all visitors can view them. Users can edit or delete their reviews if needed. Reviews will be displayed on the product page, sorted by date or helpfulness. A moderation system will ensure inappropriate content is filtered out.

### Requirements
- Users can rate products using a 5-star system.
- Optional written reviews can be added.
- Users can edit or delete their reviews.
- Only registered users can submit ratings and reviews.
- Ratings and reviews are displayed on the product page, sorted by date or helpfulness.
- A moderation system will filter out offensive or spam content.

### Open Questions
- Should ratings be visible to all users or just registered ones?
- Can users edit or delete reviews after submission?
- Should written reviews have a character limit?
- Will users be able to report inappropriate reviews?
- How should the overall product rating be calculated (e.g., average, weighted by recency)?
- Should reviews be reviewed before publication?

---

## 2. Age Verification for Alcoholic Products

### Overview
To comply with legal regulations, users must verify their age before accessing alcoholic products. A pop-up will prompt users to enter their date of birth. If under 18, they will be redirected. If 18 or older, they can proceed. The system will remember verified users for the session but require re-verification in a new session.

### Requirements
- A pop-up appears when users access alcoholic products.
- Users must enter their date of birth.
- Users under 18 are redirected away from alcoholic products.
- Users 18+ can continue.
- Verification is remembered for the session but resets upon a new session.

### Open Questions
- Should verification apply to both guests and logged-in users?
- Can users bypass verification by refreshing or using incognito mode?
- Are there legal requirements for storing age verification logs?
- Should verification be required every visit or remembered for a session?
- How should incorrect entries (e.g., mistyped birthdates) be handled?
- Should users under 18 be restricted from the entire store or just alcoholic products?

---

## 3. Shipping Cost Changes

### Overview
To enhance transparency, a free shipping threshold will be introduced. Orders exceeding a configurable amount (e.g., $20) will qualify for free shipping, while others will incur a fee based on weight and destination. The shipping fee will be displayed at checkout before payment. Discounts applied post-cart addition will not affect free shipping eligibility. The system will also calculate varied shipping costs based on location.

### Requirements
- Orders over $20 (configurable by admin) qualify for free shipping.
- Orders below the threshold incur a shipping fee based on weight and destination.
- The shipping fee is displayed at checkout before payment.
- Discounts do not impact free shipping eligibility after items are in the cart.
- Different regions have different shipping costs.

### Open Questions
- What is the exact free shipping threshold, and can admins adjust it?
- Should taxes be included in the free shipping calculation?
- How should multiple shipping addresses in one order be handled?
- If an item is removed and the total drops below the threshold, should shipping be automatically applied?
- Should shipping costs update dynamically in the cart or only at checkout?
- Should users be notified when they are close to qualifying for free shipping?

