#!/usr/bin/env python

"""my-new-package setup script."""

from setuptools import find_packages, setup

# https://github.com/PyCQA/pylint/issues/3826
with open("README.rst", encoding="utf8") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst", encoding="utf8") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0"]
test_requirements = ["pytest>=6.0"]

__version__ = '0.1.0'

setup(
    author="Mark Sevelj",
    author_email='mark@example.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="An example package for cookiecutter-py3-package.",
    entry_points={
        'console_scripts': [
            'my_new_package=my_new_package.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='my_new_package',
    name='my_new_package',
    packages=find_packages(include=['my_new_package', 'my_new_package.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/imAsparky/my-new-package',
    version=__version__,
    zip_safe=False,
)
