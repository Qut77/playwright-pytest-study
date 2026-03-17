import pytest
from playwright.sync_api import Page
from pages.like_button_page import LikeButtonPage
from pages.simple_page import SimplePage

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height':1080, 'width':1920})
    yield page

@pytest.fixture()
def like_button_page(page: Page) -> LikeButtonPage:
    return LikeButtonPage(page)

@pytest.fixture()
def simple_page(page: Page)-> SimplePage:
    return SimplePage(page)