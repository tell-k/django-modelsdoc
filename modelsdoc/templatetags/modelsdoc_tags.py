#! -*- coding: utf-8 -*-
"""
    modelsdoc.templatetags.modelsdoc_tags
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA

import django
from django.db.models.fields import NOT_PROVIDED
from django.db import router
from django.template import Library, Node

import yaml

from modelsdoc.utils import get_parent_model_attr, get_related_field

register = Library()


class EmptylinelessNode(Node):

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        lines = []
        for line in self.nodelist.render(context).strip().split('\n'):
            if not line.strip():
                continue
            lines.append(line)
        return '\n'.join(lines)


@register.tag
def emptylineless(parser, token):
    """
    Removes empty line.

    Example usage::

        {% emptylineless %}
            test1

            test2

            test3
        {% endemptylineless %}

    This example would return this HTML::

            test1
            test2
            test3

    """
    nodelist = parser.parse(('endemptylineless',))
    parser.delete_first_token()
    return EmptylinelessNode(nodelist)


@register.filter
def get_attr(obj, attr):
    return getattr(obj, attr, '')


@register.filter
def str_repeat(times, string):
    return string * times


@register.filter
def yamldump(models):
    result = {}

    for model in models:
        dbname = router.db_for_read(model)

        table = {
            "name": model._model._meta.db_table,
            "logical_name": model.display_name,
            "comment": model.doc,
            "columns": [],
        }
        for field in model.fields:

            fk_table = None
            related = get_related_field(field, django.VERSION)
            if related:
                # TODO change table to column
                fk = get_parent_model_attr(related, django.VERSION)
                fk_table = fk._meta.db_table

            default_value = None
            if field.default != NOT_PROVIDED:
                default_value = field.default
                if callable(default_value):
                    default_value = default_value.__module__ + "." + default_value.__name__

            column = {
                "name": field.name,
                "verbose_name": str(field.verbose_name),
                "data_type": field.db_type,
                "is_primary": field.primary_key or False,
                "is_unique": field.unique or False,
                "is_index": field.db_index or False,
                "not_null": not field.null,
                "foreignkey": fk_table,
                "comment": field.comment,
                "default": default_value,
            }
            table["columns"].append(column)

        if dbname not in result:
            result[dbname] = dict(
                name=dbname,
                logical_name=dbname,
                comment="",
                tables=[]
            )

        result[dbname]["tables"].append(table)

    return yaml.dump(result, allow_unicode=True, default_flow_style=False)
