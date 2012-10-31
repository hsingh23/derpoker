from django.conf.urls import patterns, include, url
urlpatterns = patterns('pokeviewer.views',
    url(r'^$', 'home'),
)
