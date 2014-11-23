#coding: utf-8
from badges.models import CentruLocal

__author__ = 'andrei'


from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        cls = CentruLocal.objects.all()

        from geopy import geocoders
        g = geocoders.GoogleV3()
        for cl in cls:
            #fixed_str = cl.localitate.lower().replace(u"ș", "s").replace(u"ț", "t").replace(u"ă", "a")
            #self.stdout.write(u"%s" % fixed_str.encode("utf-8"))
            self.stdout.write(cl.localitate.encode('utf-8'))
            try:
                place, (lat, lng) = g.geocode(cl.localitate.encode('utf-8'))
            except Exception, e:
                continue
            cl.geo_lat = lat
            cl.geo_long = lng
            cl.save()