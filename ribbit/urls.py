from django.conf.urls import patterns, include, url
from ribbit_app import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ribbit.views.home', name='home'),
    # url(r'^ribbit/', include('ribbit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^ribbits$', views.public, name='public'),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^admin/', include(admin.site.urls)),
)
