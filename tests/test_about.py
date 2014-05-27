#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.start_page import StartPage
from unittestzero import Assert

credentials = pytest.mark.credentials
nondestructive = pytest.mark.nondestructive


class TestAboutPage:

    @credentials
    @nondestructive
    def test_about_page_has_proper_titles(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        about_page = home_page.click_about_nav_link()
        Assert.true(about_page.is_the_current_url)
        Assert.equal(about_page.faq_header, 'Frequently Asked Questions')

    @credentials
    @nondestructive
    def test_about_text_present(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        about_page = home_page.click_about_nav_link()
        Assert.not_none(about_page.about_text)

    @credentials
    @nondestructive
    def test_about_page_faq_category_present(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        about_page = home_page.click_about_nav_link()
        Assert.true(about_page.category_count > 0)

    @credentials
    @nondestructive
    def test_about_page_faq_questions_present(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        about_page = home_page.click_about_nav_link()
        Assert.true(about_page.questions_count > 0)

    @credentials
    @nondestructive
    def test_about_page_faq_answers_present(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        about_page = home_page.click_about_nav_link()
        Assert.equal(about_page.questions_count, about_page.answers_count,
            'Questions count did not match answers count')
