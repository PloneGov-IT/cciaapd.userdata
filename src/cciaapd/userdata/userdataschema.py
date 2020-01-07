# -*- coding: utf-8 -*-
from cciaapd.userdata.vocabularies import COMUNI_VOCAB
from cciaapd.userdata.vocabularies import ECONOMIC_SECTORS
from cciaapd.userdata.vocabularies import USER_TYPES
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider
from zope import schema
from zope.interface import implements


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    user_type = schema.Choice(
        title=u"Tipologia di utente",
        missing_value=u"",
        required=False,
        vocabulary=USER_TYPES,
    )

    economic_sector = schema.Choice(
        title=u"Settore economico di attività",
        description=u'Da compilare solo nel caso che l\'utente sia un cittadino.',  # noqa
        missing_value=u"",
        required=False,
        vocabulary=ECONOMIC_SECTORS,
    )

    economic_sector_other = schema.TextLine(
        title=u"Altro settore economico",
        description=u'Da compilare solo nel caso che si sia selezionato "Altro" precedentemente.',  # noqa
        missing_value=u"",
        required=False,
    )

    area_activity = schema.Choice(
        title=u"Zona di attività",
        description=u'Indica il comune di attività.',
        missing_value=u"",
        required=False,
        vocabulary=COMUNI_VOCAB,
    )
