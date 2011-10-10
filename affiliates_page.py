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
# Portions created by the Initial Developer are Copyright (C) 2011
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

from selenium import selenium
import re
import time
import base64
from page import Page

class AffiliatesBasePage(Page):

    def __init__(self, testsetup):
        Page.__init__(self, testsetup)
        self.sel = self.selenium
        self.sel.open("/")

    @property
    def page_title(self):
        return self.sel.get_title()

class AffiliatesHomePage(AffiliatesBasePage):

    _display_name_field_locator = 'id=id_display_name'
    _email_field_locator = 'id=id_email'
    _password_field_locator = 'css=#register-form #id_password'
    _agreement_checkbox_locator = 'id=id_agreement'
    _register_button_locator = 'css=#register-form .register'
    _forgot_password_link_locator = 'css=#login-form a[href*="forgot_password"]'
    _learn_more_link_locator = 'css=#content .show_tooltip'
    _learn_more_tooltip_locator = 'id=tooltip_home'
    _message_warning_locator = 'css=#home-registration-forms .msg_warning:contains(%s)'
    _password_warning = 'Please enter a password'
    _display_name_warning = 'Please enter a display name'
    _email_address_warning = 'Please enter an email address'
    _valid_email_address_warning = 'Enter a valid e-mail address'
    _privacy_policy_warning = 'You must agree to the terms of service and privacy policy to register'
    _insecure_password_warning = 'Passwords must contain at least 1 letter and 1 number'

    def set_display_name(self, display_name):
        self.sel.type(self._display_name_field_locator, display_name)

    def set_email_address(self, email_address):
        self.sel.type(self._email_field_locator, email_address)

    def set_password(self, password):
        self.sel.type(self._password_field_locator, password)

    def check_agreement_checkbox(self):
        self.sel.check(self._agreement_checkbox_locator)

    def click_register_button(self):
        self.sel.click(self._register_button_locator)
        self.sel.wait_for_page_to_load(self.timeout)

    def click_forgot_password_link(self):
        self.sel.click(self._forgot_password_link_locator)
        self.sel.wait_for_page_to_load(self.timeout)
        return AffiliatesForgotPasswordPage(testsetup)

    def hover_over_learn_more_link(self):
        self.sel.mouse_over(self._learn_more_link_locator)

    def is_warning_present(self, warning_text):
        return self.sel.is_element_present(self._message_warning_locator % warning_text)

    @property
    def is_password_required(self):
        return self.is_warning_present(self._password_warning)

    @property
    def is_display_name_required(self):
        return self.is_warning_present(self._display_name_warning)

    @property
    def is_email_address_required(self):
        return self.is_warning_present(self._email_address_warning)

    @property
    def is_valid_email_address_required(self):
        return self.is_warning_present(self._valid_email_address_warning)

    @property
    def is_privacy_policy_acceptance_required(self):
        return self.is_warning_present(self._privacy_policy_warning)

    @property
    def is_insecure_password_warning_present(self):
        return self.is_warning_present(self._insecure_password_warning)

    @property
    def is_learn_more_tooltip_visible(self):
        return self.sel.is_visible(self._learn_more_tooltip_locator)

class AffiliatesForgotPasswordPage(AffiliatesBasePage):

    _forgot_password_heading_locator = 'css=#content h2:contains(Forgot password on Firefox Affiliates)'
    _send_button_locator = 'css=#forgot-password-form button[type="submit"]'

    @property
    def is_forgot_password_heading_present(self):
        return self.sel.is_element_present(self._forgot_password_heading_locator)

    @property
    def is_send_button_present(self):
        return self.sel.is_element_present(self.send_button_locator)

    def click_send_button(self):
        self.sel.click(self._send_button_locator)
        self.sel.wait_for_page_to_load(timeout)
        return AffiliatesPasswordResetConfirmedPage(testsetup)

class AffiliatesPasswordResetConfirmedPage(AffiliatesBasePage):

    _password_reset_heading_locator = 'css=#content h2:contains(Password Reset)'
    _password_reset_text = 'We\'ve sent an email to any account using this email address'

    @property
    def is_password_reset_heading_visible(self):
        return self.sel.is_visible(self._password_reset_heading_locator)

    @property
    def is_description_present(self):
        return self.sel.is_text_present(self._password_reset_text)