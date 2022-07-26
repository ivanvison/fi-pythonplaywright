from random import randint
from playwright.sync_api import expect
from pom.clients_page_elements import ClientCreationForm, ClientsPage
import pytest
import re

@pytest.mark.regression
def test_adding_new_client_form(clients_page_context):
    # Assess
    page = clients_page_context

    # Act
    clients_page = ClientsPage(page)
    
    clients_page.new_client_button.click()
    
    new_client_form = ClientCreationForm(page)

    expect(page).to_have_url(re.compile(".*clients/create"))

    name = 'Johnny Rocks ' + str(randint(1548,78965))

    new_client_form.new_client_creation_form_fill(name, 'rocks@jr.com', 'Customer')
    
    page.wait_for_load_state('networkidle')
    expect(page.locator("#unique_name")).to_be_visible()
    page.locator("#unique_name").fill(name)
    new_client_form.save_new_client_button.click()

    page.wait_for_load_state('networkidle')
    expect(page.locator('.label-success:has-text("Rocks")')).to_be_visible()


@pytest.mark.regression
def test_check_client_created(clients_page_context):
    # Assess
    page = clients_page_context
    page.locator("text=MInistry of Silly Walks").click()

    page.wait_for_load_state('networkidle')
    expect(page.locator('.label-success:has-text("Silly")')).to_be_visible()