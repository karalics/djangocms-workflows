#!/usr/bin/env python
import os
import uuid
from setuptools import find_packages, setup

from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = [str(ir.req) for ir in parse_requirements('requirements.txt', session=uuid.uuid1())]

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='djangocms-workflows',
    version='0.2a1',
    description='Workflow system for Django-CMS.',
    long_description=README,
    license=read('LICENSE'),
    author='karalics',
    author_email='slavisa.karalic@gmail.com',
    url='https://github.com/karalics/djangocms-workflows.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    keywords=['django', 'Django CMS', 'workflow', 'bootstrap', 'website', 'CMS'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
