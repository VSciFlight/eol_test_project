from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from src.pages.eol_article import Articles
from src.pages.eol_homepage import Homepage

import pytest
from loguru import logger as lg

class DriverSetup:

    @pytest.fixture()
    def driver(self):
        url = 'https://www.eol.co.il/'
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        self.article = Articles()
        self.homepage = Homepage()

        driver.maximize_window()
        driver.get('https://www.eol.co.il/')

        yield driver
        driver.quit()



def click_that(driver, locator, timeout=10):
    WDW(driver, timeout).until(EC.visibility_of_element_located(locator)).click()
    return


def get_element(driver, locator, timeout=10):
    return WDW(driver, timeout).until(EC.visibility_of_element_located(locator))

def get_elements(driver, locator, timeout=10):
    return WDW(driver, timeout).until(EC.visibility_of_all_elements_located(locator))