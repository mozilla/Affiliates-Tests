#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.start_page import StartPage
from unittestzero import Assert

import pytest

nondestructive = pytest.mark.nondestructive


class TestStartPage:

    @nondestructive
    def test_start_page_has_proper_titles(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        Assert.true(start_page.is_the_current_page)
        Assert.equal(start_page.header, 'Become a Firefox Affiliate today!')

    @nondestructive
    def test_login_logout_works_properly(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        Assert.true(home_page.is_user_logged_in, 'User not logged in')
        Assert.equal(home_page.header, 'Dashboard')
        home_page.logout()
        Assert.false(home_page.is_user_logged_in, 'User logged in')
        Assert.equal(start_page.header, 'Become a Firefox Affiliate today!')
