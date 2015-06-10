# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import urllib2

import pytest


@pytest.fixture(scope='session')
def capabilities(capabilities):
    capabilities.setdefault('tags', []).append('affiliates')
    return capabilities


@pytest.fixture
def existing_user(variables):
    return variables['users']['default']


@pytest.fixture
def new_user(variables):
    response = urllib2.urlopen('http://personatestuser.org/email/').read()
    user = json.loads(response)
    return {'email': user['email'],
            'password': user['pass']}


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium
