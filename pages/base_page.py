from playwright.sync_api import Page

class BasePage:

    url: str | None = None

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        if self.url:
            self.page.goto(self.url)