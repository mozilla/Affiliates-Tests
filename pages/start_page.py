#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base


class StartPage(Base):

    _page_title = 'Firefox Affiliates'

    _page_header_locator = (By.CSS_SELECTOR, '.contain > h1')

    #Not LoggedIn
    _login_browser_id_locator = (By.CSS_SELECTOR, 'a.persona-button')

    def __init__(self, testsetup, open_url=True):
        """ Creates a new instance of the class and gets the page ready for testing """
        Base.__init__(self, testsetup)
        if open_url:
            self.open('/')

    def login(self, user='default'):
        base = self.click_login_browser_id()
        base.login_user_browser_id(user)

        from pages.home import Home
        return Home(self.testsetup)

    def login_with_credentials(self, credentials):
        """Log in using a vouched email from personatestuser.org"""
        self.click_login_browser_id()
        from browserid import BrowserID
        pop_up = BrowserID(self.selenium, self.timeout)
        pop_up.sign_in(credentials['email'], credentials['password'])

        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_user_logged_in)

        from pages.home import Home
        return Home(self.testsetup)

    def click_login_browser_id(self):
        self.selenium.find_element(*self._login_browser_id_locator).click()
        from pages.base import Base
        return Base(self.testsetup)


    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text.replace('\n', ' ')
