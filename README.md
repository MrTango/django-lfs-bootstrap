Django-LFS bootstrap
====================

A simple and pythonic way to build your django-lfs shop.

Install django and django-lfs
-----------------------------

$pip install -r requirements.txt


Make your settings
------------------

The settings are in settings.py and local_settings.py. You can override every from settings.py in you local_settings.py.
As a starting point you can just copy the local_settings.py_tmpl

$cp local_settings.py_tmpl local_settings.py

Then define your database and language aso in local_settings.py or settings.py
You can override every from settings.py in you local_settings.py

Sync th database:

$./manage.py syncdb

Initialize lfs:

$./manage.py lfs_init

Collect static files:

$./manage.py collectstatic


And finaly use runserver to start your shop:

$./manage.py runserver

