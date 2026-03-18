import pytest
import allure

@allure.epic('Сайт с тестовым функционалом')
@allure.feature('Кнопка like button')
@pytest.mark.simple
@pytest.mark.ui
class TestLikeButton:
    @allure.story('Проверка наличия кнопки')
    @allure.title('Проверка наличия кнопки')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_like_button_exists(self, like_button_page):
        like_button_page.open()
        like_button_page.check_button_exists()

    @allure.story('Клик по кнопке и проверка подтверждения')
    @allure.title('Валидация текста')
    @allure.severity(allure.severity_level.NORMAL)
    def test_like_button_click(self, like_button_page):
        like_button_page.open()
        like_button_page.click_button()
        like_button_page.check_result_click('Submitted')