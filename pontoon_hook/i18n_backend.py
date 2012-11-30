# -*- coding: utf-8 -*-

from __future__ import absolute_import
import re
from django.utils.translation import trans_real, I18nRealBackend

PONTOON_WRAPPER_TAG = '<!--l10n-->'
PONTOON_PSEUDO_WRAPPER_TAG = 'LT--pontoonl10n--GT'


def wrap_message(message):
    # regex to match format specifiers in a string
    p = re.compile(r'%(\([A-Za-z0-9_\-]+\)){0,1} *[diouxXeEfFgGcrs]')
    # We do not wrap strings with a pontoon tag if they
    # contain format specifiers
    if not p.search(message):
        message = PONTOON_PSEUDO_WRAPPER_TAG + message or ''
    return message


class PontoonI18nRealBackend(I18nRealBackend):
    """
    i18n backend to be used by Pontoon. This is wrapper
    around Django's I18nRealBackend to wrap translation
    texts as required by Pontoon.
    """
    def gettext_noop(self, message):
        return trans_real.gettext_noop(wrap_message(message))

    def gettext(self, message):
        return trans_real.gettext(wrap_message(message))

    def ugettext(self, message):
        return trans_real.ugettext(wrap_message(message))

    def pgettext(self, context, message):
        return trans_real.pgettext(context, wrap_message(message))
