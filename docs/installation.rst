============
Installation
============

#. Install djangocms-markitup::

        $ pip install djangocms-markitup

   or from the repository::

        pip install -e https://github.com/nephila/djangocms-markitup#egg=djangocms-markitup

#. Then add it to INSTALLED_APPS along with its dependencies::

        'markitup',
        'djangocms_markitup',

#. Synchronize the database with syncdb::

        $ python manage.py syncdb

   or migrate::

        $ python manage.py migrate

#. That's all!

************
Dependencies
************

* `django-markitup`_ >= 2.2.2
* `markdown2`_  >= 2.3

.. _django-markitup: https://bitbucket.org/carljm/django-markitup
.. _markdown2: https://github.com/trentm/python-markdown2