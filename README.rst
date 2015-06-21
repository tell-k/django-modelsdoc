=====================
django-modelsdoc
=====================

TODO

Quick start
-----------

1. Add "modelsdoc" to your INSTALLED_APPS setting like this

::

  INSTALLED_APPS = (
      ...
      'modelsdoc',
  )

2. Run **python manage.py listing_models** to listing model definition

You can check `Sample listing models<https://github.com/tell-k/django-modelsdoc/blob/master/tests/sample_models.rst>`

Option
-----------

--app(-a)
-----------------

You can pass specify app name. Listing only the specified app.

::

 $ python manage.py listing_models --app polls

--output(-o)
-----------------

It writes the results to the specified file.

::

 $ python manage.py listing_models --output sample.rst

--format(-f)
-----------------

You can choice output formats. **rst** (reStructuredText) or **md** (Markdown). Default format is **rst**.

::

 $ python manage.py listing_models --format md

Customize
-----------

TODO

Python and Django Support
---------------------------

.. csv-table::
   :widths: 10, 10, 10, 10, 10

   "　", "Django.1.5", "Django1.6", "Django1.7", "Django1.8"
   "Python 2.7","◯","◯","◯","◯"
   "PyPy","◯","◯","◯","◯"
   "Python 3.3","","","◯","◯"
   "Python 3.4","","","◯","◯"

License
-----------

MIT Licence

History
-----------


