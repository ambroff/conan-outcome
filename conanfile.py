#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class OutcomeConan(ConanFile):
    name = "outcome"
    version = "2.0"
    url = "https://github.com/ambroff/conan-outcome"
    description = "A set of tools for reporting and handling function failures in contexts where using C++ exception handling is unsuitable"

    exports_sources = "include/*"
    no_copy_source = True

    # Indicates License type of the packaged library
    license = "Apache-2.0"

    def source(self):
        archive_url = 'https://github.com/ned14/outcome/releases/download/v2.0-boost-peer-review/outcome-v2.0-source-201801180951.tar.xz'
        checksum = '710497dbb445e066fbe94fee671c8e7c25fdbd201b76ae07a0b81daa85082668'
        tools.get(archive_url, sha256=checksum)

    def package(self):
        self.copy(pattern="License.txt", dst="license")
        self.copy('*.h', src=os.path.join('outcome', 'include'), dst='include')
        self.copy('*.hpp', src=os.path.join('outcome', 'include'), dst='include')
    
    def package_id(self):
        self.info.header_only()
