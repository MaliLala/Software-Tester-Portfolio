### XPath Task 1

#### 1. Locate the main **h1** element:
```xpath
//h1[@id='mainTitle']
```

#### 2. Select the **About Us** navigational link:
```xpath
//a[@href='#about' and contains(@class, 'nav-link')]
```

#### 3. Select the **Graphic Design** dropdown link:
```xpath
//ul[@class='dropdown']/li/a[@href='#graphicdesign']
```

#### 4. Select the team member’s name **Jane Smith**:
```xpath
//div[@class='team']//h4[text()='Jane Smith']
```

#### 5. Select the description (inside the paragraph) of **SEO Services**:
```xpath
//div[@class='service-item'][h3[text()='SEO Services']]/p
```

#### 6. Select all service items in the "**Our Services**" section:
```xpath
//section[@id='services']//div[@class='service-item']
```

#### 7. Select the **email input field** in the contact form:
```xpath
//form[@id='contactForm']//input[@type='email']
```

#### 8. Select the **entire contact form**:
```xpath
//form[@id='contactForm']
```

#### 9. Select the **footer paragraph element**:
```xpath
//footer//p
```

#### 10. Select the **first team member**'s (`<h4>`) name:
```xpath
//div[@class='team']//ul/li[1]/h4
```

#### 11. Select the description of the **second service** item:
```xpath
//div[@class='service-item'][2]/p
```

#### 12. Select the "Contact Us" section header (`<h2>` element):
```xpath
//section[@id='contact']//h2
```

#### 13. Select all links within the dropdown under the "Services" navigation item:
```xpath
//ul[@class='dropdown']//a
```

#### 14. Select the first `<li>` under the "Our Team" section:
```xpath
//div[@class='team']//ul/li[1]
```

#### 15. Locate the "Send Message" button in the contact form:
```xpath
//form[@id='contactForm']//input[@type='submit']
```
