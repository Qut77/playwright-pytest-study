from playwright.sync_api import Page
import allure

class BasePage:

    def __init__(self, page: Page, url:str = None, locators=None) -> None:
        self.page = page
        self.url = url
        self.locators = locators

    @allure.step("Открыть страницу")
    def open(self) -> None:
        if self.url:
            self.page.goto(self.url)