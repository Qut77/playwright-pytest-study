import pytest
import allure

@allure.epic('Сайт с тестовым функционалом')
@allure.feature('Кнопка disabled')
@pytest.mark.simple
@pytest.mark.ui
class TestDisabledButton:
    
    @allure.story('Проверка наличия кнопки')
    @allure.title('Проверка наличия кнопки')
    def test_disabled_button_exists(self, disabled_page):
        disabled_page.open()
        disabled_page.check_button_exists()

    @allure.story('Проверка наличия select')
    @allure.title('Проверка наличия select')
    def test_select_exists(self, disabled_page):
        disabled_page.open()
        disabled_page.check_select_exists()

    @allure.story('Проверка состояния disabled по умолчанию')
    @allure.title('Проверка состояния disabled по умолчанию')
    def test_submit_button_disabled_by_default(self, disabled_page):
        disabled_page.open()
        disabled_page.check_button_is_disabled()

    @allure.story('Взаимодействие с заблокированной кнопкой')
    @allure.title('Успешное переключение состояния кнопки через select')
    def test_submit_button_state_toggle(self, disabled_page):
        disabled_page.open()
        disabled_page.set_select_state(disabled_page.locators.ENABLED)
        disabled_page.check_button_is_enabled()
        disabled_page.click_button()
        disabled_page.check_result_click("Submitted")
        disabled_page.set_select_state(disabled_page.locators.DISABLED)
        disabled_page.check_button_is_disabled()