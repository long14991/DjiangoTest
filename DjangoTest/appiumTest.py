__author__ = 'QDHL'


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from zipfile import ZipFile
import json
import os
import random
from time import sleep
#from dateutil.parser import parse

from selenium.common.exceptions import NoSuchElementException

from appium import webdriver
import desired_capabilities
import xmlConfig


# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1


class AppiumTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

        # remove zipped file from `test_pull_folder`
        if hasattr(self, 'zipfilename') and os.path.isfile(self.zipfilename):
            os.remove(self.zipfilename)


    def test_current_activity(self):
        self.driver.start_activity(xmlConfig.getPackageName(),xmlConfig.getActivityName(),app_wait_package='',app_wait_activity='')
        self.driver.close_app()

def startTest():
	suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
	unittest.TextTestRunner(verbosity=2).run(suite)
