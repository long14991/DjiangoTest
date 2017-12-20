#!/usr/bin/env python

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

import os
import xmlConfig


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def get_desired_capabilities():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': 'LE67A06250157651',
        'newCommandTimeout': 240,
		'appPackage':'',
		'appActivity':''
    }
	#'app': PATH('../../apps/' + app),
    desired_caps['appPackage']=xmlConfig.getPackageName()
    desired_caps['appActivity']=xmlConfig.getActivityName()
    return desired_caps
