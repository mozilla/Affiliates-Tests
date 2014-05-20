#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.base import Base


class Home(Base):

    _page_title = 'Firefox Affiliates - Mozilla Firefox'
    _page_url = '/dashboard'

    _page_header_locator = (By.CSS_SELECTOR, '.page-head .page-title')
    _about_content_nav_locator = (By.CSS_SELECTOR, 
        'ul#nav-main-menu li:nth-of-type(1) a')

    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text

    def click_about_nav_link(self):
        self.selenium.find_element(*self._about_content_nav_locator).click()
        from pages.about import About
        return About(self.testsetup)
