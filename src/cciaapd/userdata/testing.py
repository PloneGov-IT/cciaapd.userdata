# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import cciaapd.userdata


class CciaapdUserdataLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=cciaapd.userdata)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cciaapd.userdata:default')


CCIAAPD_USERDATA_FIXTURE = CciaapdUserdataLayer()


CCIAAPD_USERDATA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CCIAAPD_USERDATA_FIXTURE,),
    name='CciaapdUserdataLayer:IntegrationTesting',
)


CCIAAPD_USERDATA_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CCIAAPD_USERDATA_FIXTURE,),
    name='CciaapdUserdataLayer:FunctionalTesting',
)


CCIAAPD_USERDATA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CCIAAPD_USERDATA_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CciaapdUserdataLayer:AcceptanceTesting',
)
