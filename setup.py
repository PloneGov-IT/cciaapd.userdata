# -*- coding: utf-8 -*-
"""Installer for the cciaapd.userdata package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join(
    [
        open('README.rst').read(),
        open('CONTRIBUTORS.rst').read(),
        open('CHANGES.rst').read(),
    ]
)


setup(
    name='cciaapd.userdata',
    version='1.0.1.dev0',
    description="Additional userdata for cciaapd",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='RedTurtle Technology',
    author_email='sviluppoplone@redturtle.it',
    url='https://github.com/collective/cciaapd.userdata',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/cciaapd.userdata',
        'Source': 'https://github.com/collective/cciaapd.userdata',
        'Tracker': 'https://github.com/collective/cciaapd.userdata/issues',
        # 'Documentation': 'https://cciaapd.userdata.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['cciaapd'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=['setuptools', 'collective.monkeypatcher'],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.robotframework[debug]',
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = cciaapd.userdata.locales.update:update_locale
    """,
)
