import os

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class NoseTestCommand(TestCommand):
    # Inspired by the example at https://pytest.org/latest/goodpractises.html

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests'])

TESTS_REQUIRE = [
    'coverage',
    'nose',
]


setup(
    name="xamcheck.utils",
    version="0.0.1",
    author="Pankaj Singh",
    author_email="pankaj@policyinnovations.in",
    description=("Utility functions used in python projects of Xamcheck."),
    license = "BSD",
    keywords = "xamcheck utility",
    url = "http://packages.python.org/pypi/xamcheck.utils",
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['xamcheck'],
    extras_require=dict(
        test=TESTS_REQUIRE,
    ),
    install_requires=[
        'Django',
        'setuptools',
    ],
    cmdclass={'test': NoseTestCommand},
    tests_require=TESTS_REQUIRE,
    test_suite = "nose.collector",
    include_package_data=True,
    zip_safe=False,
)
