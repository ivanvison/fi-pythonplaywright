from playwright.sync_api import expect
from pom.dashboard_page_elements import DashboardPage
import pytest
import re

@pytest.mark.regression
def test_landing_on_dashboard_page(dashboard_page_context):
    # Assess
    page = dashboard_page_context

    # Act
    dashboard_page = DashboardPage(page)

    # Assert
    expect(page).to_have_url(re.compile(".*dashboard"))
    expect(dashboard_page.dashboard_title).to_be_visible()