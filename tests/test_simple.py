import pytest
import allure

@allure.epic('Сайт с тестовым функционалом')
@allure.feature('Кнопка simple')
@pytest.mark.buttons
@pytest.mark.ui
class TestSimple:
    @allure.story('Проверка наличия кнопки')
    @allure.title('Проверка наличия кнопки')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_simple_exists(self, simple_page):
        simple_page.open()
        simple_page.check_button_exists()

    @allure.story('Клик по кнопке и проверка подтверждения')
    @allure.title('Валидация текста')
    @allure.severity(allure.severity_level.NORMAL)
    def test_simple_click(self, simple_page):
        simple_page.open()
        simple_page.click_button()
        simple_page.check_result_click('Submitted')