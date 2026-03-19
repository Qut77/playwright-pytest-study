import allure
from pages.base_page import BasePage
from playwright.async_api import expect

class InputPage(BasePage):

    @allure.step('Ввод текста в поле')
    def fill_input(self, text: str) -> None:
        self.page.locator(self.locators.INPUT).fill(text)

    @allure.step('Нажатие enter')
    def press_enter(self) -> None:
        self.page.locator(self.locators.INPUT).press('Enter')

    @allure.step('Получение результата')
    def get_result_text(self) -> str:
        return self.page.locator(self.locators.RESULT).text_content()

    @allure.step('Получить текущее значение в поле ввода')
    def get_input_value(self) -> str:
        return self.page.locator(self.locators.INPUT).input_value()

    @allure.step('Проверить, что поле обязательно для заполнения')
    def is_required(self) -> bool:
        return self.page.locator(self.locators.INPUT).get_attribute("required") is not None

    @allure.step('Получить элемент ошибки валидации под полем')
    def get_error(self):
        return self.page.locator(self.locators.ERROR)