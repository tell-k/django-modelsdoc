#! -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    """ Poll

    * Poll has question and description fields
    """

    question = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    """ Description field allows Blank """

    null_field = models.CharField(null=True, max_length=255)
    blank_field = models.CharField(blank=True, max_length=255)
    both_field = models.CharField(null=True, blank=True, max_length=255)
    index_field = models.CharField(db_index=True, max_length=255)

    class Meta:
        verbose_name = 'Poll'


class Choice(models.Model):
    """ Choice

    * Choice has poll reference
    * Choice has choices field
    """

    CHOICES = (
        (1, 'test1'),
        (2, 'test2'),
        (3, 'test3'),
    )

    poll = models.ForeignKey(Poll)
    choice = models.SmallIntegerField(max_length=255, choices=CHOICES)

    class Meta:
        verbose_name = 'Choice'


class Vote(models.Model):
    """ Vote

    * Vote has user reference
    * Vote has poll reference
    * Vote has choice reference
    """

    user = models.ForeignKey(User)
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)

    class Meta:
        verbose_name = 'Vote'
        unique_together = (('user', 'poll'))
