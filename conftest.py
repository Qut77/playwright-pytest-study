import pytest
import allure
from playwright.sync_api import Page
from pages.button_page import ButtonPage
from pages.locators import *
from dotenv import load_dotenv
import os
load_dotenv()

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height':1080, 'width':1920})
    yield page

@pytest.fixture()
def like_button_page(page: Page) -> ButtonPage:
    return ButtonPage(
        page=page,
        url=os.getenv('LIKE_BUTTON_URL'),
        locators=LikeButtonLocators,
        )

@pytest.fixture()
def simple_page(page: Page) -> ButtonPage:
    return ButtonPage(
        page=page,
        url=os.getenv('SIMPLE_URL'),
        locators=SimplePageLocators,
        )

@pytest.fixture()
def disabled_page(page: Page) -> ButtonPage:
    return ButtonPage(
        page=page,
        url=os.getenv('DISABLED_URL'),
        locators=DisabledPageLocators
    )

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