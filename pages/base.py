#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from pages.page import Page


class Base(Page):

    #LoggedIn
    _logout_locator = (By.CSS_SELECTOR, '#nav-user-submenu li a.browserid-logout')
    _profile_locator = (By.CSS_SELECTOR, '#nav-user-submenu li:nth-of-type(2) a')
    _username_locator = (By.CSS_SELECTOR, '#nav-main-menu > li.user > a')

    #Content Navigation
    _about_content_nav_locator = (By.CSS_SELECTOR, '#nav-main-menu li:nth-of-type(1) a')

    def _hover_user_menu(self):
        username = self.selenium.find_element(*self._username_locator)
        ActionChains(self.selenium).move_to_element(username).perform()

    @property
    def is_user_logged_in(self):
        return self.is_element_present(*self._logout_locator)

    @property
    def username(self):
        return self.selenium.find_element(*self._username_locator).text

    def click_logout(self):
        self._hover_user_menu()
        self.selenium.find_element(*self._logout_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: not self.is_user_logged_in)

    def click_profile(self):
        self._hover_user_menu()
        self.selenium.find_element(*self._profile_locator).click()
        from pages.user import EditProfile
        return EditProfile(self.testsetup)

    def click_about_nav_button(self):
        self.selenium.find_element(*self._about_content_nav_locator).click()
        from pages.about import About
        return About(self.testsetup)

    def login_user_browser_id(self, user):
        credentials = self.testsetup.credentials[user]
        from browserid import BrowserID
        browserid = BrowserID(self.selenium, self.timeout)
        browserid.sign_in(credentials['email'], credentials['password'])
        WebDriverWait(self.selenium, self.timeout).until(lambda s: s.find_element(*self._logout_locator))
