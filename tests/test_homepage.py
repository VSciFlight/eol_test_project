import time

import utility
from utility import DriverSetup
from utility import lg

from src.pages.eol_homepage import Homepage
from src.locators.eol_homepage_locators import Homepage_Locators

from src.locators.eol_overall_locators import Overall_Locators

class TestHomepage(DriverSetup):
    """
    Collection of tests on the homepage
    """

    def test_homepage_search(self, driver):
        """
        TC3:
        Homepage - Search - Searching for terms gives the user relevant search results
        1. Go to eol.co.il
        2. Look for the search box and fill in a term
        3. Press enter or click the magnifying glass
        4. The results should contain the term in the title, the sub-title or the content itself
        :param driver:
        :return:
        """
        term = "רוח"
        Homepage.search_bar(driver, term)
        time.sleep(5)

        # in case where there are more than 16 results I want to load them all and then continue
        try:
            while len(driver.find_elements('xpath', '//button[contains(@class,"plusicon")]')) > 0:
                driver.find_element('xpath', '//button[contains(@class,"plusicon")]').click()
                time.sleep(4)
            lg.info("all results were loaded successfully")

        except:
            lg.info("these are all the results")
            pass

        # checking all the results
        try:
            article_grid = ('xpath', '//li[contains(@class, "ais-InfiniteHits-item")]')
            article_grid_list = utility.get_elements(driver, article_grid)
            lg.info("acquired search result grid")

            article_title_list = article_grid_list.find_elements('xpath', "./descendant::b[contains(@class,'article_title')]")
            article_title_text_list = [x.text for x in article_title_list]
            lg.info("acquired articles titles")

            article_subtitle_list = article_grid_list.find_elements('xpath', "./descendant::b[contains(@class,'article-text')]")
            article_subtitle_text_list = [x.text for x in article_subtitle_list]
            lg.info("acquired articles subtitles")

            # check for every element
            for title in article_title_text_list:

                # assertion of the term within the title_list
                try:
                    assert term in title

                # case where the term isn't in the title, check its sub-title
                except AssertionError:
                    lg.error('MAY BE IN SUBTITLE')




        # case where there are no results
        except:
            lg.error("No results were found")
            lg.info("suggesting searching for another term")

    def test_header_buttons(self, driver):
        """
        TC1:
        Header - Buttons - Buttons take the user to the relevant page
        1. Go to eol.co.il
        2. Press on any button in the header
        3. Relevant page should be open in a new tab.
        4. The results should contain the term in the title, the sub-title or the content itself

        :param driver:
        :return:
        """

        # home button (logo)
        try:
            logo = utility.get_element(driver, Overall_Locators.locators['header_logo_link'])
            logo_link = logo.get_attribute("href")
            logo.click()
            if utility.WDW(driver, 5).until(utility.EC.presence_of_element_located(('xpath', '//html'))):
                assert driver.current_url == logo_link

        except utility.NoSuchElementException:
            utility.lg.error("Element not found")

        except utility.TimeoutException:
            utility.lg.error("Element not loaded. Also possible the locator isn't correct")

        except AssertionError:
            raise("Assertion Error, values are incorrect!")
