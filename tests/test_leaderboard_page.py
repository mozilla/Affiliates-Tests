#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest

from pages.start_page import StartPage
from unittestzero import Assert

credentials = pytest.mark.credentials
nondestructive = pytest.mark.nondestructive


class TestLeaderboardPage():

    @credentials
    @nondestructive
    def test_logged_in_user_can_reach_leaderboard(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        leaderboard_page = home_page.click_leaderboard_link()
        Assert.contains('Top Affiliates', leaderboard_page.title)

    @nondestructive
    def test_leaderboard_layout_for_guest_users(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        leaderboard_page = start_page.click_leaderboard_link()
        Assert.contains('Top Affiliates', leaderboard_page.title)
        Assert.greater('Leaderboard is empty',
                       0, leaderboard_page.leaderboard_user_count)

        for user_row in leaderboard_page.leaderboard_user_rows:
            Assert.true('Row not visible. Row info: %s' % user_row,
                        user_row.is_row_visible())
