from django.contrib.auth.models import User
from rest_framework.fields import ImageField
from rest_framework.pagination import PaginationSerializer
from badges.models import Badge, Eveniment
from users.serializers import UserSerializer
from rest_framework import routers, serializers, viewsets
from time import mktime

__author__ = 'yeti'


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge
        fields = ['poster', 'amintire', 'timestamp', 'acceptat', 'imagine', 'imagine_thumbnail', 'timestamp_processed']

    poster = UserSerializer(many=False)
    imagine_thumbnail = serializers.SerializerMethodField("get_imagine_thumbnail")
    timestamp_processed = serializers.SerializerMethodField("get_timestamp_processed")

    def get_imagine_thumbnail(self, obj):
        if obj.imagine:
            return obj.imagine_thumbnail.url
        return None

    def get_timestamp_processed(self, obj):
        return mktime(obj.timestamp.timetuple())

class EvenimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eveniment
        fields = ["nume", "an", "badges", "imagine", "poveste", "id", "facebook_link", "twitter_link"]

    badges = serializers.SerializerMethodField("get_badges")
    imagine = serializers.SerializerMethodField("get_default_image")
    poveste = serializers.SerializerMethodField("get_display_story")
    facebook_link = serializers.SerializerMethodField("get_facebook_share_link")
    twitter_link = serializers.SerializerMethodField("get_twitter_share_link")

    def get_facebook_share_link(self, obj):
        return obj.facebook_share_link()

    def get_twitter_share_link(self, obj):
        return obj.twitter_share_link()

    def get_badges(self, obj):
        return BadgeSerializer(obj.badge_set.all(), many=True).data

    def get_default_image(self, obj):
        default = obj.get_badge_imagine_implicita()
        if default:
            return default.imagine_thumbnail.url
        return None

    def get_display_story(self, obj):
        badge = obj.badge_set.all().order_by("-timestamp").first()
        return BadgeSerializer(badge).data


class PaginatedEvenimentSerializer(PaginationSerializer):
    class Meta:
        object_serializer_class = EvenimentSerializer