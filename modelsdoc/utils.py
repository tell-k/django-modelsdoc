#! -*- coding:utf-8 -*-
"""
    modelsdoc.utils
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA

import django


def get_model_attr(option_model, django_version):
    if django_version < (1, 6):
        return getattr(option_model, 'concrete_model')
    else:
        return getattr(option_model, 'model')


def get_fields_attr(option_model, django_version):
    if django_version < (1, 6):
        return getattr(option_model, 'fields')
    else:
        return getattr(option_model, 'concrete_fields')


def get_parent_model_attr(related_field, django_version):
    if django_version < (1, 8):
        return getattr(related_field, 'parent_model')
    else:
        return getattr(related_field, 'model')


def class_to_string(model):
    return '{}.{}'.format(model.__module__, model.__name__)


def get_null_blank(field):
    if field.blank and field.null:
        return 'Both'
    elif field.blank:
        return 'Blank'
    elif field.null:
        return 'Null'
    return ''


def get_foreignkey(field):
    if not getattr(field, 'related', None):
        return ''
    return 'FK:' + class_to_string(
        get_parent_model_attr(field.related, django.VERSION)
    )


def get_choices(field):
    if not getattr(field, 'choices', None):
        return ''
    return ', '.join(['{}:{}'.format(*c) for c in field.choices])


def import_class(cl):
    d = cl.rfind('.')
    classname = cl[d + 1:len(cl)]
    m = __import__(cl[0:d], globals(), locals(), [classname])
    return getattr(m, classname)
