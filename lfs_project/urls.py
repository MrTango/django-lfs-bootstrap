# django imports
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

import os
DIRNAME = os.path.dirname(__file__)

handler500 = 'lfs.core.views.server_error'

urlpatterns = patterns("",
    (r'', include('lfs.core.urls')),
    (r'^manage/', include('lfs.manage.urls')),
)

urlpatterns += patterns("",
    (r'^reviews/', include('reviews.urls')),
    (r'^paypal/ipn/', include('paypal.standard.ipn.urls')),
    (r'^paypal/pdt/', include('paypal.standard.pdt.urls')),
)

urlpatterns += patterns("",
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(DIRNAME, "media"), 'show_indexes': True }),
)
