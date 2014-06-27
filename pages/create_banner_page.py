#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base import Base


class CreateBanner(Base):
    _category_locator = (By.CSS_SELECTOR, '.categories-list > li:nth-child(1) > a')
    _banner_locator = (By.CSS_SELECTOR, '.banners-list > li:nth-child(1) > a')
    _select_language_locator = (By.CSS_SELECTOR, '.config-option.option-language > select')
    _select_size_locator = (By.CSS_SELECTOR, '.config-option.option-size > select')
    _select_color_locator = (By.CSS_SELECTOR, '.config-option.option-color > select')
    _save_banner_button_locator = (By.CSS_SELECTOR, '.button.go')
    _dashboard_button_locator = (By.CSS_SELECTOR, '.button.go[href*="dashboard"]')
    _embed_code_locator = (By.ID, 'embed-code')
    _banner_href_locator = (By.CSS_SELECTOR, '.banner-preview a')

    def choose_category(self):
        self.selenium.find_element(*self._category_locator).click()

    def choose_banner(self):
        self.selenium.find_element(*self._banner_locator).click()

    def select_language(self, option_value):
        element = self.selenium.find_element(*self._select_language_locator)
        select = Select(element)
        select.select_by_value(option_value)

    def select_size(self):
        element = self.selenium.find_element(*self._select_size_locator)
        select = Select(element)
        select.select_by_index(1)

    def select_color(self):
        element = self.selenium.find_element(*self._select_color_locator)
        select = Select(element)
        select.select_by_index(1)

    def click_save(self):
        self.selenium.find_element(*self._save_banner_button_locator).click()

    def go_to_dashboard_page(self):
        self.selenium.find_element(*self._dashboard_button_locator).click()

    @property
    def is_embeded_code_generated(self):
        return self.is_element_visible(*self._embed_code_locator)

    @property
    def banner_url(self):
        return self.selenium.current_url
