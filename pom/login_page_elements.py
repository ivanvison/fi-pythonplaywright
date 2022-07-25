from unicodedata import name


class LoginPage:

    def __init__(self, page):
        self.login_sign_in_button = page.locator("button", has_text="Sign In")
        self.login_email_input = page.locator("#email")
        self.login_password_input = page.locator("[type='password']")

    
    def login_submit_form(self, email, password):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_sign_in_button.click()


