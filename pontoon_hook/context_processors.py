# -*- coding: utf-8 -*-

from __future__ import absolute_import
from django.conf import settings


def pontoon_js_url(request):
    """
    Inserts a context variable PONTOON_JS_URL from settings
    """
    return {'PONTOON_JS_URL': getattr(settings, 'PONTOON_JS_URL', None) or
            "https://pontoon-dev.mozillalabs.com/en-US/static/"
            "js/project/pontoon.js"}
