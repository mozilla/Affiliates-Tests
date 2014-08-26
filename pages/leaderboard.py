#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from pages.base import Base
from pages.page import Page
from selenium.webdriver.common.by import By


class LeaderboardPage(Base):

    _title = (By.CSS_SELECTOR, '.page-title')
    _table = (By.CSS_SELECTOR, 'table.leaderboard tbody tr')

    @property
    def title(self):
        return self.selenium.find_element(*self._title).text

    @property
    def leaderboard_user_rows(self):
        return [self.LeaderboardUser(self.testsetup, row) for row in self.selenium.find_elements(*self._table)]

    @property
    def leaderboard_user_count(self):
        return len(self.selenium.find_elements(*self._table))

    class LeaderboardUser(Page):

        def __init__(self, testsetup, root_element):
            Page.__init__(self, testsetup)
            self._root_element = root_element

        def is_row_visible(self):
            return self._root_element.is_displayed()
