from django.conf.urls.defaults import url, patterns

urlpattern=urlpattern('foodspot.views',
    url('^$/','main'),
    url('^profile$/','profile'),
    url('^order$/','order'),
)
