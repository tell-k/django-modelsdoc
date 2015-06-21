#! -*- coding:utf-8 -*-
"""
    tests.test_commands.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA

from django.test import TestCase
from testfixtures import OutputCapture


class TestModels2rst(TestCase):

    def _callCommand(self, *args, **kwargs):
        from django.core.management import call_command
        return call_command('listing_models', **kwargs)

    def test_it(self):
        with OutputCapture() as o:
            self._callCommand()

        self.assertTrue('Poll(tests.models.Poll)' in o.captured)
        self.assertTrue('Choice(tests.models.Choice)' in o.captured)
        self.assertTrue('Vote(tests.models.Vote)' in o.captured)
        self.assertTrue('* - Question Name' in o.captured)
        self.assertTrue('- varchar(255)' in o.captured)
        self.assertTrue("unique_together : (('user', 'poll'),)" in o.captured)
        self.assertTrue('Description field allows Blank' in o.captured)

    def test_option_app(self):
        with OutputCapture() as o:
            self._callCommand(app='tests')

        self.assertTrue('Poll(tests.models.Poll)' in o.captured)
        self.assertTrue('Choice(tests.models.Choice)' in o.captured)
        self.assertTrue('Vote(tests.models.Vote)' in o.captured)
        self.assertTrue('* - Question Name' in o.captured)
        self.assertTrue('- varchar(255)' in o.captured)
        self.assertTrue("unique_together : (('user', 'poll'),)" in o.captured)
        self.assertTrue('Description field allows Blank' in o.captured)

        with OutputCapture() as o:
            self._callCommand(app='missing_app')

        self.assertTrue('Cannot find models' in o.captured)

    def test_option_output(self):
        import tempfile
        temp = tempfile.NamedTemporaryFile()

        with OutputCapture() as o:
            self._callCommand(output_file=temp.name)

        self.assertTrue('Complete! Create the output file.' in o.captured)

        with open(temp.name) as fp:
            body = fp.read()

        self.assertTrue('Poll(tests.models.Poll)' in body)
        self.assertTrue('Choice(tests.models.Choice)' in body)
        self.assertTrue('Vote(tests.models.Vote)' in body)
        self.assertTrue('* - Question Name' in body)
        self.assertTrue('- varchar(255)' in body)
        self.assertTrue("unique_together : (('user', 'poll'),)" in body)
        self.assertTrue('Description field allows Blank' in body)

    def test_option_format(self):

        with OutputCapture() as o:
            self._callCommand(output_format='rst')

        self.assertTrue('Poll(tests.models.Poll)' in o.captured)
        self.assertTrue('Choice(tests.models.Choice)' in o.captured)
        self.assertTrue('Vote(tests.models.Vote)' in o.captured)
        self.assertTrue('* - Question Name' in o.captured)
        self.assertTrue('- varchar(255)' in o.captured)
        self.assertTrue("unique_together : (('user', 'poll'),)" in o.captured)
        self.assertTrue('Description field allows Blank' in o.captured)

        with OutputCapture() as o:
            self._callCommand(output_format='md')

        self.assertTrue('## Poll(tests.models.Poll)' in o.captured)
        self.assertTrue('## Choice(tests.models.Choice)' in o.captured)
        self.assertTrue('## Vote(tests.models.Vote)' in o.captured)
        self.assertTrue("unique_together : (('user', 'poll'),)" in o.captured)
        self.assertTrue('Description field allows Blank' in o.captured)
        self.assertTrue(
            '|Question Name|question|varchar(255)||||||' in o.captured
        )

        with OutputCapture() as o:
            self._callCommand(output_format='unknown')

        self.assertTrue('Cannot find the output template file' in o.captured)
