#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Selenium Tests.
#
# The Initial Developer of the Original Code is
# Mozilla.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Sergey Tupchiy (tupchii.sergii@gmail.com)
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from pages.start_page import StartPage
from unittestzero import Assert

import pytest

nondestructive = pytest.mark.nondestructive
destructive = pytest.mark.destructive
xfail = pytest.mark.xfail


class TestHomePage:

    @nondestructive
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
        home_page = start_page.login()
        username = mozwebqa.credentials['default']['name']
        edit_page = home_page.click_edit_profile()

        edit_page.set_input_text_for('display_name', 'affiliates_name')
        edit_page.click_cancel()
        Assert.equal(home_page.username, username)

        home_page.click_edit_profile()
        new_name = 'affiliates_test'
        edit_page.set_input_text_for('display_name', new_name)
        edit_page.click_save_my_changes()
        Assert.equal(home_page.username, new_name)
        #Back changes to normal
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
        Assert.greater(home_page.category_count, 0, 'There is no categories in list')
        Assert.not_none(home_page.categories[0].name)
        Assert.true(home_page.is_step_button_selected('first'))
        #Select first Category in list
        home_page.categories[0].select_category()
        Assert.true(home_page.is_step_button_selected('second'))
        Assert.not_none(home_page.categories[0].name)
        #Select first Banner in list
        home_page.categories[0].select_category()
        Assert.true(home_page.is_step_button_selected('third'))
        #Commenting out - ui changed
        #Assert.equal(home_page.banner_url, home_page.banner_preview_url)
        #Assert.equal(home_page.banner_img_src, home_page.banner_preview_img_src)

    @xfail(reason="Changed UI")
    @nondestructive
    def test_change_banner_size_correct(self, mozwebqa):
        size = '180x150'
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()

        home_page.categories[0].select_category()
        home_page.categories[0].select_category()
        home_page.select_size(size)
        Assert.contains(size, home_page.banner_html_code)
