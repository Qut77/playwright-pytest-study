import pytest

@pytest.mark.simple
@pytest.mark.ui
def test_simple_exists(simple_page):
    simple_page.open()
    simple_page.chech_button_exists()

@pytest.mark.simple
@pytest.mark.ui
def test_simple_click(simple_page):
    simple_page.open()
    simple_page.click_button()
    simple_page.check_result_click('Submitted')