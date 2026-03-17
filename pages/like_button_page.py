from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators import LikeButtonLocators
from dotenv import load_dotenv
import os
load_dotenv()

class LikeButtonPage(BasePage):
    url: str | None = os.getenv('LIKE_BUTTON_URL')

    def chech_button_exists(self) -> None:
        expect(self.page.locator(LikeButtonLocators.BUTTON)).to_be_visible()

    def click_button(self) -> None:
        self.page.locator(LikeButtonLocators.BUTTON).click()
    
    def check_result_click(self, text: str) -> None:
        expect(self.page.locator(LikeButtonLocators.RESULT)).to_have_text(text)