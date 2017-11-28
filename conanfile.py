#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class CeleroConan(ConanFile):
    name = "celero"
    version = "2.1.0"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/bincrafters/conan-celero"
    license = "Apache 2.0 License"
    author = "Gareth A. Lloyd"

    def source(self):
        self.run("git clone --depth 1  -- https://github.com/DigitalInBlue/Celero.git celero")

    def build(self):
        cmake = CMake(self)
        self.run('cmake -DCMAKE_INSTALL_PREFIX=install -DCELERO_COMPILE_DYNAMIC_LIBRARIES=OFF -DCELERO_ENABLE_EXPERIMENTS=OFF %s/celero %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . --target install %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="install/include")
        self.copy("*.a", dst="lib", src="install/lib")

    def package_info(self):
        self.cpp_info.libs = ["celero"]
