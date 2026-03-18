from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import SimplePageLocators
from dotenv import load_dotenv
import os
import allure
load_dotenv()

class SimplePage(BasePage):

    url: str | None = os.getenv('SIMPLE_URL')

    @allure.step("Проверить видно ли кнопку")
    def check_button_exists(self) -> None:
        expect(self.page.locator(SimplePageLocators.BUTTON)).to_be_visible()

    @allure.step("Нажать на кнопку")
    def click_button(self) -> None:
        self.page.locator(SimplePageLocators.BUTTON).click()
    
    @allure.step("Проверить есть ли текст")
    def check_result_click(self, text: str) -> None:
        expect(self.page.locator(SimplePageLocators.RESULT)).to_have_text(text)