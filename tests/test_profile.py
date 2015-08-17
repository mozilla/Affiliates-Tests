#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from datetime import datetime

import pytest
from unittestzero import Assert

from pages.start_page import StartPage

destructive = pytest.mark.destructive


class TestProfilePage:

    @destructive
    def test_edit_profile_change_display_name(self, mozwebqa, existing_user):
        new_username = "Testbot: %s" % (datetime.now())

        start_page = StartPage(mozwebqa)
        home_page = start_page.login(existing_user['email'], existing_user['password'])
        profile_page = home_page.click_profile()

        # verify changing username, update username to include a timestamp
        profile_page.update_profile_name(new_username)
        actual_username = profile_page.profile_username

        Assert.equal(actual_username, new_username,
                     "Failed: username on profile page failed to update. "
                     "Expected: '%s', but returned '%s'" % (
                         new_username, actual_username))

        # verify username persists after logging out and then logging back in
        logged_out = profile_page.logout()
        home_page = logged_out.login(existing_user['email'], existing_user['password'])
        profile_page = home_page.click_profile()

        actual_username = profile_page.profile_username

        Assert.equal(actual_username, new_username,
                     "Failed: update to username did not persist after logout. "
                     "Expected '%s', but returned '%s'" % (
                         new_username, actual_username))

        # verify user can leave username field empty
        profile_page.update_profile_name("")
        actual_username = profile_page.profile_username

        Assert.equal(actual_username, "Affiliate",
                     "Failed: leaving username blank should default profile username "
                     "to 'Affiliate'. Expected 'Affiliate', but returned '%s'" % actual_username)

    @destructive
    def test_edit_profiles_website(self, mozwebqa, existing_user):
        start_page = StartPage(mozwebqa)
        new_url = 'http://wiki.mozilla.org/' + datetime.utcnow().strftime("%s")
        home_page = start_page.login(existing_user['email'], existing_user['password'])
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
        home_page = logged_out.login(existing_user['email'], existing_user['password'])
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
                     "user can't set website URL to an empty string. "
                     "Expected '', returned '%s'" % actual_website)

    @destructive
    def test_verify_layout_logged_in_user(self, mozwebqa, existing_user):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login(existing_user['email'], existing_user['password'])
        edit_page = home_page.click_profile()

        Assert.true(edit_page.is_stats_section_visible())
        Assert.true(edit_page.is_stats_ranking_visible())
        Assert.not_none(edit_page.stats_ranking, 'Stats rankings is null')
        Assert.true(edit_page.is_stats_banners_visible())
        Assert.not_none(edit_page.stats_banners, 'Stats banners is null')
        Assert.true(edit_page.is_stats_clicks_visible())
        Assert.not_none(edit_page.stats_clicks, 'Stats clicks is null')
        Assert.true(edit_page.is_milestones_section_visible())

    @destructive
    def test_new_account_creation(self, mozwebqa, new_user):
        start_page = StartPage(mozwebqa)
        start_page.login(new_user['email'], new_user['password'], error=True)
        assert start_page.error == 'Login failed. Firefox Affiliates has stopped accepting new users.'
