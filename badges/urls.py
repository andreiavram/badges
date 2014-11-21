from badges.views import BadgeList, BadgeViewSet, BadgeDetail
from django.conf.urls import patterns, include, url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'badges', BadgeViewSet)

urlpatterns = patterns('badges.views',
    # url(r'(?P<pk>\d+)/$', BadgeDetail.as_view(), name="badge_detail"),
    url(r'api/1/', include(router.urls)),

    url(r'(?P<pk>\d+)/$', BadgeDetail.as_view(), name="badge-detail"),
    url(r'$', BadgeList.as_view(), name="index"),
)
