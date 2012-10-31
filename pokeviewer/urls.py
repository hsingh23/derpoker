from django.conf.urls import patterns, include, url
urlpatterns = patterns('pokeviewer.views',
    url(r'^$', 'home'),
)

urlpatterns += patterns(”,
  (r’^static/(?P.*)$’, ‘django.views.static.serve’, {‘document_root’: settings.STATIC_ROOT}),
)
