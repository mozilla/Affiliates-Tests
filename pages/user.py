#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class Login(Page):

    _home_logout_locator = (By.CSS_SELECTOR, '#sidebar-nav li:nth-of-type(1) a')

    def login_user_browser_id(self, user):
        credentials = self.testsetup.credentials[user]
        from browserid import BrowserID
        browserid = BrowserID(self.selenium, self.timeout)
        browserid.sign_in(credentials['email'], credentials['password'])
        WebDriverWait(self.selenium, 10).until(lambda s: s.find_element(*self._home_logout_locator))


class Register(Page):

    _display_name_field_locator = (By.ID, 'id_display_name')
    _display_name_warning = 'Please enter a display name'
    _agreement_checkbox_locator = (By.ID, 'id_agreement')
    _subscribe_email_locator = (By.ID, 'id_email_subscribe')
    _register_button_locator = (By.CSS_SELECTOR, '#register-form .register')

    _message_warning_locator = (By.XPATH, "//div[@id='home-registration-forms']/p[contains(text(), '%s')]")
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


class EditProfile(Page):

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

    def get_input_text_for(self, for_field):
        return self.selenium.find_element(*getattr(self, '_%s_locator' % for_field)).get_attribute('value')

    def set_input_text_for(self, for_field, value):
        input_field = self.selenium.find_element(*getattr(self, '_%s_locator' % for_field))
        input_field.clear()
        input_field.send_keys(value)

    def get_label_text_for(self, for_label):
        locator = getattr(self, "_%s_locator" % for_label)
        return self.selenium.find_element(By.CSS_SELECTOR, 'label[for=\'%s\']' % locator[1]).text

    def click_save_my_changes(self):
        self.selenium.find_element(*self._save_my_changes_locator).click()

    def click_cancel(self):
        self.selenium.find_element(*self._cancel_locator).click()
