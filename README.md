Django-LFS bootstrap
====================

A simple and pythonic way to build your django-lfs shop.

Clone django-lfs-bootstrap
--------------------------

	$ git clone https://github.com/MrTango/django-lfs-bootstrap.git shop

The you have the following structure:

	./shop
	├── lfs_project
	│   ├── __init__.py
	│   ├── local_settings.py_tmpl
	│   ├── manage.py
	│   ├── settings.py
	│   └── urls.py
	├── README.md
	└── requirements.txt


Create virtualenv
-----------------

Its recommended to use virtalenv to avoid conflicts. If you don't know virtualenv please read this: http://pypi.python.org/pypi/virtualenv/.

Install django and django-lfs
-----------------------------

	$ pip install -r requirements.txt

Make your settings
------------------

The settings are in settings.py and local_settings.py. You can override every from settings.py in you local_settings.py.
As a starting point you can just copy the local_settings.py_tmpl

	$ cp local_settings.py_tmpl local_settings.py

Then define your database and language aso in local_settings.py or settings.py
You can override every from settings.py in you local_settings.py

Sync the database
-----------------

	$ ./manage.py syncdb

Initialize lfs
--------------

	$ ./manage.py lfs_init

Collect static files
--------------------

	$ ./manage.py collectstatic

Start your shop:
----------------

	$ ./manage.py runserver 

or

	$ ./manage.py runserver 127.0.0.1:8080

Using other WSGI servers
------------------------

Of course, you can use any WSGI server like [Gunicorn](http://gunicorn.org/), [uWSGI](http://projects.unbit.it/uwsgi) or [Chaussette](http://chaussette.readthedocs.org/) to run your shop now. 

### uWSGI example

You can just install and run your shop with uWSGI like so:

	$ pip install uwsgi

Then create an ini-file uwsgi.ini for example:

	[uwsgi]
	uid = lfs
	gid = lfs
	master = true
	processes = 4
	threads = 1
	# set the http port
	http = :8001
	# change to django project directory
	chdir = /home/lfs/shop/lfs_project
	pythonpath = /home/lfs/shop
	virtualenv = /home/lfs/.virtualenvs/venv1/
	env = DJANGO_SETTINGS_MODULE=lfs_project.settings
	# load django
	module = django.core.handlers.wsgi:WSGIHandler()
	daemonize = /home/lfs/shop/uwsgi.log
	pidfile2 = /home/lfs/shop/uwsgi.pid	

Then you can start your shop:

	$ uwsgi --ini uwsgi.ini

And to stop uwsgi:

	$ uwsgi --stop uwsgi.pid

Have fun ;)
