import random


class Homepage_Locators():
    locators = dict()

    locators['article_list'] = ('xpath', '//a[contains(@href, "articles")]')
    locators['article'] = ('xpath', f'//a[contains(@href, "articles")][{random.randrange(1,12)}]')

    locators['search_box'] = ('xpath', '//input[@id="search-home"]')
    locators['plusicon'] = ('xpath', '//a[contains(@class, "plusicon")]') #load more articles



    