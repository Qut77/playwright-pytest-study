from playwright.sync_api import expect
from pages.base_page import BasePage
import allure

class ButtonPage(BasePage):

    @allure.step("Проверить видно ли кнопку")
    def check_button_exists(self) -> None:
        expect(self.page.locator(self.locators.BUTTON)).to_be_visible()

    @allure.step("Нажать на кнопку")
    def click_button(self) -> None:
        self.page.locator(self.locators.BUTTON).click()
    
    @allure.step("Проверить есть ли текст")
    def check_result_click(self, text: str) -> None:
        expect(self.page.locator(self.locators.RESULT)).to_have_text(text)
    
    @allure.step("Проверить видно ли селект")
    def check_select_exists(self) -> None:
        expect(self.page.locator(self.locators.SELECT)).to_be_visible()

    @allure.step("Выбрать в select значение {state}")
    def set_select_state(self, state:str) -> None:
        self.page.locator(self.locators.SELECT).select_option(state)

    @allure.step("Проверить не активность кнопки")
    def check_button_is_disabled(self) -> None:
        expect(self.page.locator(self.locators.BUTTON)).to_be_disabled()

    @allure.step("Проверить активность кнопки")
    def check_button_is_enabled(self) -> None:
        expect(self.page.locator(self.locators.BUTTON)).to_be_enabled()