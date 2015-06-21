#! -*- coding:utf-8 -*-
"""
    tests.test_utils
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA

from django.test import TestCase
import unittest


class TestGetModelAttr(unittest.TestCase):

    def _getTarget(self):
        from modelsdoc.utils import get_model_attr
        return get_model_attr

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):

        class DummyMetaOption(object):

            concrete_model = 'concrete_model'
            model = 'model'

        self.assertEqual('model',
                         self._callFUT(DummyMetaOption(), (1, 6)))
        self.assertEqual('concrete_model',
                         self._callFUT(DummyMetaOption(), (1, 5)))


class TestGetFieldsAttr(unittest.TestCase):

    def _getTarget(self):
        from modelsdoc.utils import get_fields_attr
        return get_fields_attr

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):

        class DummyMetaOption(object):

            concrete_fields = 'concrete_fields'
            fields = 'fields'

        self.assertEqual('concrete_fields',
                         self._callFUT(DummyMetaOption(), (1, 6)))
        self.assertEqual('fields',
                         self._callFUT(DummyMetaOption(), (1, 5)))


class TestGetParentModelAttr(unittest.TestCase):

    def _getTarget(self):
        from modelsdoc.utils import get_parent_model_attr
        return get_parent_model_attr

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):

        class DummyMetaOption(object):

            parent_model = 'parent_model'
            model = 'model'

        self.assertEqual('parent_model',
                         self._callFUT(DummyMetaOption(), (1, 7)))
        self.assertEqual('model',
                         self._callFUT(DummyMetaOption(), (1, 8)))


class TestClassToString(unittest.TestCase):

    def _getTarget(self):
        from modelsdoc.utils import class_to_string
        return class_to_string

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):

        class DummyModel(object):
            __name__ = 'DummyModel'
            __module__ = 'test_mod'

        self.assertEqual('test_mod.DummyModel', self._callFUT(DummyModel()))


class TestGetNullBlank(TestCase):

    def _getTarget(self):
        from modelsdoc.utils import get_null_blank
        return get_null_blank

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        from tests.models import Poll

        question = None
        null_field = None
        blank_field = None
        both_field = None
        for f in Poll._meta.fields:
            if f.name == 'question':
                question = f
            if f.name == 'null_field':
                null_field = f
            if f.name == 'blank_field':
                blank_field = f
            if f.name == 'both_field':
                both_field = f

        self.assertEqual('', self._callFUT(question))
        self.assertEqual('Blank', self._callFUT(blank_field))
        self.assertEqual('Null', self._callFUT(null_field))
        self.assertEqual('Both', self._callFUT(both_field))


class TestGetForeignkey(TestCase):

    def _getTarget(self):
        from modelsdoc.utils import get_foreignkey
        return get_foreignkey

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        from tests.models import Choice

        poll = None
        choice = None
        for f in Choice._meta.fields:
            if f.name == 'poll':
                poll = f
            if f.name == 'choice':
                choice = f

        self.assertEqual('FK:tests.models.Poll', self._callFUT(poll))
        self.assertEqual('', self._callFUT(choice))


class TestGetChoices(TestCase):

    def _getTarget(self):
        from modelsdoc.utils import get_choices
        return get_choices

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        from tests.models import Choice

        poll = None
        choice = None
        for f in Choice._meta.fields:
            if f.name == 'poll':
                poll = f
            if f.name == 'choice':
                choice = f

        self.assertEqual('1:test1, 2:test2, 3:test3', self._callFUT(choice))
        self.assertEqual('', self._callFUT(poll))


class TestImportClass(unittest.TestCase):

    def _getTarget(self):
        from modelsdoc.utils import import_class
        return import_class

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_it(self):
        self.assertEqual("<class 'modelsdoc.wrappers.ModelWrapper'>",
                         str(self._callFUT('modelsdoc.wrappers.ModelWrapper')))

        with self.assertRaises(AttributeError):
            self._callFUT('modelsdoc.wrappers.NonExistsWrapper')

        with self.assertRaises(ImportError):
            self._callFUT('modelsdoc.nonexists.Hoge')
