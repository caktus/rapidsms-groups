#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from rapidsms.apps.base import AppBase
from rapidsms.models import Contact

from groups.models import GroupContact
from groups.utils import normalize_number


class GroupsApp(AppBase):

    def _associate_contact(self, connection):
        normalized_number = normalize_number(connection.identity)
        self.debug('Normalized number: {0}'.format(normalized_number))
        try:
            group_contact = GroupContact.objects.get(phone=normalized_number)
        except GroupContact.DoesNotExist:
            self.debug('Failed to find matching contact')
            group_contact = None
        if group_contact:
            self.debug('Associating connection to {0}'.format(group_contact.contact))
            connection.contact = group_contact.contact
            connection.save()

    def filter(self, msg):
        # XXX for some reason msg.connections is an instance rather than a list; need to figure out why
        if not msg.connections.contact:
            self.debug('Found {0} without contact'.format(msg.connections))
            self._associate_contact(msg.connections)
