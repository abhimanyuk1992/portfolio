from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'abhimanyu_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',	include('resume.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
