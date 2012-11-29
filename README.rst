rapidsms-groups
===============

rapidsms-groups integrates with the RapidSMS framework and allows you to
define groups of Contacts.


Getting Started
---------------

To add rapidsms-groups to an existing RapidSMS project, add it and its
dependencies to your installed apps::

    INSTALLED_APPS = [
        ...
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'rapidsms',
        'rapidsms.contrib.messagelog',
        'groups',
        'pagination',
        'sorter',
        ...
    ]

In addition to the default middleware classes, be sure to include pagination
middleware::

    MIDDLEWARE_CLASSES = [
        ...
        'pagination.middleware.PaginationMiddleware',
        ...
    ]

Configure django_sorter::

    SORTER_ALLOWED_CRITERIA = {
        'sort_contacts': ['id', 'name', 'email', 'phone'],
        'sort_groups': ['id', 'name', 'count'],
    }

Add contacts URLs to your urlconf::

    urlpatterns += patterns('',
        (r'^groups/', include('groups.urls')),
    )

Optionally, add links to groups and contacts in your ``RAPIDSMS_TABS`` setting::

    RAPIDSMS_TABS += [
        ('groups.views.list_groups', 'Groups'),
        ('groups.views.list_contacts', 'Contacts'),
    ]

Finally, run syncdb or migrate::

    python manage.py migrate groups


Running the Tests
-----------------

You can run the tests via::

    python runtests.py

If you would like to run specific test(s), specify them as arguments to the
command::

    python runtests.py groups.GroupViewTest.test_editable_views


License
-------

rapidsms-groups is released under the BSD License. See the `LICENSE
<https://github.com/caktus/rapidsms-groups/blob/master/LICENSE>`_ file for
more details.


Contributing
------------

If you think you've found a bug or are interested in contributing to this
project check out `rapidsms-groups on Github
<https://github.com/caktus/rapidsms-groups>`_.

Development sponsored by `Caktus Consulting Group, LLC
<http://www.caktusgroup.com/services>`_.
