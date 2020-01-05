from .base_page import BasePage


class MainPage(BasePage):

    url = "https://www.lotteryheroes.com"

    def main_pages_title(self):
        return self.browser.title