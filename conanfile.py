import os

from conans import ConanFile, tools


class NinjaConan(ConanFile):
    name = "ninja"
    version = tools.get_env("GIT_TAG", "1.9.0")
    license = "Apache"
    description = "Small build system with a focus on speed"
    settings = "os", "compiler", "build_type", "arch"

    def build_requirements(self):
        self.build_requires("generators/1.0.0@camposs/stable")
        self.build_requires("python/[>=3.8.2]@camposs/stable")

    def source(self):
        tools.get("https://github.com/ninja-build/ninja/archive/v%s.tar.gz" % self.version)

    def build(self):
        with tools.chdir("%s-%s" % (self.name, self.version)):
            self.run("python3 configure.py --bootstrap")

    def package(self):
        self.copy(
            os.path.join("%s-%s" % (self.name, self.version), "ninja"),
            "bin",
            keep_path=False,
        )
