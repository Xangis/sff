# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'db.views.index'),
    url(r"^show/(?P<id>\d+)/rate/(?P<rating>\d+)/$", 'db.views.rate_show' ),
    url(r"^show/(?P<show_name>[\w\W]+)/episode/(?P<episode_name>[\w\W]+)/$", 'db.views.view_episode' ),
    url(r"^people/$", 'db.views.view_people' ),
    url(r"^person/(?P<person_name>[\w\W]+)/$", 'db.views.view_person' ),
    url(r"^show/(?P<show_name>[0-9a-zA-Z()',: -]+)/$", 'db.views.view_show' ),
    url(r"^movie/(?P<movie_name>[0-9a-zA-Z()',: -]+)/$", 'db.views.view_movie' ),
    url(r"^company/(?P<name>[0-9a-zA-Z()',: -]+)/$", 'db.views.view_company' ),
    url(r"^subgenres/$", 'db.views.subgenres' ),
    url(r"^subgenre/(?P<name>[0-9a-zA-Z()' -]+)/$", 'db.views.view_subgenre' ),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.htm'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.htm'}),
    url(r'^register/$', 'db.views.register'),
    url(r'^account/$', 'db.views.account'),
    url(r'^privacy-policy/$', 'db.views.privacy', name='privacy'),
    url(r'^contact/$', 'db.views.contact', name='contact'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
