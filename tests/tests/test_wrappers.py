#! -*- coding:utf-8 -*-
"""
    tests.test_wrappers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA

import mock

from django.test import TestCase


class TestFieldWrapper(TestCase):

    def _getTargetClass(self):
        from modelsdoc.wrappers import FieldWrapper
        return FieldWrapper

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _getDummyModel(self, model=None):
        class DummyModel(object):

            __name__ = 'DummyModel'

            def __init__(self, model):
                self._model = model
        return DummyModel(model)

    def _getDummyField(self):
        class DummyField(object):

            name = 'test_field'
            proxy_attr = 'test'

            def db_type(self, con):
                return 'test' if con else None

        return DummyField()

    @mock.patch('modelsdoc.wrappers.get_null_blank',
                return_value='dummy_field')
    def test_null_blank(self, mock):
        target = self._makeOne('dummy_field', 'dummy', 'dummy', 'dummy')
        self.assertEqual('dummy_field', target.null_blank)
        mock.assert_called_with('dummy_field')

    def test_comment(self):
        target = self._makeOne(
            self._getDummyField(),
            self._getDummyModel(model=self._getDummyModel()),
            'connection',
            {('DummyModel', 'test_field'): ['test1', 'test2']}
        )
        self.assertEqual('test1 test2', target.comment)

    def test_db_type(self):
        target = self._makeOne(self._getDummyField(),
                               'dummy', 'connection', 'dummy')
        self.assertEqual('test', target.db_type)

        target = self._makeOne(self._getDummyField(), 'dummy', '', 'dummy')
        self.assertEqual('', target.db_type)

    def test_getattr(self):
        target = self._makeOne(self._getDummyField(),
                               'dummy', 'connection', 'dummy')
        self.assertEqual('test', target.proxy_attr)
        self.assertEqual('', target.non_exists_attr)


class TestModelWrapper(TestCase):

    def _getTargetClass(self):
        from modelsdoc.wrappers import ModelWrapper
        return ModelWrapper

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _getDummyMeta(self):
        class DummyMeta(object):
            verbose_name = 'name'
            model = 'TestModel'
            concrete_model = 'TestModel'
            concrete_fields = ['field1', 'field2', 'field3']
            fields = concrete_fields

        return DummyMeta()

    def _getDummyModel(self, model=None):
        class DummyModel(object):
            """ TEST DOC STRING """

            __module__ = 'dummy_module'
            __name__ = 'DummyModel'

            def __init__(self, model=None, meta=None):
                self._model = model
                self._meta = meta
                self.proxy_attr = 'test'

        return DummyModel(model, self._getDummyMeta())

    def _getDummyAnalyizer(self):
        class DummyAnalyizer(object):

            def find_attr_docs(self):
                return 'dummy'
        return DummyAnalyizer()

    @mock.patch('modelsdoc.wrappers.class_to_string', return_value='dummy')
    def test_class_fullname(self, mock):

        target = self._makeOne(self._getDummyModel(), 'connection')
        self.assertEqual('dummy', target.class_fullname)
        mock.assert_called_with('TestModel')

    def test_class_name(self):
        target = self._makeOne(
            self._getDummyModel(self._getDummyModel()),
            'connection'
        )
        self.assertEqual('DummyModel', target.class_name)

    def test_doc(self):
        target = self._makeOne(self._getDummyModel(), 'connection')
        self.assertEqual(' TEST DOC STRING ', target.doc)

    def test_name(self):
        target = self._makeOne(self._getDummyModel(), 'connection')
        self.assertEqual('name', target.name)

    def test_fields(self):

        with mock.patch('modelsdoc.wrappers.ModuleAnalyzer.for_module',
                        return_value=self._getDummyAnalyizer()) as m:

            target = self._makeOne(self._getDummyModel(), 'connection')
            self.assertEqual(3, len(target.fields))
            m.assert_called_once_with('dummy_module')

    def test_attrdocs(self):
        with mock.patch('modelsdoc.wrappers.ModuleAnalyzer.for_module',
                        return_value=self._getDummyAnalyizer()) as m:

            target = self._makeOne(self._getDummyModel(), 'connection')
            self.assertEqual('dummy', target.attrdocs)
            m.assert_called_once_with('dummy_module')

    def test_getattr(self):
        target = self._makeOne(self._getDummyModel(), 'connection')
        self.assertEqual('test', target.proxy_attr)
        self.assertEqual('', target.non_exists_attr)
