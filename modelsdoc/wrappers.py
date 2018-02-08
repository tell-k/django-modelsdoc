#! -*- coding:utf-8 -*-
"""
    modelsdoc.wrappers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA

from sphinx.pycode import ModuleAnalyzer
import django
from django.utils.encoding import force_bytes

from modelsdoc.utils import (
    class_to_string, get_foreignkey,
    get_choices, get_null_blank, import_class,
    get_model_attr, get_fields_attr
)
from modelsdoc import constants


class FieldWrapper(object):

    def __init__(self, field, model, connection, attrdocs):
        self._model = model
        self._field = field
        self._connection = connection
        self._attrdocs = attrdocs

    @property
    def comment(self):
        comment = get_foreignkey(self._field)
        comment += get_choices(self._field)
        key = (self._model._model.__name__, self._field.name)
        comment += ' '.join(self._attrdocs.get(key, []))
        return comment

    @property
    def null_blank(self):
        return get_null_blank(self._field)

    @property
    def db_type(self):
        return self._field.db_type(self._connection) or ''

    def __getattr__(self, name):
        if hasattr(self._field, name):
            return getattr(self._field, name) or ''
        return ''


class ModelWrapper(object):

    def __init__(self, model, connection):
        self._model = model
        self._attrdocs = []
        self._model_options = {}
        self._connection = connection
        self._field_wrapper_cls = import_class(constants.FIELD_WRAPPER)

    @property
    def class_fullname(self):
        return class_to_string(
            get_model_attr(self._model._meta, django.VERSION))

    @property
    def class_name(self):
        return self._model._model.__name__

    @property
    def display_name(self):
        return '{}({})'.format(self.name, self.class_fullname)

    @property
    def display_name_length(self):
        """ Return length of byte string. for reST section """
        return len(force_bytes(self.display_name))

    @property
    def doc(self):
        return self._model.__doc__

    @property
    def attrdocs(self):
        if self._attrdocs:
            return self._attrdocs
        analyzer = ModuleAnalyzer.for_module(self._model.__module__)
        self._attrdocs = analyzer.find_attr_docs()
        return self._attrdocs

    @property
    def model_options(self):
        if self._model_options:
            return self._model_options
        for option in constants.MODEL_OPTIONS:
            if not hasattr(self._model._meta, option) or\
                    not getattr(self._model._meta, option):
                continue
            self._model_options.update(
                {option: getattr(self._model._meta, option)})
        return self._model_options

    @property
    def name(self):
        return self._model._meta.verbose_name

    @property
    def fields(self):
        return [
            self._field_wrapper_cls(f, self, self._connection, self.attrdocs)
            for f in get_fields_attr(self._model._meta, django.VERSION)
        ]

    def __getattr__(self, name):
        if hasattr(self._model, name):
            return getattr(self._model, name) or ''
        return ''
