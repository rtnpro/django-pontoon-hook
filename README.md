django-pontoon-hook
===================
This hook enables a Django website to use [Pontoon][1] as a live localization tool.

[1]: https://github.com/mathjazz/pontoon

Installation
------------
`pip install -e git+git://github.com/rtnpro/django-pontoon-hook.git@master#egg=django_pontoon_hook`
 
Usage
-----
 1. Add 'pontoon_hook' to your `settings.INSTALLED_APPS`.
 1. Add 'pontoon_hook.middleware.PontoonMiddleware' to your `settings.MIDDLEWARE_CLASSES`
    preferably as the last item or as later as possible.
 1. Add `I18N_BACKEND_REAL = "pontoon_hook.i18n_backend.PontoonI18nRealBackend"` to your
    `settings.py`.

TODO
----
- Write unittests

License
-------
This software is licensed under the [New BSD License](http://creativecommons.org/licenses/BSD/). For more information, read the file `LICENSE`.
