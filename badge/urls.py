from django.conf.urls import patterns, include, url
from django.contrib import admin
from users import urls as user_urls
from badges import urls as badges_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'badge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include(user_urls, namespace="users")),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^', include(badges_urls, namespace='badges'))
)