from playwright.sync_api import Playwright
from pom.login_page_elements import LoginPage
import pytest
import os

@pytest.fixture(scope='session')
def context_creation(playwright):
    # Assess
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://demo.fusioninvoice.com/login")

    login_page = LoginPage(page)
    email = os.environ['EMAIL']
    password = os.environ['PASSWORD']
 
    # Act
    login_page.login_submit_form(email,password)

    page.wait_for_load_state('networkidle')
    context.storage_state(path='state.json')   

    yield context
    browser.close()


@pytest.fixture()
def login_set_up(context_creation,playwright):
    context = context_creation
    page = context.new_page()

    yield page


@pytest.fixture()
def dashboard_page_context(context_creation,playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()
    page.goto("https://demo.fusioninvoice.com/dashboard")

    yield page
    browser.close()


@pytest.fixture()
def clients_page_context(context_creation,playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()
    page.goto("https://demo.fusioninvoice.com/clients")

    yield page
    browser.close()