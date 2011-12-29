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
# Contributor(s): Bebe <florin.strugariu@softvision.ro>
#                 Stephen Donner
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

from selenium.webdriver.common.by import By

from page import Page


class Login(Page):

    _login_browser_id_locator = (By.CSS_SELECTOR, '.browserid:nth-of-type(1)')

    def login_user_browser_id(self, user):
        from pages.browser_id import BrowserID
        pop_up = BrowserID(self.testsetup)
        pop_up.login_browser_id(user)
        pop_up.sign_in()


class Register(Page):

    _register_browser_id_locator = (By.CSS_SELECTOR, '.browserid:nth-of-type(2)')
    _display_name_field_locator = (By.ID, 'id_display_name')
    _display_name_warning = 'Please enter a display name'
    _agreement_checkbox_locator = (By.ID, 'id_agreement')
    _subscribe_email_locator = (By.ID, 'id_email_subscribe')
    _register_button_locator = (By.CSS_SELECTOR, '#register-form .register')

    _message_warning_locator = (By.CSS_SELECTOR, '#home-registration-forms .msg_warning:contains(%s)')
    _privacy_policy_warning = 'You must agree to the terms of service and privacy policy to register'

    def set_display_name(self, display_name):
        self.selenium.find_element(*self._display_name_field_locator).send_keys(display_name)

    def check_agreement_checkbox(self):
        self.selenium.find_element(*self._agreement_checkbox_locator).click()

    def click_register_button(self):
        self.selenium.find_element(*self._register_button_locator).click()

    def is_warning_present(self, warning_text):
        return self.is_element_present(self._message_warning_locator % warning_text)

    @property
    def is_display_name_required(self):
        return self.is_warning_present(self._display_name_warning)

    @property
    def is_privacy_policy_acceptance_required(self):
        return self.is_warning_present(self._privacy_policy_warning)


class User(Page):

        _username_locator = (By.CSS_SELECTOR, '#user-info div')

        @property
        def username(self):
            return self.selenium.find_element(*self._username_locator).text


class EditProfile(Page):

    _page_header = 'Edit your user profile'

    _display_name_locator = (By.ID, 'id_display_name')
    _full_name_locator = (By.ID, 'id_name')
    _street_locator = (By.ID, 'id_address_1')
    _appartment_locator = (By.ID, 'id_address_2')
    _city_locator = (By.ID, 'id_city')
    _state_locator = (By.ID, 'id_state')
    _postal_code_locator = (By.ID, 'id_postal_code')
    _country_locator = (By.ID, 'id_country')
    _locale_locator = (By.ID, 'id_locale')
    _save_my_changes_locator = (By.CSS_SELECTOR, '.save_changes')
    _cancel_locator = (By.CSS_SELECTOR, '.button')

    @property
    def get_input_text_for(self, for_field):
        return self.selenium.find_element(*getattr(self, '_%s_locator' % for_field)).text

    def set_input_text_for(self, for_field, value):
        self.selenium.find_element(*getattr(self, '_%s_locator' % for_field)).send_keys(value)
    
    @property
    def get_label_text_for(self, for_label):
        locator = getattr(self, "_%s_locator" % for_label)
        return self.selenium.find_element(locator[0], 'label[for=\'%s\']' % locator[1]).text

    def click_save_my_changes(self):
        self.selenium.find_element(*self._save_my_changes_locator).click()

    def click_cancel(self):
        self.selenium.find_element(*self._cancel_locator).click()
