from badges.views import BadgeList, BadgeViewSet, BadgeDetail, BadgeCreate, BadgeAppend
from django.conf.urls import patterns, include, url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'badges', BadgeViewSet)

urlpatterns = patterns('badges.views',
    url(r'api/1/', include(router.urls)),

    url(r'create/$', BadgeCreate.as_view(), name="badge_create"),
    url(r'append/(?P<pk>\+d)/$', BadgeAppend.as_view(), name="badge_append"),
    url(r'(?P<pk>\d+)/$', BadgeDetail.as_view(), name="badge_detail"),
    url(r'$', BadgeList.as_view(), name="index"),
)
