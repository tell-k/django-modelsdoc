# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class DjangoTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import os
        import sys
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

        test_dir = os.path.dirname(__file__)
        sys.path.insert(0, test_dir)

        import django
        from django.test.utils import get_runner
        from django.conf import settings

        if django.VERSION >= (1, 7):
            django.setup()

        runner = get_runner(settings)(verbosity=1,
                                      interactive=False, failfast=False)
        errno = runner.run_tests(['tests'])
        sys.exit(errno)

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fp:
    readme = fp.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'Django',
    'Sphinx'
]

tests_require = [
    'mock',
    'testfixtures',
    'six',
]

classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Framework :: Django',
    'Framework :: Django :: 1.5',
    'Framework :: Django :: 1.6',
    'Framework :: Django :: 1.7',
    'Framework :: Django :: 1.8',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    name='django-modelsdoc',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT',
    description='A simple Django app to conduct Web-based polls.',
    long_description=readme,
    url='http://www.example.com/',
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': DjangoTest},
    author='telll-k',
    author_email='ffk2005@gmail.com',
    classifiers=classifiers,
)
