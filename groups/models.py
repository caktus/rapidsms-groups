#/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from django.db import models

from rapidsms.models import Contact

from groups.utils import format_number


class GroupContact(models.Model):
    """ Model to extend the RapidSMS Contact model """
    contact = models.OneToOneField(Contact)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=True)
    title = models.CharField(max_length=64, blank=True)

    def save(self, **kwargs):
        self.name = '%s %s' % (self.first_name, self.last_name)
        super(GroupContact, self).save(**kwargs)

    @property
    def formatted_phone(self):
        return format_number(self.phone)


class Group(models.Model):
    """ Organize RapidSMS contacts into groups """
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    is_editable = models.BooleanField(default=True)

    contacts = models.ManyToManyField(GroupContact, related_name='groups',
                                      blank=True)

    def __unicode__(self):
        return self.name
