from .pages.main_page import MainPage


def test_open_main_page(browser):
    link = "https://www.lotteryheroes.com/"
    page = MainPage(browser, link)
    page.open()
    assert page.main_pages_title(), "Play Online Lottery | Bet on global lotteries jackpots | LotteryHeroes"
