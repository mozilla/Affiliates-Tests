# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from datetime import datetime

import pytest

from pages.start_page import StartPage

destructive = pytest.mark.destructive


class TestProfilePage:

    @destructive
    def test_edit_profile_change_display_name(self, mozwebqa, existing_user):
        start_page = StartPage(mozwebqa)
        new_username = "Testbot: %s" % (datetime.now())
        home_page = start_page.login(existing_user['email'], existing_user['password'])
        profile_page = home_page.click_profile()

        # verify changing username, update username to include a timestamp
        profile_page.update_profile_name(new_username)
        assert new_username == profile_page.profile_username, 'Username did not update'

        # verify username persists after logging out and then logging back in
        logged_out = profile_page.logout()
        home_page = logged_out.login(existing_user['email'], existing_user['password'])
        profile_page = home_page.click_profile()
        assert new_username == profile_page.profile_username, 'Username change did not persist after logout'

        # verify user can leave username field empty
        profile_page.update_profile_name("")
        assert 'Affiliate' == profile_page.profile_username, 'Blank username did not use default value'

    @destructive
    def test_edit_profiles_website(self, mozwebqa, existing_user):
        start_page = StartPage(mozwebqa)
        new_url = 'http://wiki.mozilla.org/' + datetime.utcnow().strftime("%s")
        home_page = start_page.login(existing_user['email'], existing_user['password'])
        profile_page = home_page.click_profile()

        # update profile website to include a timestamp
        profile_page.update_profile_website(new_url)
        assert new_url == profile_page.profile_website, 'Website did not update'

        # verify username persists after logging out and then logging back in
        logged_out = profile_page.logout()
        home_page = logged_out.login(existing_user['email'], existing_user['password'])
        profile_page = home_page.click_profile()
        assert new_url == profile_page.profile_website, 'Website change did not persist after logout'

        # verify user can leave website field empty
        profile_page.update_profile_website("")
        assert '' == profile_page.profile_website, 'Blank website was not accepted'

    @destructive
    def test_verify_layout_logged_in_user(self, mozwebqa, existing_user):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login(existing_user['email'], existing_user['password'])
        edit_page = home_page.click_profile()
        assert edit_page.is_stats_section_visible()
        assert edit_page.is_stats_ranking_visible()
        assert edit_page.stats_ranking is not None
        assert edit_page.is_stats_banners_visible()
        assert edit_page.stats_banners is not None
        assert edit_page.is_stats_clicks_visible()
        assert edit_page.stats_clicks is not None
        assert edit_page.is_milestones_section_visible()

    @destructive
    def test_new_account_creation(self, mozwebqa, new_user):
        start_page = StartPage(mozwebqa)
        start_page.login(new_user['email'], new_user['password'], error=True)
        assert start_page.error == 'Login failed. Firefox Affiliates has stopped accepting new users.'
