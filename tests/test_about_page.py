# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.start_page import StartPage


class TestAboutPage:

    @pytest.mark.nondestructive
    def test_about_page_has_proper_layout(self, base_url, selenium, existing_user):
        start_page = StartPage(base_url, selenium)
        home_page = start_page.login(existing_user['email'], existing_user['password'])
        about_page = home_page.click_about_nav_link()
        assert about_page.is_the_current_url
        assert 'Frequently Asked Questions' == about_page.faq_header
        assert about_page.about_text is not None, 'about page has no text to display'
        assert about_page.category_count > 0, 'FAQ category not present'
        assert about_page.questions_count > 0, 'No faq questions present in about page'
        about_page = home_page.click_about_nav_link()
        assert about_page.questions_count == about_page.answers_count, 'Questions count did not match answers count'
