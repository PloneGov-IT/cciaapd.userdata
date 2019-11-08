# -*- coding: utf-8 -*-
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider
from zope import schema
from zope.interface import implements
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


USER_TYPES = SimpleVocabulary(
    [
        SimpleTerm(
            value=u'impresa_individuale',
            token=u'impresa_individuale',
            title=u'Impresa individuale',
        ),
        SimpleTerm(
            value=u'societa_di_persone',
            token=u'societa_di_persone',
            title=u'Società di persone (SNC, SAS,SS)',
        ),
        SimpleTerm(
            value=u'societa_di_capitali',
            token=u'societa_di_capitali',
            title=u'Società di capitali (SPA, SRL, SAPA)',
        ),
        SimpleTerm(
            value=u'consorzio_cooperativa',
            token=u'consorzio_cooperativa',
            title=u'Consorzio, Cooperativa',
        ),
        SimpleTerm(
            value=u'professionista',
            token=u'professionista',
            title=u'Professionista',
        ),
        SimpleTerm(
            value=u'associazione_di_categoria',
            token=u'associazione_di_categoria',
            title=u'Associazione di categoria',
        ),
        SimpleTerm(value=u'cittadino', token=u'cittadino', title=u'Cittadino'),
    ]
)

ECONOMIC_SECTORS = SimpleVocabulary(
    [
        SimpleTerm(
            value=u'attivita_manifatturiere',
            token=u'attivita_manifatturiere',
            title=u'Attività manifatturiere',
        ),
        SimpleTerm(
            value=u'servizi',
            token=u'servizi',
            title=u'Servizi (trasporti, alloggio e ristorazione, editoria,'
            u' attività finanziarie e assicurative, attività immobiliari,'
            u' servizi vari alle imprese, istruzioni , sanità, attività'
            u' sportive e artistiche, altre attività di servizi)',
        ),
        SimpleTerm(
            value=u'agricoltura_pesca',
            token=u'agricoltura_pesca',
            title=u'Agricoltura e pesca',
        ),
        SimpleTerm(
            value=u'commercio',
            token=u'commercio',
            title=u'Commercio (dettaglio, ingrosso, intermediari)',
        ),
        SimpleTerm(value=u'altro', token=u'altro', title=u'Altro'),
    ]
)


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

    area_activity = schema.TextLine(
        title=u"Zona di attività",
        description=u'Indica il comune di attività.',
        missing_value=u"",
        required=False,
    )
