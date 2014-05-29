#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.start_page import StartPage
from unittestzero import Assert


credentials = pytest.mark.credentials
nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive


class TestProfilePage:

    @credentials
    @nondestructive
    def test_edit_profile_has_proper_display_name(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        username = mozwebqa.credentials['default']['name']

        edit_page = home_page.click_profile()
        Assert.equal(home_page.header, username)
        edit_page_modal = edit_page.click_edit_profile()
        Assert.equal(edit_page_modal.display_name_label, 'DISPLAY NAME')
        Assert.equal(edit_page_modal.display_name, username)

    @credentials
    @destructive
    def test_edit_profile_change_display_name(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login('technical_debt')
        username = mozwebqa.credentials['technical_debt']['name']
        edit_page = home_page.click_profile()
        edit_page_modal = edit_page.click_edit_profile()

        edit_page_modal.set_display_name('affiliates_name')
        edit_page_modal.click_cancel()
        Assert.equal(home_page.username, username.upper())

        edit_page_modal = edit_page.click_edit_profile()
        new_name = 'affiliates_test'
        edit_page_modal.set_display_name(new_name)
        edit_page_modal.click_save_my_changes()
        Assert.equal(home_page.username, new_name.upper())

        # revert changes
        edit_page_modal = edit_page.click_edit_profile()
        edit_page_modal.set_display_name(username)
        edit_page_modal.click_save_my_changes()

    @credentials
    @destructive
    def test_edit_profile_set_website(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        username = mozwebqa.credentials['default']['name']
        edit_page = home_page.click_profile()
        edit_page_modal = edit_page.click_edit_profile()

        website_url = 'http://wiki.mozilla.com'
        edit_page_modal.set_website(website_url)
        edit_page_modal.click_save_my_changes()
        Assert.contains(website_url, edit_page.view_website, 'Read-only website did not match the saved website.')

        # revert changes
        edit_page_modal = edit_page.click_edit_profile()
        edit_page_modal.set_website('')
        edit_page_modal.click_save_my_changes()
