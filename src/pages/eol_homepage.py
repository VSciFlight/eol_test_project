import utility
import time
from src.locators.eol_homepage_locators import Homepage_Locators
from selenium.webdriver.common.keys import Keys
class Homepage:

    def search_bar(driver, term, timeout=10):
        locator = Homepage_Locators.locators['search_box']
        search_box = utility.get_element(driver, locator)
        search_box.send_keys(term)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)
