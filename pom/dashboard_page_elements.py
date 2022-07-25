from unicodedata import name


class DashboardPage:

    def __init__(self, page):
        self.dashboard_title = page.locator('h1:has-text("Dashboard")')


