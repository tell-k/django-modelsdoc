#! -*- coding:utf-8 -*-
"""
    modelsdoc.management.commands.listing_models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k  <ffk2005@gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
from __future__ import division, print_function, absolute_import, unicode_literals  # NOQA
import sys

import logging
from optparse import make_option

import django
from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured
from django.db import connection

from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist

from modelsdoc import constants
from modelsdoc.utils import import_class, get_model_attr, get_models


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """ listing_models command """

    help = 'Listing your model definition. You can pass specify app name.'

    option_args = [
        dict(
            args=['-a', '--app'],
            kwargs=dict(dest='app',
                        help='Target only a specific app', default=None)
        ),
        dict(
            args=['-o', '--output'],
            kwargs=dict(dest='output_file',
                        help='Output file', default=None),
        ),
        dict(
            args=['-f', '--format'],
            kwargs=dict(dest='output_format',
                        help='Output format(rst/md)',
                        default=constants.OUTPUT_FORMAT)
        ),
    ]

    def __init__(self):
        if django.VERSION < (1, 8):  # pragma: no cover
            options = tuple([make_option(*o['args'], **o['kwargs']) for o in self.option_args])  # NOQA
            Command.option_list = BaseCommand.option_list + options
        else:
            def add_arguments(self, parser):
                for o in self.option_args:
                    parser.add_argument(*o['args'], **o['kwargs'])
            Command.add_arguments = add_arguments

        super(Command, self).__init__()

    def handle(self, app, output_file, output_format, *args, **options):

        if app or constants.APPS:
            apps = [app] if app else constants.APPS
            models = []
            for app in apps:
                try:
                    models += get_models(
                        constants.INCLUDE_AUTO_CREATED,
                        django.VERSION,
                        app
                    )
                except (ImproperlyConfigured, LookupError):
                    pass
        else:
            models = get_models(constants.INCLUDE_AUTO_CREATED, django.VERSION)
            models = sorted(
                models,
                key=lambda m: get_model_attr(m._meta, django.VERSION).__module__  # NOQA
            )

        if not models:
            msg = 'Cannot find models. Please add one model at least.'
            print(msg, file=sys.stderr)
            return

        try:
            model_wrapper = import_class(constants.MODEL_WRAPPER)
            template = '{}.{}'.format(constants.OUTPUT_TEMPLATE, output_format)
            rendered = render_to_string(
                template,
                {
                    'models': [model_wrapper(m, connection) for m in models],
                    'display_fields': constants.DISPLAY_FIELDS,
                }
            )
        except TemplateDoesNotExist:
            msg = 'Cannot find the output template file. {}'
            print(msg.format(template), file=sys.stderr)
            return

        if output_file:
            with open(output_file, 'wb') as fp:
                fp.write(rendered.encode('utf-8', errors='replace'))
            print('Complete! Create the output file. {}'.format(output_file))
        else:
            print(rendered)
