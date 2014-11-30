==================
djangocms-markitup
==================

.. image:: https://pypip.in/v/djangocms-markitup/badge.png
        :target: https://pypi.python.org/pypi/djangocms-markitup
        :alt: Latest PyPI version
    
.. image:: https://travis-ci.org/nephila/djangocms-markitup.png?branch=master
        :target: https://travis-ci.org/nephila/djangocms-markitup
        :alt: Latest Travis CI build status

.. image:: https://pypip.in/d/djangocms-markitup/badge.png
        :target: https://pypi.python.org/pypi/djangocms-markitup
        :alt: Monthly downloads

.. image:: https://coveralls.io/repos/nephila/djangocms-markitup/badge.png?branch=master
        :target: https://coveralls.io/r/nephila/djangocms-markitup?branch=master
        :alt: Test coverage

A django CMS 3 plugin that implements a `django-markitup`_ field

**********
Quickstart
**********

Install djangocms-markitup::

    pip install djangocms-markitup

Then add it to INSTALLED_APPS along with its dependencies::

    'markitup',
    'djangocms_markitup',


Execute migration or syncdb::

    $ python manage.py syncdb

or::

    $ python manage.py migrate

*****
Usage
*****

A ``MarkItUp`` plugin will appear in the list of available plugins; see `django-markitup`_
for more details and detailed configuration

*************************
Plugin template processor
*************************

``djangocms-markitup`` provide a plugin template processor that parses the
plugin body and renders templatetags; to enable it, add the following
configuration::

    CMS_PLUGIN_PROCESSORS = (
        'djangocms_markitup.processors.process_templatetags',
    )

*************
Documentation
*************

For further documentation see http://djangocms-markitup.readthedocs.org/

.. _django-markitup: https://bitbucket.org/carljm/django-markitup