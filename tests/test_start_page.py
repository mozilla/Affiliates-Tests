# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.start_page import StartPage

import pytest

nondestructive = pytest.mark.nondestructive


class TestStartPage:

    @nondestructive
    def test_start_page_has_proper_titles(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        assert start_page.is_the_current_page
        assert 'Important Notice: Firefox Affiliates is being discontinued' == start_page.header

    @nondestructive
    def test_login_logout_works_properly(self, mozwebqa, existing_user):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login(existing_user['email'], existing_user['password'])
        assert home_page.is_user_logged_in
        assert 'Dashboard' == home_page.header
        home_page.logout()
        assert not home_page.is_user_logged_in
        assert 'Important Notice: Firefox Affiliates is being discontinued' == start_page.header
