#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class EditProfile(Page):

    _edit_profile_locator = (By.ID, 'edit-profile-link')

    def click_edit_profile(self):
        self.selenium.find_element(*self._edit_profile_locator).click()
        return self.EditProfileModal(self.testsetup)

    class EditProfileModal(Page):

        _modal_locator = (By.CSS_SELECTOR, '#profile > div#modal')

        _save_locator = (By.CSS_SELECTOR, '.button.go')
        _cancel_locator = (By.CSS_SELECTOR, '.button.close')

        def __init__(self, testsetup):
            Page.__init__(self, testsetup)
            WebDriverWait(self.selenium, self.timeout).until(
                lambda s: self.is_element_visible(*self._modal_locator))
            self._root_element = self.selenium.find_element(*self._modal_locator)

        def get_input_text_for(self, for_field):
            return self._root_element.find_element(*getattr(self, '_%s_locator' % for_field)).get_attribute('value')

        def set_input_text_for(self, for_field, value):
            input_field = self._root_element.find_element(*getattr(self, '_%s_locator' % for_field))
            input_field.clear()
            input_field.send_keys(value)

        def get_label_text_for(self, for_label):
            locator = getattr(self, "_%s_locator" % for_label)
            return self._root_element.find_element(By.CSS_SELECTOR, 'label[for=\'%s\']' % locator[1]).text

        def click_save_my_changes(self):
            self._root_element.find_element(*self._save_locator).click()
            WebDriverWait(self.selenium, self.timeout).until(
                lambda s: not self.is_element_visible(*self._modal_locator))

        def click_cancel(self):
            self._root_element.find_element(*self._cancel_locator).click()
            WebDriverWait(self.selenium, self.timeout).until(
                lambda s: not self.is_element_visible(*self._modal_locator))
