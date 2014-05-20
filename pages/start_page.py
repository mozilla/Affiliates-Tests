#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class StartPage(Page):

    _page_title = 'Firefox Affiliates'

    _page_header_locator = (By.CSS_SELECTOR, '.contain > h1')

    #Not LoggedIn
    _login_browser_id_locator = (By.CSS_SELECTOR, 'a.persona-button')

    def __init__(self, testsetup, open_url=True):
        """ Creates a new instance of the class and gets the page ready for testing """
        Page.__init__(self, testsetup)
        if open_url:
            self.selenium.get(self.base_url)

    def login(self, user='default'):
        base = self.click_login_browser_id()
        base.login_user_browser_id(user)

        from pages.home import Home
        return Home(self.testsetup)

    def click_login_browser_id(self):
        self.selenium.find_element(*self._login_browser_id_locator).click()
        from pages.base import Base
        return Base(self.testsetup)

    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text.replace('\n', ' ')
