from playwright.sync_api import Page
import allure

class BasePage:

    url: str | None = None

    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step("Открыть страницу")
    def open(self) -> None:
        if self.url:
            self.page.goto(self.url)