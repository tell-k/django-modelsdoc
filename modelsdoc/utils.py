#! -*- coding:utf-8 -*-
"""
    modelsdoc.utils
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA

import django


def get_models(include_auto_created, django_version, appname=None):
    if django_version < (1, 7):  # pragma: no cover
        from django.db.models import get_app, get_models
        if appname:
            return get_models(
                app_mod=get_app(appname),
                include_auto_created=include_auto_created
            )
        else:
            return get_models(
                include_auto_created=include_auto_created
            )
    else:
        from django.apps import apps
        if appname:
            app = apps.get_app_config(appname)
            return app.get_models(include_auto_created=include_auto_created)
        else:
            return apps.get_models(include_auto_created=include_auto_created)


def get_model_attr(option_model, django_version):
    if django_version < (1, 6):
        return getattr(option_model, 'concrete_model')
    else:
        return getattr(option_model, 'model')


def get_fields_attr(option_model, django_version):
    if django_version < (1, 6):
        fields = list(getattr(option_model, 'fields'))
    else:
        fields = list(getattr(option_model, 'concrete_fields'))
    for f in getattr(option_model, 'many_to_many', []):
        fields.append(f)
    return fields


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


def get_related_field(field, django_version):
    if django_version < (1, 9):
        return getattr(field, 'related', None)
    else:
        return getattr(field, 'remote_field', None)


def get_foreignkey(field):
    related_field = get_related_field(field, django.VERSION)
    if not related_field:
        return ''

    label = 'FK:'
    through = ''
    if hasattr(field, 'm2m_column_name'):
        label = 'M2M:'
        through = ' (through: {})'.format(
            class_to_string(field.rel.through))

    return '{}{}{}'.format(
        label,
        class_to_string(get_parent_model_attr(related_field, django.VERSION)),
        through
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
