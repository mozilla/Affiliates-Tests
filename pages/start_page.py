# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.base import Base


class StartPage(Base):

    _page_title = 'Firefox Affiliates'

    def __init__(self, testsetup, open_url=True):
        Base.__init__(self, testsetup)
        if open_url:
            self.open('/')
