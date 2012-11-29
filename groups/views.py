#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404

from rapidsms.models import Contact

from groups.models import Group
from groups.forms import GroupForm, ContactForm


@login_required
def list_groups(request):
    groups = Group.objects.annotate(count=Count('contacts')).order_by('name')
    return render(request, 'groups/groups/list.html', {
        'groups': groups,
    })


@login_required
@transaction.commit_on_success
def create_edit_group(request, group_id=None):
    group = None
    if group_id:
        group = get_object_or_404(Group, pk=group_id)
        if not group.is_editable:
            return HttpResponseForbidden('Access denied')
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.info(request, 'Group saved successfully')
            return HttpResponseRedirect(reverse('list-groups'))
    else:
        form = GroupForm(instance=group)
    return render(request, 'groups/groups/create_edit.html', {
        'form': form,
        'group': group,
    })


@login_required
@transaction.commit_on_success
def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if not group.is_editable:
        return HttpResponseForbidden('Access denied')
    if request.method == 'POST':
        group.delete()
        messages.info(request, 'Group successfully deleted')
        return HttpResponseRedirect(reverse('list-groups'))
    return render(request, 'groups/groups/delete.html', {
        'group': group,
    })


@login_required
def list_contacts(request):
    contacts = Contact.objects.all().order_by('name')
    return render(request, 'groups/contacts/list.html', {
        'contacts': contacts,
    })


@login_required
@transaction.commit_on_success
def create_edit_contact(request, contact_id=None):
    contact = None
    if contact_id:
        contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.info(request, 'Contact saved successfully')
            return HttpResponseRedirect(reverse('list-contacts'))
    else:
        form = ContactForm(instance=contact)
    return render(request, 'groups/contacts/create_edit.html', {
        'form': form,
        'contact': contact,
    })


@login_required
@transaction.commit_on_success
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        messages.info(request, 'Contact successfully deleted')
        return HttpResponseRedirect(reverse('list-contacts'))
    return render(request, 'groups/contacts/delete.html', {
        'contact': contact,
    })
