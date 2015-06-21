Create models definitions document from your django project. This project help the documentation related to Django models.

|travis| |coveralls| |downloads| |version| |license| |requires|

Quick start
=============

1. Add "modelsdoc" to your INSTALLED_APPS setting like this

::

  INSTALLED_APPS = (
      ...
      'modelsdoc',
  )

2. Run **python manage.py listing_models** to listing model definition

* You can see `the results <https://github.com/tell-k/django-modelsdoc/blob/master/tests/sample_models.rst>`_ of executing the command to `tests/models.py <https://github.com/tell-k/django-modelsdoc/blob/master/tests/models.py>`_.

Option
=======

--app(-a)
-----------

You can pass specify app name. Listing only the specified app.

::

 $ python manage.py listing_models --app polls

--output(-o)
-------------

It writes the results to the specified file.

::

 $ python manage.py listing_models --output sample.rst

--format(-f)
-------------

You can choice output format. **rst** (reStructuredText) or **md** (Markdown). Default format is **rst**.

::

 $ python manage.py listing_models --format md

Customize Settings
===================

MODELSDOC_APPS
----------------

You can specify the apps and change the order.

::

 # output only models of poll
 MODELSDOC_APPS = (polls,)


MODELSDOC_DISPLAY_FIELDS
-------------------------

You can specify the field value and change the order.

::

 MODELSDOC_DISPLAY_FIELDS = (
     ('Fullname', 'verbose_name'),
     ('Name', 'name'),
     ('Type', 'db_type'),
     ('PK', 'primary_key'),
     ('Unique', 'unique'),
     ('Index', 'db_index'),
     ('Null/Blank', 'null_blank'),
     ('Comment', 'comment'),
 )

MODELSDOC_DISPLAY_FIELDS
-------------------------

# TODO more documented

::

 MODELSDOC_MODEL_OPTIONS = (
     'unique_together',
     'index_together',
     'ordering',
     'permissions',
     'get_latest_by',
     'order_with_respect_to',
     'db_tablespace',
     'abstract',
     'swappable',
     'select_on_save',
     'default_permissions',
     'default_related_name'
 )

Other settings
---------------

# TODO more documented

::

 MODELSDOC_OUTPUT_TEMPLATE = 'modelsdoc/models'
 MODELSDOC_OUTPUT_FORMAT = 'rst' # default format
 MODELSDOC_MODEL_WRAPPER = 'modelsdoc.wrappers.ModelWrapper'
 MODELSDOC_FIELD_WRAPPER = 'modelsdoc.wrappers.FieldWrapper'


Python and Django Support
=========================

.. csv-table::
   :widths: 10, 10, 10, 10, 10

   "　", "Django.1.5", "Django1.6", "Django1.7", "Django1.8"
   "Python 2.7","◯","◯","◯","◯"
   "PyPy","◯","◯","◯","◯"
   "Python 3.3","","","◯","◯"
   "Python 3.4","","","◯","◯"

License
=======

MIT Licence. See the LICENSE file for specific terms.

History
=======

0.1.0(Jun 21, 2015)
---------------------
* First release

.. |travis| image:: https://travis-ci.org/tell-k/django-modelsdoc.svg?branch=master
    :target: https://travis-ci.org/tell-k/django-modelsdoc

.. |coveralls| image:: https://coveralls.io/repos/tell-k/django-modelsdoc/badge.png
    :target: https://coveralls.io/r/tell-k/django-modelsdoc
    :alt: coveralls.io

.. |requires| image:: https://requires.io/github/tell-k/django-modelsdoc/requirements.svg?branch=master
    :target: https://requires.io/github/tell-k/django-modelsdoc/requirements/?branch=master
    :alt: requirements status

.. |downloads| image:: https://img.shields.io/pypi/dm/django-modelsdoc.svg
    :target: http://pypi.python.org/pypi/django-modelsdoc/
    :alt: downloads

.. |version| image:: https://img.shields.io/pypi/v/django-modelsdoc.svg
    :target: http://pypi.python.org/pypi/django-modelsdoc/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/django-modelsdoc.svg
    :target: http://pypi.python.org/pypi/django-modelsdoc/
    :alt: license
