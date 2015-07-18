#! -*- coding: utf-8 -*-
"""
    tests.test_templatetags
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA

from django.template import Template, Context
from django.test import TestCase


class TestEmptylineless(TestCase):

    def _getTargetTags(self):
        return """
{% load modelsdoc_tags %}
{% emptylineless %}
test1

test2

test3
{% endemptylineless %}
"""

    def _callFUT(self):
        t = Template(self._getTargetTags())
        return t.render(Context())

    def test_remove_emptyline(self):
        self.assertEqual('\n\ntest1\ntest2\ntest3\n', self._callFUT())


class TestGetAttr(TestCase):

    def _getTargetTags(self):
        return '{% load modelsdoc_tags %}{{ obj|get_attr:attr_name }}'

    def _callFUT(self, obj, attr_name):
        t = Template(self._getTargetTags())
        return t.render(Context({'obj': obj, 'attr_name': attr_name}))

    def test_get_attr(self):

        class Dummy(object):

            test = 'test'

        self.assertEqual('test', self._callFUT(Dummy(), 'test'))
        self.assertEqual('', self._callFUT(Dummy(), 'non_exists_attr'))
