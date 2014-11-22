from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

__author__ = 'yeti'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "full_name", "last_name", "first_name"]

    full_name = serializers.SerializerMethodField('get_full_name')

    def get_full_name(self, obj):
        return obj.get_full_name()