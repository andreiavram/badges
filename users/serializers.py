from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from users.models import Utilizator, CentruLocal

__author__ = 'yeti'


class CentruLocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CentruLocal
        fields = ["nume", "localitate"]


class UtilizatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Utilizator
        fields = ["centrul_local", "porecla", "is_auto_approved"]

    centrul_local = CentruLocalSerializer(many=False)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "full_name", "last_name", "first_name", "id", "profile", "evenimente"]

    full_name = serializers.SerializerMethodField("get_full_name")
    profile = serializers.SerializerMethodField("get_utilizator")
    evenimente = serializers.SerializerMethodField("get_evenimente")

    def get_full_name(self, obj):
        return obj.get_full_name()

    def get_utilizator(self, obj):
        return UtilizatorSerializer(obj.utilizator).data

    def get_evenimente(self, obj):
        return obj.badge_set.all().values_list("eveniment__id", flat=True).distinct().order_by("eveniment__id")