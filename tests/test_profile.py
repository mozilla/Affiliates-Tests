#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from datetime import datetime

import pytest
from unittestzero import Assert

from pages.start_page import StartPage

credentials = pytest.mark.credentials
nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive


class TestProfilePage:

    @credentials
    @destructive
    @pytest.mark.xfail(reason='Bug 1040085 - [dev] [stage] The name displayed on the profile page is not matching the name in page header')
    def test_edit_profile_change_display_name(self, mozwebqa):
        cur_date_time = datetime.now()

        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        current_username = home_page.username
        new_username = mozwebqa.credentials['default']['name'] + str(cur_date_time)

        edit_page = home_page.click_profile()
        edit_page_modal = edit_page.click_edit_profile()

        edit_page_modal.set_display_name(new_username)
        edit_page_modal.click_cancel()
        Assert.equal(edit_page.username, current_username)

        edit_page_modal = edit_page.click_edit_profile()
        edit_page_modal.set_display_name(new_username)
        edit_page_modal.click_save_my_changes()
        Assert.equal(edit_page.get_expected_user(new_username.upper()), new_username.upper())

        # revert changes
        edit_page_modal = edit_page.click_edit_profile()
        edit_page_modal.set_display_name(current_username)
        edit_page_modal.click_save_my_changes()

    @credentials
    @destructive
    def test_edit_profile_set_website(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        edit_page = home_page.click_profile()
        edit_page_modal = edit_page.click_edit_profile()

        edit_page_modal.set_website('http://wiki.mozilla.com/')
        edit_page_modal.click_save_my_changes()
        Assert.true(edit_page.is_website_visible())
        Assert.equal(edit_page.view_website, 'http://wiki.mozilla.com/',
                     "Failed because expected 'http://wiki.mozilla.com' but returned "
                     + edit_page.view_website)

        # verify user can leave website field empty
        edit_page_modal = edit_page.click_edit_profile()
        edit_page_modal.set_website('')
        edit_page_modal.click_save_my_changes()
        edit_page_modal = edit_page.click_edit_profile()
        Assert.equal(edit_page_modal.website, '',
                     'Clearing the website field failed.')

    @credentials
    @nondestructive
    def test_verify_layout_logged_in_user(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        edit_page = home_page.click_profile()

        Assert.true(edit_page.is_stats_section_visible())
        Assert.true(edit_page.is_stats_ranking_visible())
        Assert.not_none(edit_page.stats_ranking, 'Stats rankings is null')
        Assert.true(edit_page.is_stats_banners_visible())
        Assert.not_none(edit_page.stats_banners, 'Stats banners is null')
        Assert.true(edit_page.is_stats_clicks_visible())
        Assert.not_none(edit_page.stats_clicks, 'Stats clickss is null')
        Assert.true(edit_page.is_milestones_section_visible())
        Assert.true(edit_page.is_newsletter_form_visible())

    @credentials
    @destructive
    def test_new_account_creation(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.create_new_account()

        Assert.true(home_page.is_user_logged_in)

        logged_out = home_page.logout()
        Assert.false(logged_out.is_user_logged_in)

        logged_in = logged_out.login()
        Assert.true(logged_in.is_user_logged_in)
