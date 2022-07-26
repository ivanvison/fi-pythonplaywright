from playwright.sync_api import expect
from pom.clients_page_elements import ClientsPage
import pytest
import re

@pytest.mark.regression
def test_landing_on_clients_page(clients_page_context):
    # Assess
    page = clients_page_context

    # Act
    clients_page = ClientsPage(page)

    # Assert
    expect(page).to_have_url(re.compile(".*clients"))
    expect(clients_page.clients_title).to_be_visible()