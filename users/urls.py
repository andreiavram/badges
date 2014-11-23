from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from users.forms import LoginForm

from users.views import Register, CurrentUserAPIView
from django.contrib.auth import views as auth_views

urlpatterns = patterns('users.views',
    url(r'login/$', auth_views.login, {'template_name': 'users/login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'logout/$', auth_views.logout, {'next_page': reverse_lazy("badges:index")}, name="logout"),
    url(r'register/$', Register.as_view(), name="register"),
    url(r'api/1/utilizatori/get_current/$', CurrentUserAPIView.as_view(), name="current_user")
)
