from django.conf.urls.defaults import url, patterns
from foodspot import views

urlpatterns=patterns('',
    url(r'^',views.main),
    url(r'^profile/','views.profile'),
    url(r'^order/','views.order'),
)
