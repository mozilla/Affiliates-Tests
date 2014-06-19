#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import pytest

from pages.start_page import StartPage
from pages.leaderboard import LeaderboardPage
from unittestzero import Assert

credentials = pytest.mark.credentials
nondestructive = pytest.mark.nondestructive


class TestLeaderboardPage:

    @credentials
    @nondestructive
    def test_leaderboard_is_present(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        leaderboard_page = LeaderboardPage(mozwebqa)
        leaderboard_page.go_to_page()
        Assert.contains('Top Affiliates', leaderboard_page.leaderboard_header_text)

        
    
