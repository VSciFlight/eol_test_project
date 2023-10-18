import utility
from src.locators.eol_homepage_locators import Homepage_Locators

class Articles:
    def go_to_article(self, driver):
        try:
            article_locator = Homepage_Locators.locators['article']
            utility.click_that(driver, article_locator)

        except:
            pass