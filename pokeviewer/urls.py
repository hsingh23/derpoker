from django.conf.urls import patterns, include, url
urlpatterns = patterns('pokeviewer.views',
    url(r'^$', 'home'),
)

if not settings.DEBUG:
  urlpatterns += patterns('',
      (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
      )
