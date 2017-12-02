#! -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    """ Poll

    * Poll has question and description fields
    """

    question = models.CharField('Question Name', max_length=255)
    description = models.TextField('Description', blank=True)
    """ Description field allows Blank """

    null_field = models.CharField('Null Test', null=True, max_length=255)
    blank_field = models.CharField('Blank Test', blank=True, max_length=255)
    both_field = models.CharField('Both Test',
                                  null=True, blank=True, max_length=255)
    index_field = models.CharField('Index Test', db_index=True, max_length=255)

    class Meta:
        verbose_name = 'Poll'


class Genre(models.Model):
    """ Genre

    * Choice has genre
    """
    name = models.CharField('Genre name', max_length=255)

    class Meta:
        verbose_name = 'Genre'


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

    poll = models.ForeignKey(Poll, verbose_name='Poll',
                             on_delete=models.CASCADE)
    choice = models.SmallIntegerField('Choice', choices=CHOICES)

    genres = models.ManyToManyField(Genre, verbose_name='Genre')

    class Meta:
        verbose_name = 'Choice'


class Vote(models.Model):
    """ Vote

    * Vote has user reference
    * Vote has poll reference
    * Vote has choice reference
    """

    user = models.ForeignKey(User, verbose_name='Voted User',
                             on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, verbose_name='Voted Poll',
                             on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, verbose_name='Voted Choice',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vote'
        unique_together = (('user', 'poll'))
