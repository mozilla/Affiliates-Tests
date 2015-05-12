Affiliates Tests
====================

Thank you for checking out Mozilla's Affiliates-Tests test suite. Mozilla and the Web QA team are grateful for the help and hard work of many contributors like yourself. The following contributors have submitted pull requests to Affiliates-Tests:

https://github.com/mozilla/Affiliates-Tests/contributors

Continuous Integration
----------------------

[![Build Status](https://secure.travis-ci.org/mozilla/Affiliates-Tests.png?branch=master)](http://travis-ci.org/mozilla/Affiliates-Tests/)

Getting involved as a contributor
---------------------------------

We love working with contributors to fill out the Selenium test coverage for Affiliates-Tests, but it does require a few skills. You will need to know some Python, some Selenium and a basic familiarity with GitHub.

If you know some Python, it's worth having a look at the Selenium framework to understand the basic concepts of browser based testing and especially page objects. Our suite uses [Selenium WebDriver][Selenium WebDriver].

If you need to brush-up on programming, but are eager to start contributing immediately, please consider helping us find bugs in Mozilla [Firefox][Firefox] or find bugs in the Mozilla websites tested by the [WebQA][WebQA] team. To brush up on Python skills before engaging with us, [Dive Into Python][Dive Into Python] is an excellent resource. MIT also has [lecture notes on Python][Lecture notes on Python] available through their OpenCourseWare. The programming concepts you will need to know include functions, working with classes, and some object-oriented programming basics.

[Selenium WebDriver]: http://docs.seleniumhq.org/docs/03_webdriver.jsp
[Firefox]: https://quality.mozilla.org/teams/desktop-firefox/
[WebQA]: https://quality.mozilla.org/teams/web-qa/
[Dive Into Python]: http://www.diveintopython.net/toc/index.html
[Lecture notes on Python]: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/

Questions are always welcome
----------------------------

While we take pains to keep our documentation updated, the best source of information is those of us who work on the project. Don't be afraid to join us in irc.mozilla.org [#mozwebqa][mozwebqa] to ask questions about our Selenium tests. Mozilla also hosts the [#affiliates][affiliates] chat room to answer your general questions about contributing to Mozilla.

[mozwebqa]: http://client01.chat.mibbit.com/?server=irc.mozilla.org&channel=#mozwebqa
[affiliates]: http://client01.chat.mibbit.com/?server=irc.mozilla.org&channel=#affiliates

Getting set up
--------------

It's easy to get set up: just some pieces of software to install and in you'll be running the tests! 

### Install Git

If you don't have Git on your computer, download and install [it][Git]. I you already have Git, you can skip this step.

[Git]:http://git-scm.com/downloads

### Install Python

If you don't already have it installed, please install [Python 2.6+][Python], because you will need it for running tests.

[Python]: https://www.python.org/download/releases/2.6.6/

### Cloning the test repository with Git

After you have installed [Git][Git] you will need to clone the project to your hard drive. From your workspace directory run this command which will copy (clone) the project to your hard drive


    git clone --recursive git://github.com/mozilla/Affiliates-Tests.git


[Git]: http://git-scm.com/downloads

### Installing Python packages

You will need to install Selenium, py.test, unittestzero and some other project specific packages. Fortunately ```pip``` makes it easy to install all of these in one step. Let's start by installing pip:


    sudo easy_install pip


Now using pip we'll install the packages we need (which are listed in requirements.txt)

    pip install -Ur requirements.txt

If you are running on Ubuntu/Debian you will need to do following first:

    sudo apt-get install python-setuptools

to install the required Python libraries.


### Running tests locally

To run tests locally it's a simple case of calling ```py.test``` from the Affiliates-Tests directory.

For more command-line options see the [pytest-mozwebqa documentation](https://github.com/mozilla/pytest-mozwebqa)

### Virtual Environments (Optional/Intermediate level)

The step above installs the packages globally on your operating system. Using ```virtualenv``` you can sandbox Python packages into virtual environments for each Mozilla project you work on. Follow our [Virtual Env guide][Virtual Environment] to get a virtual environment up and running. We recommend this practice.

[Virtual Environment]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Automation/Virtual_Environments


Writing tests
-------------

If you want to get involved and add more tests, then there's just a few things we'd like to ask you to do:

1. Use the [template files][Template files] for all new tests and page objects
2. Follow our simple [style guide][Style guide]
3. Fork this project with your own GitHub account
4. Add your test into the "tests" folder and the necessary methods for it into the appropriate file in "pages"
5. Make sure all tests are passing and submit a pull request with your changes

[Template files]: https://github.com/mozilla/mozwebqa-test-templates
[Style guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide

License
-------

This software is licensed under the [MPL][MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
    If a copy of the MPL was not distributed with this file, You can obtain one at
    http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/

