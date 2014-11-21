from django.contrib.auth.models import User
from badges.models import Badge

__author__ = 'yeti'
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "full_name", "last_name", "first_name"]

    full_name = serializers.SerializerMethodField('get_full_name')

    def get_full_name(self, obj):
        return obj.get_full_name()


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge
        fields = ['nume_activitate', 'an_activitate', 'poster', 'amintire', 'timestamp', 'acceptate', 'imagine']

    poster = UserSerializer(many=False)

