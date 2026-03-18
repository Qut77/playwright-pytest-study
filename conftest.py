import pytest
import allure
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == 'call' and rep.failed:
        page = item.funcargs.get('page')
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="Финишный скриншот",
                attachment_type=allure.attachment_type.PNG
            )