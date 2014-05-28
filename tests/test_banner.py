#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.start_page import StartPage
from unittestzero import Assert

credentials = pytest.mark.credentials
destructive = pytest.mark.destructive


class TestBanners:

    @credentials
    @destructive
    def test_user_can_create_banner(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        create_banner_page = home_page.click_create_banner()
        create_banner_page.choose_category()
        create_banner_page.choose_banner()
        create_banner_page.select_language('English (US)')
        create_banner_page.select_size()
        create_banner_page.select_color()
        create_banner_page.click_save()
        Assert.true(create_banner_page.is_embeded_code_generated)

        # Get the id of the new banner from the page url
        new_banner_id = create_banner_page.get_url_current_page.split('/')[-2]
        create_banner_page.go_to_dashboard_page()

        # Get the id of the last created banner in the list
        last_banner_id = home_page.banners[len(home_page.banners) - 1].banner_link.split('/')[-2]

        #Check that the new banner is the last on the list of banners
        Assert.equal(new_banner_id, last_banner_id)
