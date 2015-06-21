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
from django.db.models import get_models, get_app
from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist

from modelsdoc import constants
from modelsdoc.utils import import_class, get_model_attr


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """ listing_models command """

    help = 'Listing your model definition. You can pass specify app name.'

    option_list = BaseCommand.option_list + (
        make_option('-a', '--app', dest='app',
                    help='Target only a specific app', default=None),
        make_option('-o', '--output', dest='output_file',
                    help='Output file', default=None),
        make_option('-f', '--format',
                    dest='output_format', help='Output format(rst/md)',
                    default=constants.OUTPUT_FORMAT)
    )

    def handle(self, app, output_file, output_format, *args, **options):

        if app or constants.APPS:
            apps = [app] if app else constants.APPS
            models = []
            for app in apps:
                try:
                    models += get_models(app_mod=get_app(app))
                except ImproperlyConfigured:
                    pass
        else:
            models = get_models(include_auto_created=True)
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
            print(rendered.encode('utf-8', errors='replace'))
