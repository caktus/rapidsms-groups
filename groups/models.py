#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from django.db import models

from rapidsms.models import Contact


class Group(models.Model):
    """ Organize RapidSMS contacts into groups """
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    is_editable = models.BooleanField(default=True)

    contacts = models.ManyToManyField(Contact, related_name='groups',
                                      blank=True)

    def __unicode__(self):
        return self.name
