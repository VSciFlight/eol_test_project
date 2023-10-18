import utility
from utility import DriverSetup

from src.pages.eol_article import Articles
from src.locators.eol_article_locators import Article_Locators

class TestArticles(DriverSetup):
    """
    Collection of tests on the article page
    """

    def test_content_integration(self, driver):
        """
        TC11
        Article - Integration - Article that contains an external video or image will be shown properly
        :param driver:
        :return:
        """
        self.article.go_to_article(driver)
        article_title = utility.get_element(driver, Article_Locators.locators['title'])

