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

        _display_name_label_locator = (By.CSS_SELECTOR, '#modal label[for="id_display_name"]')
        _display_name_locator = (By.CSS_SELECTOR, '#modal input#id_display_name')
        _save_locator = (By.CSS_SELECTOR, '.button.go')
        _cancel_locator = (By.CSS_SELECTOR, '.button.close')

        def __init__(self, testsetup):
            Page.__init__(self, testsetup)
            WebDriverWait(self.selenium, self.timeout).until(
                lambda s: self.is_element_visible(*self._modal_locator))
            self._root_element = self.selenium.find_element(*self._modal_locator)

        @property
        def display_name_label(self):
            return self._root_element.find_element(*self._display_name_label_locator).text

        @property
        def display_name(self):
            return self._root_element.find_element(*self._display_name_locator).get_attribute('value')

        def set_display_name(self, name):
            input_field = self._root_element.find_element(*self._display_name_locator)
            input_field.clear()
            input_field.send_keys(name)

        def click_save_my_changes(self):
            self._root_element.find_element(*self._save_locator).click()
            WebDriverWait(self.selenium, self.timeout).until(
                lambda s: not self.is_element_visible(*self._modal_locator))

        def click_cancel(self):
            self._root_element.find_element(*self._cancel_locator).click()
            WebDriverWait(self.selenium, self.timeout).until(
                lambda s: not self.is_element_visible(*self._modal_locator))
