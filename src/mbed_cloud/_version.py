# ---------------------------------------------------------------------------
# Mbed Cloud Python SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------

"""Version number is composed based on API backend version and SDK version.

Breaking changes in SDK will increment major version number.
API version number will follow Mbed release schedule (~quarterly releases).

See https://www.python.org/dev/peps/pep-0440/ for reference

Validate with:
python -c "from mbed_cloud import __version__; print(__version__)"
"""

# Generated by build system
COMMIT = ''  # auto
COMMIT_COUNT = ''  # auto

# Manually configured
API_MAJOR = '1'
API_MINOR = '2'
API_VERSION = '.'.join((API_MAJOR, API_MINOR))

SDK_MAJOR = '6'
SDK_MINOR = ''
LOCAL = None
BETA = False
DEV = not COMMIT

if BETA:
    SDK_MAJOR += 'b%s' % COMMIT_COUNT
else:
    SDK_MINOR += COMMIT_COUNT

if DEV:
    SDK_MINOR = 'dev%s' % SDK_MINOR

__version__ = '.'.join(part for part in (
    API_MAJOR,
    API_MINOR,
    SDK_MAJOR,
    SDK_MINOR,
) if part)

if LOCAL:
    __version__ = '%s+%s' % (__version__, LOCAL)

__version__ = __version__.lower()
