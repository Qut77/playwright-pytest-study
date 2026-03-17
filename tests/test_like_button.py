import pytest

@pytest.mark.like_button
@pytest.mark.ui
def test_like_button_exists(like_button_page):
    like_button_page.open()
    like_button_page.chech_button_exists()

@pytest.mark.like_button
@pytest.mark.ui
def test_like_button_click(like_button_page):
    like_button_page.open()
    like_button_page.click_button()
    like_button_page.check_result_click('Submitted')