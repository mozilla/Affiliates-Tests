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
xfail = pytest.mark.xfail


class TestAboutPage:

    @credentials
    @nondestructive
    def test_about(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        about_page = home_page.click_about_nav_button()
        Assert.equal(home_page.header, 'About Firefox Affiliates')
        Assert.true(about_page.is_the_current_url)
        Assert.not_none(about_page.about_text)

    @credentials
    @nondestructive
    def test_faq(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        faq_page = home_page.click_about_nav_button()

        Assert.true(faq_page.questions_count > 0)
        #Pick one question from each section
        for i in range(4):
            Assert.not_none(faq_page.questions_text(i))
            Assert.not_none(faq_page.answer(i))
