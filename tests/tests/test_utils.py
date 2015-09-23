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

    def _callFUT(self, option_model, django_version):
        from modelsdoc.utils import get_model_attr
        return get_model_attr(option_model, django_version)

    def _getDummyMetaOption(self):
        class DummyMetaOption(object):

            concrete_model = 'concrete_model'
            model = 'model'
        return DummyMetaOption()

    def test_django_ver16_over(self):
        self.assertEqual(
            'model',
            self._callFUT(self._getDummyMetaOption(), (1, 6))
        )

    def test_django_ver15(self):
        self.assertEqual(
            'concrete_model',
            self._callFUT(self._getDummyMetaOption(), (1, 5))
        )


class TestGetFieldsAttr(unittest.TestCase):

    def _getDummyMetaOption(self):
        class DummyMetaOption(object):

            concrete_fields = ('concrete_fields',)
            fields = ('fields',)
            many_to_many = ('many2many',)

        return DummyMetaOption()

    def _callFUT(self, option_model, django_version):
        from modelsdoc.utils import get_fields_attr
        return get_fields_attr(option_model, django_version)

    def test_django_ver16_over(self):
        self.assertEqual(
            ['concrete_fields', 'many2many'],
            self._callFUT(self._getDummyMetaOption(), (1, 6))
        )

    def test_django_ver15(self):
        self.assertEqual(
            ['fields', 'many2many'],
            self._callFUT(self._getDummyMetaOption(), (1, 5))
        )


class TestGetParentModelAttr(unittest.TestCase):

    def _callFUT(self, related_field, django_version):
        from modelsdoc.utils import get_parent_model_attr
        return get_parent_model_attr(related_field, django_version)

    def _getDummyMetaOption(self):
        class DummyMetaOption(object):

            parent_model = 'parent_model'
            model = 'model'

        return DummyMetaOption()

    def test_django_ver17_lower(self):
        self.assertEqual(
            'parent_model',
            self._callFUT(self._getDummyMetaOption(), (1, 7))
        )

    def test_django_ver18(self):
        self.assertEqual(
            'model',
            self._callFUT(self._getDummyMetaOption(), (1, 8))
        )


class TestClassToString(unittest.TestCase):

    def _callFUT(self, model):
        from modelsdoc.utils import class_to_string
        return class_to_string(model)

    def _getDummyModel(self):
        class DummyModel(object):
            __name__ = 'DummyModel'
            __module__ = 'test_mod'
        return DummyModel()

    def test_to_string(self):
        self.assertEqual(
            'test_mod.DummyModel',
            self._callFUT(self._getDummyModel())
        )


class TestGetNullBlank(TestCase):

    def _callFUT(self, field):
        from modelsdoc.utils import get_null_blank
        return get_null_blank(field)

    def _getDummyField(self, null, blank):
        class DummyField(object):

            def __init__(self, null, blank):
                self.null = null
                self.blank = blank
        return DummyField(null, blank)

    def test_not_allow_null_and_blank(self):
        self.assertEqual(
            '',
            self._callFUT(self._getDummyField(null=False, blank=False))
        )

    def test_allow_blank_only(self):
        self.assertEqual(
            'Blank',
            self._callFUT(self._getDummyField(null=False, blank=True))
        )

    def test_allow_null_only(self):
        self.assertEqual(
            'Null',
            self._callFUT(self._getDummyField(null=True, blank=False))
        )

    def test_allow_both(self):
        self.assertEqual(
            'Both',
            self._callFUT(self._getDummyField(null=True, blank=True))
        )


class TestGetForeignkey(TestCase):

    def _callFUT(self, field):
        from modelsdoc.utils import get_foreignkey
        return get_foreignkey(field)

    def _getTargetField(self, field_name):
        from tests.models import Choice
        return Choice._meta.get_field(field_name)

    def test_is_foreignkey(self):
        self.assertEqual(
            'FK:tests.models.Poll',
            self._callFUT(self._getTargetField('poll'))
        )

    def test_not_foreignkey(self):
        self.assertEqual(
            '',
            self._callFUT(self._getTargetField('choice'))
        )

    def test_many_to_many_field(self):
        self.assertEqual(
            'M2M:tests.models.Genre (through: tests.models.Choice_genres)',
            self._callFUT(self._getTargetField('genres'))
        )


class TestGetChoices(TestCase):

    def _callFUT(self, field):
        from modelsdoc.utils import get_choices
        return get_choices(field)

    def _getTargetField(self, field_name):
        from tests.models import Choice
        for f in Choice._meta.fields:
            if f.name != field_name:
                continue
            return f

    def test_is_choices(self):
        self.assertEqual(
            '1:test1, 2:test2, 3:test3',
            self._callFUT(self._getTargetField('choice'))
        )

    def test_not_choices(self):
        self.assertEqual(
            '',
            self._callFUT(self._getTargetField('poll'))
        )


class TestImportClass(unittest.TestCase):

    def _callFUT(self, cl):
        from modelsdoc.utils import import_class
        return import_class(cl)

    def test_import_ok(self):
        self.assertEqual(
            "<class 'modelsdoc.wrappers.ModelWrapper'>",
            str(self._callFUT('modelsdoc.wrappers.ModelWrapper'))
        )

    def test_raise_attribute_error(self):
        with self.assertRaises(AttributeError):
            self._callFUT('modelsdoc.wrappers.NonExistsWrapper')

    def test_raise_import_error(self):
        with self.assertRaises(ImportError):
            self._callFUT('modelsdoc.nonexists.Hoge')
