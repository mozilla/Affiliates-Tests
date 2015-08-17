# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from pages.page import Page


class Base(Page):

    _page_title_locator = (By.CSS_SELECTOR, 'h1.page-title')
    _page_header_locator = (By.CSS_SELECTOR, '.contain > h1')

    _login_browser_id_locator = (By.CSS_SELECTOR, 'a.persona-button')
    _logout_locator = (By.CSS_SELECTOR, '#nav-user-submenu li a.browserid-logout')
    _profile_locator = (By.CSS_SELECTOR, '#nav-user-submenu li:nth-of-type(2) a')
    _username_locator = (By.CSS_SELECTOR, '#nav-main-menu > li.user > a')
    _error_locator = (By.CLASS_NAME, 'error')

    _about_content_nav_locator = (By.CSS_SELECTOR, '#nav-main-menu li:nth-of-type(1) a')

    @property
    def page_title(self):
        return self.selenium.find_element(*self._page_title_locator).text

    def _hover_user_menu(self):
        username = self.selenium.find_element(*self._username_locator)
        ActionChains(self.selenium).move_to_element(username).perform()

    @property
    def is_user_logged_in(self):
        return self.is_element_present(*self._logout_locator)

    @property
    def username(self):
        return self.selenium.find_element(*self._username_locator).text

    def login(self, email, password, error=False):
        self.click_login()
        from browserid import BrowserID
        pop_up = BrowserID(self.selenium, self.timeout)
        pop_up.sign_in(email, password)
        if error:
            element = self.selenium.find_element(*self._error_locator)
            WebDriverWait(self.selenium, self.timeout).until(
                lambda s: element.is_displayed())
        else:
            WebDriverWait(self.selenium, self.timeout).until(
                lambda s: self.is_user_logged_in)
            from pages.home import Home
            return Home(self.testsetup)

    def click_login(self):
        self.selenium.find_element(*self._login_browser_id_locator).click()

    @property
    def header(self):
        return self.selenium.find_element(*self._page_header_locator).text.replace('\n', ' ')

    def logout(self):
        self._hover_user_menu()
        self.selenium.find_element(*self._logout_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: not self.is_user_logged_in)

        from pages.start_page import StartPage
        return StartPage(self.testsetup)

    def click_profile(self):
        self._hover_user_menu()
        self.selenium.find_element(*self._profile_locator).click()
        from pages.user import EditProfile
        return EditProfile(self.testsetup)

    def click_about_nav_button(self):
        self.selenium.find_element(*self._about_content_nav_locator).click()
        from pages.about import About
        return About(self.testsetup)

    @property
    def error(self):
        return self.selenium.find_element(*self._error_locator).text
