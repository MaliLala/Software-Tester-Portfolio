# XPath Selectors for Oranges

## 1️⃣ Quantity Input for Oranges
```xpath
//div[contains(@class, 'product-card') and .//p[contains(text(), 'Oranges')]]//input[@type='number']
```

## 2️⃣ "Add to Cart" Button for Oranges
```xpath
//div[contains(@class, 'product-card') and .//p[contains(text(), 'Oranges')]]//button[contains(@class, 'btn-cart')]
```

## 3️⃣ "Add to Wishlist" Button for Oranges
```xpath
//div[contains(@class, 'product-card') and .//p[contains(text(), 'Oranges')]]//button[contains(@class, 'btn-outline-dark')]
```

