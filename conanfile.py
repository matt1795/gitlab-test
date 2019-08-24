from conans import ConanFile, CMake, tools


class GitlabtestConan(ConanFile):
    name = "gitlab-test"
    version = "0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Gitlabtest here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_folder)
        cmake.build()

    def package(self):
        self.copy("*.h", "include", "include")
        self.copy("*.a", "lib", "lib")
        self.copy("*.so", "lib", "lib")

    def package_info(self):
        self.cpp_info.libs = ["test"]
