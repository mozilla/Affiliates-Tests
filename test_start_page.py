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
# Contributor(s):
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

from affiliates_page import AffiliatesBasePage
from affiliates_page import AffiliatesHomePage
from unittestzero import Assert
import pytest

class TestStartPage:

    def test_learn_more_tooltip_visibility(self, mozwebqa):
        home_page = AffiliatesHomePage(mozwebqa)
        home_page.hover_over_learn_more_link()
        Assert.true(home_page.is_learn_more_tooltip_visible)

    def test_registration_with_blank_form_data(self, mozwebqa):
        home_page = AffiliatesHomePage(mozwebqa)
        home_page.click_register_button()
        Assert.true(home_page.is_email_address_required)
        Assert.true(home_page.is_password_required)
        Assert.true(home_page.is_display_name_required)
        Assert.true(home_page.is_privacy_policy_acceptance_required)

    def test_registration_with_invalid_email_address(self, mozwebqa):
        home_page = AffiliatesHomePage(mozwebqa)
        home_page.set_display_name("John Doe")
        home_page.set_email_address("thisisinvalid")
        home_page.set_password("validpassword1")
        home_page.check_agreement_checkbox()
        home_page.click_register_button()
        Assert.true(home_page.is_valid_email_address_required)

    def test_registration_with_insecure_password(self, mozwebqa):
        home_page = AffiliatesHomePage(mozwebqa)
        home_page.set_display_name("John Doe")
        home_page.set_email_address("validemail@example.com")
        home_page.set_password("invalidwithoutnumber")
        home_page.check_agreement_checkbox()
        home_page.click_register_button()
        Assert.true(home_page.is_insecure_password_warning_present)