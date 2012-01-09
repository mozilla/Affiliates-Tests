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
#                 Sergey Tupchiy (tupchii.sergii@gmail.com)
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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class StartPage(Page):

    _page_title = 'Firefox Affiliates'

    _page_header_locator = (By.CSS_SELECTOR, '#content h2')
    _learn_more_link_locator = (By.CSS_SELECTOR, '#content .show_tooltip')
    _learn_more_tooltip_locator = (By.ID, 'tooltip_home')
    _mozilla_logo_link_locator = (By.CSS_SELECTOR, '#header a')
    _footer_locator = (By.CSS_SELECTOR, '#footer')
    _twitter_button_locator = (By.CSS_SELECTOR, '.button.share_twitter')
    _facebook_button_locator = (By.CSS_SELECTOR, '.button.share_facebook')

    #Not LoggedIn
    _login_browser_id_locator = (By.CSS_SELECTOR, '.browserid-button:nth-of-type(1) a')
    _register_locator = (By.CSS_SELECTOR, '.browserid-button:nth-of-type(2) a')

    def __init__(self, testsetup, open_url=True):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        Page.__init__(self, testsetup)
        if open_url:
            self.selenium.get(self.base_url)

    def login(self):
        login = self.click_login_browser_id()
        login.login_user_browser_id('default')
        from pages.home import Home
        return Home(self.testsetup)

    def click_login_browser_id(self):
        self.selenium.find_element(*self._login_browser_id_locator).click()
        from pages.user import Login
        return Login(self.testsetup)

    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text.replace('\n', ' ')

    @property
    def is_twitter_button_present(self):
        return self.is_element_present(*self._twitter_button_locator)

    @property
    def is_facebook_button_present(self):
        return self.is_element_present(*self._facebook_button_locator)

    @property
    def is_mozilla_logo_visible(self):
        return self.is_element_visible(*self._mozilla_logo_link_locator)

    def click_mozilla_logo(self):
        self.selenium.find_element(*self._mozilla_logo_link_locator).click()

    def hover_over_learn_more_link(self):
        learn_more = self.selenium.find_element(*self._learn_more_link_locator)
        ActionChains(self.selenium).move_to_element(learn_more).perform()

    @property
    def is_learn_more_tooltip_visible(self):
        return self.is_element_visible(*self._learn_more_tooltip_locator)
