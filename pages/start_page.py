# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base


class StartPage(Base):

    _page_title = 'Firefox Affiliates'
    _close_modal_locator = (By.CSS_SELECTOR, '#modal button.close')

    def __init__(self, testsetup, open_url=True):
        """ Creates a new instance of the class and gets the page ready for testing """
        Base.__init__(self, testsetup)
        if open_url:
            self.open('/')
            self.selenium.find_element(*self._close_modal_locator).click()
            WebDriverWait(self.selenium, testsetup.timeout).until(
                expected.invisibility_of_element_located(self._close_modal_locator))
