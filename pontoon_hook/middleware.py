# -*- coding: utf-8 -*-

class PontoonMiddleware(object):   
    """
    Middleware to make a Django project ready to use Pontoon.

    Preferrably, this middleware should be the last item
    in the list of middlewares for a Django project.
    """

    def process_response(self, request, response):
        """
        Replace PONTOON_PSEUDO_WRAPPER_TAG with PONTOON_WRAPPER_TAG
        in rendered response.
        """
        from pontoon_hook.i18n_backend import (PONTOON_WRAPPER_TAG,
            PONTOON_PSEUDO_WRAPPER_TAG)
        response.content = response.content.replace(
            PONTOON_PSEUDO_WRAPPER_TAG, 
            PONTOON_WRAPPER_TAG
        )
        return response
