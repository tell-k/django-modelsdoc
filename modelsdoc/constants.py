#! -*- coding:utf-8 -*-
"""
    modelsdoc.constants
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA
from django.conf import settings


DEFAULT_DISPLAY_FIELDS = (
    ('Fullname', 'verbose_name'),
    ('Name', 'name'),
    ('Type', 'db_type'),
    ('PK', 'primary_key'),
    ('Unique', 'unique'),
    ('Index', 'db_index'),
    ('Null/Blank', 'null_blank'),
    ('Comment', 'comment'),
)
DEFAULT_OUTPUT_TEMPLATE = 'modelsdoc/models'
DEFAULT_OUTPUT_FORMAT = 'rst'
DEFAULT_MODEL_WRAPPER = 'modelsdoc.wrappers.ModelWrapper'
DEFAULT_FIELD_WRAPPER = 'modelsdoc.wrappers.FieldWrapper'

DEFAULT_MODEL_OPTIONS = (
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
    # 'auto_created',
    # 'managed',
    # 'proxy',
    # 'verbose_name',
    # 'verbose_name_plural',
    # 'app_label',
    # 'db_table',
    # 'apps',
)

APPS = getattr(settings, 'MODELSDOC_APPS', [])

DISPLAY_FIELDS = getattr(settings, 'MODELSDOC_DISPLAY_FIELDS',
                         DEFAULT_DISPLAY_FIELDS)
OUTPUT_TEMPLATE = getattr(settings, 'MODELSDOC_OUTPUT_TEMPLATE',
                          DEFAULT_OUTPUT_TEMPLATE)
OUTPUT_FORMAT = getattr(settings, 'MODELSDOC_OUTPUT_FORMAT',
                        DEFAULT_OUTPUT_FORMAT)
MODEL_WRAPPER = getattr(settings, 'MODELSDOC_MODEL_WRAPPER',
                        DEFAULT_MODEL_WRAPPER)
FIELD_WRAPPER = getattr(settings, 'MODELSDOC_FIELD_WRAPPER',
                        DEFAULT_FIELD_WRAPPER)
MODEL_OPTIONS = getattr(settings, 'MODELSDOC_MODEL_OPTIONS',
                        DEFAULT_MODEL_OPTIONS)
