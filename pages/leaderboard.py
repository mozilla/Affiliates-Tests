#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from pages.base import Base
from selenium.webdriver.common.by import By

class LeaderboardPage(Base):

    _title = (By.CSS_SELECTOR, '.page-title')
    
    _leaderboard_page_url = '/leaderboard/'

    def go_to_page(self):
        self.open(self._leaderboard_page_url)

    @property
    def title(self):
        return self.selenium.find_element(*self._title).text
