from django.conf.urls import url, patterns


urlpatterns=patterns('foodspot',
                     url(r'^$','views.main', name="main"),
                     url(r'^profile/','views.profile', name="profile"),
                     url(r'^order/','views.order', name="order"),
)
