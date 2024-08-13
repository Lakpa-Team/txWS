#!/usr/bin/env python
# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.  You may obtain a copy
# of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations under
# the License.

from setuptools import setup, find_packages

with open('version.txt', 'r') as f:
    version = f.read().strip()

setup(
    name="txWS",
    py_modules=["txws"],
    setup_requires=["vcversioner", "six"],
    version=version,
    author="Lakpa Team",
    author_email="admin-tec@lakpa.cl",
    description="Twisted WebSockets wrapper",
    long_description=open("README.rst").read(),
    license="MIT/X11",
    url="http://github.com/Lakpa-Team/txWS.git",
)
