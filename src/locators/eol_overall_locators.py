import random


class Overall_Locators():
    locators = dict()

    # header
    locators['header_logo'] = ('xpath', '//img[@alt="מהות החיים"]')
    locators['header_logo_link'] = ('xpath', '//img[@alt="מהות החיים"]/parent::a')
    locators['header_homepage'] = ('xpath', '//ul[@id="mainnavbar"]/descendant::a[text()="בית"]')
    locators['header_about'] = ('xpath', '//ul[@id="mainnavbar"]/descendant::a[text()="מי אנחנו"]')
    locators['header_newsletter'] = ('xpath', '//ul[@id="mainnavbar"]/descendant::a[text()="הרשמה לניוזלטר"]')
    locators['header_contact'] = ('xpath', '//ul[@id="mainnavbar"]/descendant::a[text()="צרו קשר"]')

    locators['header_lang_he'] = ('xpath', '//a[@alt="he"]')
    locators['header_lang_en'] = ('xpath', '//a[@alt="en"]')

    locators['header_soundcloud'] = ('xpath', '//a[@class="soundcloud"]')
    locators['header_instagram'] = ('xpath', '//a[@class="instagram-icon"]')
    locators['header_facebook'] = ('xpath', '//a[@class="sprite fb"]')

    locators['header_play'] = ('xpath', '//a[@class="sprite liveradio"]')
    locators['header_radio'] = ('xpath', '//a[contains(@class, "sprite radiomaut")]')
    locators['header_mahuti'] = ('xpath', '//a[contains(@class, "sprite maut")]')

    # accessibility
    locators['ac_contrast_btn'] = ('xpath', '//button[contains(@class,"a11y-toggle-contrast"]')
    locators['ac_fontsize'] = ('xpath', '//button[contains(@class,"a11y-toggle-fontsize"]')

    # footer newsletter
    locators['footer_newsletter_email'] = ('xpath', '//input[@id="mce-EMAIL"]')
    locators['footer_newsletter_email'] = ('xpath', '//input[@id="mc-embedded-subscribe"]')

    # footer
    locators['footer_logo'] = ('xpath', '//img[@alt="לוגו מהות החיים"]')
    locators['footer_logotext'] = ('xpath', '//img[@alt="לוגו מהות החיים"]/parent::a/following-sibling::p/a')

    locators['footer_about'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[text()="אודות מהות החיים"]')
    locators['footer_values'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[text()="הערכים של מהות החיים"]')
    locators['footer_contact'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[text()="צרו קשר"]')
    locators['footer_terms'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[text()="תנאי שימוש"]')
    locators['footer_privacy'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[text()="מדיניות פרטיות"]')
    locators['footer_accessibility_statement'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[text()="הצהרת נגישות"]')
    locators['footer_mahuti_center'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[text()="מרכז מהותי"]')

    locators['footer_radio'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[text()="רדיו מהות החיים"]')
    locators['footer_soundcloud'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[contains(text(),"Soundcloud")]')
    locators['footer_tunein'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[contains(text(),"TuneIn")]')
    locators['footer_app_iphone'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[contains(text(),"iPhone")]')
    locators['footer_app_android'] = ('xpath', '//ul[@class="footer-links"]/descendant::a[contains(text(),"Android")]')



