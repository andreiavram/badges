from django.contrib.auth.models import User
from badges.models import Badge
from users.serializers import UserSerializer
from rest_framework import routers, serializers, viewsets

__author__ = 'yeti'



class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge
        fields = ['nume_activitate', 'an_activitate', 'poster', 'amintire', 'timestamp', 'acceptat', 'imagine']

    poster = UserSerializer(many=False)

