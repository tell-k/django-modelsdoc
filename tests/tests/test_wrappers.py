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

    @mock.patch('modelsdoc.wrappers.get_null_blank',
                return_value='dummy_field')
    def test_null_blank(self, mock):
        target = self._makeOne('dummy_field', 'dummy', 'dummy', 'dummy')
        self.assertEqual('dummy_field', target.null_blank)
        mock.assert_called_with('dummy_field')

    def test_comment(self):

        class DummyModel(object):

            __name__ = 'DummyModel'

            def __init__(self, model):
                self._model = model

        class DummyField(object):

            name = 'test_field'

        target = self._makeOne(
            DummyField(),
            DummyModel(model=DummyModel),
            'connection',
            {('DummyModel', 'test_field'): ['test1', 'test2']}
        )
        self.assertEqual('test1 test2', target.comment)

    def test_db_type(self):

        class DummyField(object):

            def db_type(self, con):
                return 'test' if con else None

        target = self._makeOne(DummyField(), 'dummy', 'connection', 'dummy')
        self.assertEqual('test', target.db_type)

        target = self._makeOne(DummyField(), 'dummy', '', 'dummy')
        self.assertEqual('', target.db_type)

    def test_getattr(self):

        class DummyField(object):
            proxy_attr = 'test'

        target = self._makeOne(DummyField(), 'dummy', 'connection', 'dummy')
        self.assertEqual('test', target.proxy_attr)
        self.assertEqual('', target.non_exists_attr)


class DummyAnalyizer(object):

    def find_attr_docs(self):
        return 'dummy'


class TestModelWrapper(TestCase):

    def _getTargetClass(self):
        from modelsdoc.wrappers import ModelWrapper
        return ModelWrapper

    def _makeOne(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    @mock.patch('modelsdoc.wrappers.class_to_string', return_value='dummy')
    def test_class_fullname(self, mock):

        class DummyMeta(object):
            model = 'TestModel'
            concrete_model = 'TestModel'

        class DummyModel(object):
            _meta = DummyMeta()

        target = self._makeOne(DummyModel(), 'connection')
        self.assertEqual('dummy', target.class_fullname)
        mock.assert_called_with('TestModel')

    def test_class_name(self):

        class DummyModel(object):
            __name__ = 'DummyModel'

            def __init__(self, model=None):
                self._model = model

        target = self._makeOne(DummyModel(DummyModel()), 'connection')
        self.assertEqual('DummyModel', target.class_name)

    def test_doc(self):
        class DummyModel(object):
            """ TEST DOC STRING """

        target = self._makeOne(DummyModel(), 'connection')
        self.assertEqual(' TEST DOC STRING ', target.doc)

    def test_name(self):

        class DummyMeta(object):
            verbose_name = 'name'

        class DummyModel(object):
            _meta = DummyMeta()

        target = self._makeOne(DummyModel(), 'connection')
        self.assertEqual('name', target.name)

    @mock.patch('modelsdoc.wrappers.ModuleAnalyzer.for_module',
                return_value=DummyAnalyizer())
    def test_fields(self, mock):

        class DummmyMeta(object):
            concrete_fields = ['field1', 'field2', 'field3']
            fields = concrete_fields

        class DummyModel(object):
            __module__ = 'dummy_module'
            _meta = DummmyMeta()

        target = self._makeOne(DummyModel(), 'connection')
        self.assertEqual(3, len(target.fields))
        mock.assert_called_once_with('dummy_module')

    @mock.patch('modelsdoc.wrappers.ModuleAnalyzer.for_module',
                return_value=DummyAnalyizer())
    def test_attrdocs(self, mock):

        class DummyModel(object):
            __module__ = 'dummy_module'

        target = self._makeOne(DummyModel(), 'connection')
        self.assertEqual('dummy', target.attrdocs)
        mock.assert_called_once_with('dummy_module')

    def test_getattr(self):

        class DummyModel(object):
            proxy_attr = 'test'

        target = self._makeOne(DummyModel(), 'connection')
        self.assertEqual('test', target.proxy_attr)
        self.assertEqual('', target.non_exists_attr)
