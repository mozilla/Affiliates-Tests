# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class About(Base):

    _page_title = 'About | Firefox Affiliates'
    _page_url = '/about'
    _about_text_locator = (By.CSS_SELECTOR, '.section.page-head p.prose')

    _category_locator = (By.CSS_SELECTOR, 'article#faq div.contain h3')
    _question_locator = (By.CSS_SELECTOR, '#faq .faq > dt')
    _answer_locator = (By.CSS_SELECTOR, 'dd p:nth-of-type(1)')

    _page_header_locator = (By.CSS_SELECTOR, 'h1.page-title')
    _faq_header_locator = (By.CSS_SELECTOR, '#faq .section-title')

    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text

    @property
    def about_text(self):
        return self.selenium.find_element(*self._about_text_locator).text

    @property
    def faq_header(self):
        return self.selenium.find_element(*self._faq_header_locator).text

    @property
    def category_count(self):
        return len(self.selenium.find_elements(*self._category_locator))

    @property
    def questions_count(self):
        return len(self.selenium.find_elements(*self._question_locator))

    def questions_text(self, lookup):
        return self.selenium.find_elements(*self. _question_locator)[lookup].text

    @property
    def answers_count(self):
        return len(self.selenium.find_elements(*self._answer_locator))

    def answer(self, lookup):
        return self.selenium.find_elements(*self._answer_locator)[lookup].text
