#!/usr/bin/env python
#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.start_page import StartPage
from unittestzero import Assert

import pytest

credentials = pytest.mark.credentials
nondestructive = pytest.mark.nondestructive


class TestStartPage:

    @nondestructive
    def test_start_page_has_proper_titles(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        Assert.true(start_page.is_the_current_page)
        Assert.equal(start_page.header, 'Become a Firefox Affiliate Today!')

    @credentials
    @nondestructive
    def test_login_logout_works_properly(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        Assert.true(home_page.is_user_logged_in, 'User not logged in')
        Assert.equal(home_page.header, 'Follow these easy steps to get started:')
        home_page.click_logout()
        Assert.false(home_page.is_user_logged_in, 'User logged in')
        Assert.equal(start_page.header, 'Become a Firefox Affiliate Today!')

    @nondestructive
    def test_start_page_logo_twitter_facebook_present(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        Assert.true(start_page.is_mozilla_logo_visible)
        Assert.true(start_page.is_twitter_button_present)
        Assert.true(start_page.is_facebook_button_present)

    @nondestructive
    def test_that_text_bubble_appears_on_hovering_learn_more_link(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        start_page.hover_over_learn_more_link()
        Assert.true(start_page.is_learn_more_tooltip_visible)
        Assert.greater(len(start_page.learn_more_tooltip_text), 0)
