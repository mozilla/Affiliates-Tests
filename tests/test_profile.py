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
    def test_edit_profile_change_display_name(self, mozwebqa):
        new_username = "%s: %s" % \
            (mozwebqa.credentials['default']['name'], str(datetime.now()))

        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        profile_page = home_page.click_profile()

        # verify changing username, update username to include a timestamp
        profile_page.update_profile_name(new_username)
        actual_username = profile_page.profile_username

        Assert.equal(actual_username , new_username,
            "Failed: username on profile page failed to update. Expected: '%s' \
            , but returned '%s'" %
            (new_username, actual_username))

        leader_board_page = profile_page.click_leaderboard_link()

        Assert.equal(leader_board_page.username, new_username.upper(),
            "Failed: username in header of leaderboard failed to update. \
            Expected '%s', but returned '%s'" %
            (new_username.upper(), leader_board_page.username))

        # verify username persists after logging out and then logging back in
        logged_out = profile_page.logout()
        home_page = logged_out.login()
        profile_page = home_page.click_profile()

        actual_username = profile_page.profile_username

        Assert.equal(actual_username, new_username,
            "Failed: update to username did not persist after logout. \
            Expected '%s', but returned '%s'" %
            (new_username, actual_username))

        # verify user can leave username field empty
        profile_page.update_profile_name("")
        actual_username = profile_page.profile_username

        Assert.equal(actual_username, "Affiliate",
            "Failed: leaving username blank should default profile username \
            to 'Affiliate'. Expected 'Affiliate', but returned '%s'" %
            actual_username)

    @credentials
    @destructive
    def test_edit_profile_website(self, mozwebqa):
        new_url = 'http://wiki.mozilla.org/'  + datetime.utcnow().strftime("%s")

        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        profile_page = home_page.click_profile()

        # update profile website to include a timestamp
        profile_page.update_profile_website(new_url)
        actual_website = profile_page.profile_website

        Assert.equal(actual_website, new_url,
                     "update to website on profile edit page. \
                     Expected '%s' but returned '%s'" %
                     (new_url, actual_website))

        # verify username persists after logging out and then logging back in
        logged_out = profile_page.logout()
        home_page = logged_out.login()
        profile_page = home_page.click_profile()

        actual_website = profile_page.profile_website

        Assert.equal(actual_website, new_url,
                     "update to website did not persist after logout. \
                     Expected '%s', but returned '%s'" %
                     (new_url, actual_website))

        # verify user can leave website field empty
        profile_page.update_profile_website("")
        actual_website = profile_page.profile_website

        Assert.equal(actual_website, "",
                     "user can't set website URL to an empty string. \
                      Expected '', returned '%s'" %
                      actual_website)


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
