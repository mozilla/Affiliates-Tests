#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class StartPage(Page):

    _page_title = 'Firefox Affiliates'

    _page_header_locator = (By.CSS_SELECTOR, '#content h2')
    _learn_more_link_locator = (By.CSS_SELECTOR, '#content .show_tooltip')
    _learn_more_tooltip_locator = (By.ID, 'tooltip_home')
    _mozilla_logo_link_locator = (By.CSS_SELECTOR, '#header a')
    _footer_locator = (By.CSS_SELECTOR, '#footer')
    _twitter_button_locator = (By.CSS_SELECTOR, '.button.share.twitter')
    _facebook_button_locator = (By.CSS_SELECTOR, '.button.share.facebook')

    #Not LoggedIn
    _login_browser_id_locator = (By.CSS_SELECTOR, 'a.persona-button')

    def __init__(self, testsetup, open_url=True):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        Page.__init__(self, testsetup)
        if open_url:
            self.selenium.get(self.base_url)

    def login(self, user='default'):
        # browser id is not logging in a normal mode and it requiters a refresh to login properly
        self.selenium.refresh()
        login = self.click_login_browser_id()
        login.login_user_browser_id(user)
        from pages.home import Home
        return Home(self.testsetup)

    def click_login_browser_id(self):
        self.selenium.find_element(*self._login_browser_id_locator).click()
        from pages.user import Login
        return Login(self.testsetup)

    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text.replace('\n', ' ')

    @property
    def is_twitter_button_present(self):
        return self.is_element_present(*self._twitter_button_locator)

    @property
    def is_facebook_button_present(self):
        return self.is_element_present(*self._facebook_button_locator)

    @property
    def is_mozilla_logo_visible(self):
        return self.is_element_visible(*self._mozilla_logo_link_locator)

    def click_mozilla_logo(self):
        self.selenium.find_element(*self._mozilla_logo_link_locator).click()

    def hover_over_learn_more_link(self):
        learn_more = self.selenium.find_element(*self._learn_more_link_locator)
        ActionChains(self.selenium).move_to_element(learn_more).perform()
        WebDriverWait(self.selenium, self.timeout).until(
                lambda s: s.find_element(*self._learn_more_tooltip_locator).get_attribute('style') == "display: block;")

    @property
    def is_learn_more_tooltip_visible(self):
        return self.is_element_visible(*self._learn_more_tooltip_locator)

    @property
    def learn_more_tooltip_text(self):
        return self.selenium.find_element(*self._learn_more_tooltip_locator).text
