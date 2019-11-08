# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from cciaapd.userdata.testing import CCIAAPD_USERDATA_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that cciaapd.userdata is properly installed."""

    layer = CCIAAPD_USERDATA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if cciaapd.userdata is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'cciaapd.userdata'))

    def test_browserlayer(self):
        """Test that ICciaapdUserdataLayer is registered."""
        from cciaapd.userdata.interfaces import (
            ICciaapdUserdataLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICciaapdUserdataLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CCIAAPD_USERDATA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['cciaapd.userdata'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if cciaapd.userdata is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'cciaapd.userdata'))

    def test_browserlayer_removed(self):
        """Test that ICciaapdUserdataLayer is removed."""
        from cciaapd.userdata.interfaces import \
            ICciaapdUserdataLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICciaapdUserdataLayer,
            utils.registered_layers())
