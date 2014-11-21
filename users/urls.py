from django.conf.urls import patterns, include, url
from users.views import Register

urlpatterns = patterns('badges.views',
    url(r'register/', Register.as_view(), name="register"),
)
