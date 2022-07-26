from playwright.sync_api import expect
from pom.login_page_elements import LoginPage
import pytest
import re

@pytest.mark.smoke
@pytest.mark.regression
def test_login_screen_and_login_form(login_set_up) -> None:
    page = login_set_up
    login_page = LoginPage(page)

    expect(page).to_have_url(re.compile(".*dashboard"))

