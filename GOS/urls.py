from django.conf.urls import patterns, include, url
from GOS.views import homepage
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', homepage),
                       (r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'GOS.views.home', name='home'),
    # url(r'^GOS/', include('GOS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
