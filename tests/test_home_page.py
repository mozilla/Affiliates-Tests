#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.start_page import StartPage
from unittestzero import Assert

import pytest

nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive
xfail = pytest.mark.xfail


class TestHomePage:

    @nondestructive
    @pytest.mark.xfail("config.getvalue('base_url') == 'https://affiliates-dev.allizom.org'", reason="[dev] Error when trying to edit profile")
    def test_edit_profile_has_proper_display_name(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        username = mozwebqa.credentials['default']['name']

        edit_page = home_page.click_edit_profile()
        Assert.equal(home_page.header, 'Edit your user profile')
        Assert.equal(edit_page.get_label_text_for('display_name'), 'DISPLAY NAME')
        Assert.equal(edit_page.get_input_text_for('display_name'), username)

    @destructive
    def test_edit_profile_change_display_name(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login('technical_debt')
        username = mozwebqa.credentials['technical_debt']['name']
        edit_page = home_page.click_edit_profile()

        edit_page.set_input_text_for('display_name', 'affiliates_name')
        edit_page.click_cancel()
        Assert.equal(home_page.username, username)

        home_page.click_edit_profile()
        new_name = 'affiliates_test'
        edit_page.set_input_text_for('display_name', new_name)
        edit_page.click_save_my_changes()
        Assert.equal(home_page.username, new_name)
        # revert changes
        home_page.click_edit_profile()
        edit_page.set_input_text_for('display_name', username)
        edit_page.click_save_my_changes()

    @nondestructive
    def test_about_page(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        about_page = home_page.click_about_nav_button()
        Assert.equal(home_page.header, 'About Affiliates')
        Assert.true(about_page.is_the_current_url)
        Assert.not_none(about_page.about_text)

    @nondestructive
    def test_faq_page(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        faq_page = home_page.click_faq_nav_button()
        Assert.equal(home_page.header, 'FAQs')
        Assert.true(faq_page.is_the_current_url)

        Assert.true(faq_page.questions_count > 0)
        #Pick one question from each section
        for i in range(4):
            i += 1
            Assert.not_none(faq_page.questions_text)
            faq_page.expand_question_by_section(i)
            Assert.not_none(faq_page.answer(i))

    @nondestructive
    def test_get_started_3_steps(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        Assert.true(home_page.is_the_current_url)
        Assert.greater(home_page.category_count, 0, 'There are no categories in the list')
        Assert.not_none(home_page.categories[0].name)
        Assert.true(home_page.is_step_button_selected('first'))
        # select the first category in the list
        home_page.categories[0].select_category('second')
        Assert.true(home_page.is_step_button_selected('second'))
        Assert.not_none(home_page.categories[0].name)
        # select the first banner in list
        home_page.categories[0].select_category('third')
        Assert.true(home_page.is_step_button_selected('third'))

    @nondestructive
    def test_change_banner_size_correct(self, mozwebqa):
        size = '300x250'
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        home_page.categories[0].select_category()
        home_page.categories[0].select_category()
        home_page.select_size(size)
        Assert.contains(size, home_page.banner_size_text)
