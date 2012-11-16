#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from django.conf.urls.defaults import url, patterns

from groups import views


urlpatterns = patterns('',
    url(r'^group/$', views.list_groups,
        name='list-groups'),
    url(r'^group/create/$', views.create_edit_group,
        name='create-group'),
    url(r'^group/(\d+)/$', views.create_edit_group,
        name='edit-group'),
    url(r'^group/(\d+)/delete/$', views.delete_group,
        name='delete-group'),
    url(r'^contact/$', views.list_contacts,
        name='list-contacts'),
    url(r'^contact/create/$', views.create_edit_contact,
        name='create-contact'),
    url(r'^contact/(\d+)/$', views.create_edit_contact,
        name='edit-contact'),
    url(r'^contact/(\d+)/delete/$', views.delete_contact,
        name='delete-contact'),
)
