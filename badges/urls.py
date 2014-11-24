from badges.views import BadgeList, BadgeViewSet, BadgeDetail, BadgeCreate, BadgeAppend, EvenimentViewSet, \
    EvenimentDetail, BadgeAproba, UpdateBadgeStatus
from django.conf.urls import patterns, include, url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'badges', BadgeViewSet)
router.register(r'evenimente', EvenimentViewSet)

urlpatterns = patterns('badges.views',
    url(r'api/1/badges/(?P<pk>\d+)/update/$', UpdateBadgeStatus.as_view(), name="badge_update"),
    url(r'api/1/', include(router.urls)),

    url(r'create/$', BadgeCreate.as_view(), name="badge_create"),
    url(r'append/(?P<pk>\d+)/$', BadgeAppend.as_view(), name="badge_append"),
    url(r'approve/$', BadgeAproba.as_view(), name="badge_aproba"),

    url(r'(?P<pk>\d+)/$', EvenimentDetail.as_view(), name="eveniment_detail"),
    url(r'$', BadgeList.as_view(), name="index"),
)
