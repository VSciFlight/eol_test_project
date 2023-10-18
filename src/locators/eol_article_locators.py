import random


class Article_Locators():
    locators = dict()

    locators['recommended_sidebar'] = ('xpath', '//div[contains(@class,"recommended-sidebar")]/descendant::a')
    locators['recommended_end'] = ('xpath', '//p[@class="more_recommended_articles"]')
    locators['title'] = ('xpath', '//div[@class="title"]/div/h1')

    # TED (Embedded)
    locators['ted_play_video'] = ('xpath', '//div[contains(@class,"Embeddable__landing__play")]')
    locators['ted_play_inside'] = ('xpath', '//a[contains(@class,"Embeddable__controls__play")][1]')
    locators['ted_sound_btn'] = ('xpath', '//a[contains(@class,"Embeddable__controls__volume")]')
    locators['ted_subtitles_btn'] = ('xpath', '//a[contains(@class,"Embeddable__controls__subtitles")]')
    locators['ted_subtitles_list'] = ('xpath', '//li[contains(@class,"Embeddable__subtitles__language")]')  # selects list of available subs
    locators['ted_fullscreen_enlarge_btn'] = ('xpath', '//a[contains(@class,"Embeddable__controls__fullscreen")]')
    locators['ted_fullscreen_reduce_btn'] = ('xpath', '//a[contains(@class,"Embeddable__controls__smallscreen")]')

    # sharing
    locators['share_mail'] = ('xpath', '//a[@class="mailto"]')
    locators['share_fb'] = ('xpath', '//a[@class="facebook"]')
    locators['share_wa'] = ('xpath', '//a[@class="wapp"]')



