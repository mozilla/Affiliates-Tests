# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base
from page import Page


class Home(Base):

    _page_title = 'Firefox Affiliates - Mozilla Firefox'
    _page_url = '/dashboard'

    _page_header_locator = (By.CSS_SELECTOR, '.page-head .page-title')
    _about_content_nav_locator = (By.CSS_SELECTOR, 'ul#nav-main-menu li:nth-of-type(1) a')
    _banners_list_locator = (By.CSS_SELECTOR, '.banners-list .banner')

    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text

    def click_about_nav_link(self):
        self.selenium.find_element(*self._about_content_nav_locator).click()
        from pages.about import About
        return About(self.testsetup)

    @property
    def banners(self):
        return [self.Banners(self.testsetup, banner) for banner in self.selenium.find_elements(*self._banners_list_locator)]

    class Banners(Page):

        _banner_id_locator = (By.CSS_SELECTOR, 'a')

        def __init__(self, testsetup, banner):
            Page.__init__(self, testsetup)
            self._root_element = banner

        @property
        def banner_link(self):
            return self._root_element.find_element(*self._banner_id_locator).get_attribute('href')
