#!/usr/bin/env python
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


class TestStartPage:

    @nondestructive
    @pytest.mark.native
    def test_learn_more_tooltip_visibility(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        start_page.hover_over_learn_more_link()
        Assert.true(start_page.is_learn_more_tooltip_visible)

    @nondestructive
    def test_start_page_has_proper_titles(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        Assert.true(start_page.is_the_current_page)
        Assert.equal(start_page.header, 'Become a Firefox Affiliate Today!')

    @nondestructive
    def test_login_logout_works_properly(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        home_page = start_page.login()
        Assert.true(home_page.is_user_logged_in, 'User not logged in')
        Assert.equal(home_page.header, 'Follow these easy steps to get started:')
        home_page.click_logout()
        Assert.false(home_page.is_user_logged_in, 'User logged in')
        Assert.equal(start_page.header, 'Become a Firefox Affiliate Today!')

    @nondestructive
    def test_start_page_logo_twitter_facebook_present(self, mozwebqa):
        start_page = StartPage(mozwebqa)
        Assert.true(start_page.is_mozilla_logo_visible)
        Assert.true(start_page.is_twitter_button_present)
        Assert.true(start_page.is_facebook_button_present)
