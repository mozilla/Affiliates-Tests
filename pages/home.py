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

    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text
