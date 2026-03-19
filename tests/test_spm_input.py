import pytest
import allure
from playwright.sync_api import expect

@allure.epic('Сайт с тестовым функционалом')
@allure.feature('simple input')
@pytest.mark.ui
@pytest.mark.inputs
class TestSimpleInput:

    @allure.story('Обязательность поля')
    @allure.title('Проверка, что поле ввода является обязательным')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_input_required(self, smp_input_page):
        smp_input_page.open()
        assert smp_input_page.is_required()

    @pytest.mark.parametrize("text, is_valid", [
        pytest.param("abc", True, id="letters"),
        pytest.param("abc123", True, id="letters+numbers"),
        pytest.param("test_name", True, id="underscore"),
        pytest.param("test-name", True, id="hyphen"),
        pytest.param("abc def", False, id="space"),
        pytest.param("%$#@", False, id="special_chars"),
        pytest.param("тест", False, id="cyrillic"),
    ])
    @allure.story('Валидация символов')
    @allure.title('Проверка корректности символов в поле ввода')
    @allure.severity(allure.severity_level.NORMAL)
    def test_input_validation(self, smp_input_page, text, is_valid):
        smp_input_page.open()
        smp_input_page.fill_input(text)
        smp_input_page.press_enter()

        error = smp_input_page.get_error()

        if is_valid:
            expect(error).not_to_be_visible()
        else:
            expect(error).to_be_visible()

    @pytest.mark.parametrize("text, is_valid", [
        pytest.param("a", False, id="len_1"),
        pytest.param("ab", True, id="len_2"),
        pytest.param("abc", True, id="len_3"),
        pytest.param("a"*24, True, id="len_24"),
        pytest.param("a"*25, True, id="len_25"),
        pytest.param("a"*26, False, id="len_26"),
    ])
    @allure.story('Валидация длины')
    @allure.title('Проверка допустимой длины текста в поле ввода')
    @allure.severity(allure.severity_level.NORMAL)
    def test_input_length(self, smp_input_page, text, is_valid):
        smp_input_page.open()
        smp_input_page.fill_input(text)
        smp_input_page.press_enter()

        error = smp_input_page.get_error()
        if is_valid:
            expect(error).not_to_be_visible()
        else:
            expect(error).to_be_visible()

    @allure.story('Отправка формы')
    @allure.title('Проверка отображения текста после отправки формы')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_submit_and_check_result(self, smp_input_page):
        smp_input_page.open()
        text = "valid_name"

        smp_input_page.fill_input(text)
        smp_input_page.press_enter()

        expect(smp_input_page.get_error()).not_to_be_visible()
        expect(smp_input_page.page.locator(smp_input_page.locators.RESULT)).to_have_text(text)