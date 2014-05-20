#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.base import Base


class About(Base):

    _page_url = '/about'
    _about_text_locator = (By.CSS_SELECTOR, '.section.page-head p.prose')

    _question_locator = (By.CSS_SELECTOR, '#faq .faq > dt')
    _answer_locator = (By.CSS_SELECTOR, '#faq .faq > dd')

    _faq_header_locator = (By.CSS_SELECTOR, '#faq .section-title')

    @property
    def about_text(self):
        return self.selenium.find_element(*self._about_text_locator).text

    @property
    def faq_header(self):
        return self.selenium.find_element(*self._faq_header_locator).text

    @property
    def questions_count(self):
        return len(self.selenium.find_elements(*self._question_locator))

    def questions_text(self, lookup):
        return self.selenium.find_elements(*self._question_locator)[lookup].text

    def answer(self, lookup):
        return self.selenium.find_elements(*self._answer_locator)[lookup].text
