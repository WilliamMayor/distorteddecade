from django.conf.urls import patterns, url

from www import views

urlpatterns = patterns('',
    url(r'^/$', views.index, name='index'),
    url(r'^bio/$', views.bio, name='bio'),
    url(r'^music/$', views.music, name='music'),
    url(r'^gigs/$', views.gigs, name='gigs'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
)
