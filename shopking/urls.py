from django.conf.urls import patterns, include, url
from oscar.app import application
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'',include(application.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
