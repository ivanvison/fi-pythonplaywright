from unicodedata import name


class ClientsPage:

    def __init__(self, page):
        self.clients_title = page.locator('h1:has-text("Clients")')
        self.new_client_button = page.locator(".btn:has-text('New')")


class ClientCreationForm:

    def __init__(self, page):
        self.new_client_form_title = page.locator('h1:has-text("Client Form")')
        self.save_new_client_button = page.locator('.content-header .btn:has-text("Save")')
        self.client_name_input = page.locator("#name")
        self.client_email_input = page.locator("#client_email")
        self.client_type_select = page.locator("#type")

    def new_client_creation_form_fill(self,name,email,type):
        self.client_name_input.fill(name)
        self.client_email_input.fill(email)
        self.client_type_select.select_option(label=type)
        self.save_new_client_button.click()
