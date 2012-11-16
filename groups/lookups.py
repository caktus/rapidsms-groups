#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from django.http import HttpResponse
from django.utils import simplejson
from django.core.serializers import json

from selectable.base import ModelLookup
from selectable.registry import registry

from rapidsms.models import Contact


class ContactLookup(ModelLookup):
    model = Contact
    filters = {'patient__isnull': True}
    search_fields = ('name__icontains', )

    def results(self, request):
        term = request.GET.get('term', '')
        raw_data = self.get_query(request, term)[:10]
        data = [self.format_item(item) for item in raw_data]
        content = simplejson.dumps(data, cls=json.DjangoJSONEncoder,
                                   ensure_ascii=False)
        return HttpResponse(content, content_type='application/json')

registry.register(ContactLookup)
