#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

from selenium.webdriver.common.by import By

from page import Page


class Home(Page):

    _page_title = 'Firefox Affiliates - Mozilla Firefox'
    _page_url = '/new'

    #LoggedIn
    _logout_locator = (By.CSS_SELECTOR, '#sidebar-nav li:nth-of-type(1) a')
    _edit_profile_locator = (By.CSS_SELECTOR, '#sidebar-nav li:nth-of-type(2) a')
    _username_locator = (By.CSS_SELECTOR, '#user-info h5')

    #Content Navigation
    _page_header_locator = (By.CSS_SELECTOR, '#content h2')
    _banners_content_nav_locator = (By.CSS_SELECTOR, '#content-nav li:nth-of-type(1) a')
    _faq_content_nav_locator = (By.CSS_SELECTOR, '#content-nav li:nth-of-type(2) a')
    _about_content_nav_locator = (By.CSS_SELECTOR, '#content-nav li:nth-of-type(3) a')
    _banner_categories_locator = (By.CSS_SELECTOR, '#step-content li')
    _banner_code_locator = (By.ID, 'badge_code')
    _banner_preview_locator = (By.CSS_SELECTOR, '#banner_preview')
    _step_buttons_locator = (By.CSS_SELECTOR, '.steps-buttons')
    _size_selector_locator = (By.ID, 'size')
    _color_selector_locator = (By.ID, 'color')
    _language_selector_locator = (By.ID, 'language')

    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text

    @property
    def is_user_logged_in(self):
        return self.is_element_visible(*self._logout_locator)

    @property
    def username(self):
        return self.selenium.find_element(*self._username_locator).text

    def click_logout(self):
        self.selenium.find_element(*self._logout_locator).click()

    def click_edit_profile(self):
        self.selenium.find_element(*self._edit_profile_locator).click()
        from pages.user import EditProfile
        return EditProfile(self.testsetup)

    def click_faq_nav_button(self):
        self.selenium.find_element(*self._faq_content_nav_locator).click()
        return self.FaqNavMenu(self.testsetup)

    def click_about_nav_button(self):
        self.selenium.find_element(*self._about_content_nav_locator).click()
        return self.AboutNavMenu(self.testsetup)

    def click_banners_nav_button(self):
        self.selenium.find_element(*self._banners_content_nav_locator).click()
        return self.MyBannersNavMenu(self.testsetup)

    @property
    def category_count(self):
        return len(self.selenium.find_elements(*self._banner_categories_locator))

    @property
    def categories(self):
        return [self.Categories(self.testsetup, element)
                for element in self.selenium.find_elements(*self._banner_categories_locator)]

    def select_size(self, value):
        option_locator = (By.CSS_SELECTOR, 'option[value^=\'%s\']' % value)
        self.selenium.find_element(*self._size_selector_locator).click()
        self.selenium.find_element(*option_locator).click()

    @property
    def banner_html_code(self):
        return self.selenium.find_element(*self._banner_code_locator).get_attribute('value')

    @property
    def banner_url(self):
        return self._get_banner_attribute_from_code(self.banner_html_code, 'href')

    @property
    def banner_img_src(self):
        return self._get_banner_attribute_from_code(self.banner_html_code, 'src')

    def _get_banner_attribute_from_code(self, code, key):
        return re.search('%s="(.*?)"' % key, code).group(1)

    @property
    def banner_preview_url(self):
        _link = (By.CSS_SELECTOR, 'a')
        return self.selenium.find_element(*self._banner_preview_locator).find_element(*_link).get_attribute('href')

    @property
    def banner_preview_img_src(self):
        _img = (By.TAG_NAME, 'img')
        return self.selenium.find_element(*self._banner_preview_locator).\
                                            find_element(*_img).get_attribute('src').replace(self.base_url, '')

    def is_step_button_selected(self, button_no):
        return self.is_element_present(By.CSS_SELECTOR,
                                       '%s .%s.selected' % (self._step_buttons_locator[1], button_no))

    class FaqNavMenu(Page):

        _page_url = '/faq'
        _question_link_locator = (By.CSS_SELECTOR, '.faq_content h5')

        @property
        def questions_count(self):
            return len(self.selenium.find_elements(*self._question_link_locator))

        @property
        def questions_text(self):
            return self.selenium.find_element(*self._question_link_locator).text

        def answer(self, lookup):
            return self.selenium.find_element(By.CSS_SELECTOR,
                                              '.faq_content ul:nth-of-type(%s) .answer' % lookup).text

        def expand_question_by_section(self, link_no):
            self.selenium.find_element(By.CSS_SELECTOR,
                                       '.faq_content ul:nth-of-type(%s) li:nth-of-type(1)' % link_no).click()

    class AboutNavMenu(Page):

        _page_url = '/about'
        _about_text_locator = (By.CSS_SELECTOR, '.about_content')

        @property
        def about_text(self):
            return self.selenium.find_element(*self._about_text_locator).text

    class MyBannersNavMenu(Page):

        _page_header = 'These are the banners you\'ve created so far:'

    class Categories(Page):

        _name_locator = (By.CSS_SELECTOR, 'p')

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            return self._root_element.find_element(*self._name_locator).text

        def select_category(self):
            self._root_element.find_element(*self._name_locator).click()
