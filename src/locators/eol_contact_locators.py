import random


class Contact_Locators():
    locators = dict()

    locators['form_name'] = ('xpath', '//input[@name="your-name"]')
    locators['form_email'] = ('xpath', '//input[@name="your-email"]')
    locators['form_content'] = ('xpath', '//textarea[@name="your-message"]')

    locators[''] = ('xpath', '')
