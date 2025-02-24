## XPath for Login Page Elements

### Email Input Field
```xpath
//input[@type='email' and @placeholder='Email address']
```

### Password Input Field
```xpath
//input[@type='password' and @placeholder='Password']
```

### Sign In Button
```xpath
//button[@type='submit' and contains(@class, 'submit-btn')]
```

### Create a New Account Link
```xpath
//a[contains(@class, 'switch-link') and text()='Create a new account']
```

### Go to Home Link
```xpath
//a[contains(@class, 'home-link') and text()='Go to Home']
```

