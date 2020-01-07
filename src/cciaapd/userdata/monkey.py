# -*- coding: utf-8 -*-
from zope.schema.interfaces import InvalidValue


def convertTokensToValues(self, tokens):
    """Convert term tokens to the terms themselves.

    Tokens are used in the HTML form to represent terms. This method takes
    the form tokens and converts them back to terms.
    """
    values = []
    for token in tokens:
        try:
            term = self.vocabulary.getTermByToken(token.encode('utf-8'))
        except LookupError:
            raise InvalidValue("token %r not found in vocabulary" % token)
        else:
            values.append(term.value)
    return values
