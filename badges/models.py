#coding: utf-8
import datetime
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models
from imagekit.models.fields import ImageSpecField
from pilkit.processors.resize import ResizeToFill, SmartResize
import urllib

class Eveniment(models.Model):
    nume = models.CharField(max_length=255)
    an = models.IntegerField()

    class Meta:
        ordering = ["-an"]

    def __unicode__(self):
        return u"{0}, {1}".format(self.nume, self.an)

    @models.permalink
    def get_absolute_url(self):
        return ("badges:eveniment_detail", [], {"pk": self.id})

    def get_full_absolute_url(self):
        return "http://%s%s" % (Site.objects.get_current().domain, self.get_absolute_url())

    def facebook_share_link(self):
        base_url = "https://www.facebook.com/sharer/sharer.php?%s"
        return base_url % urllib.urlencode({"u": self.get_full_absolute_url()})

    def twitter_share_link(self):
        base_url = "https://twitter.com/share?%s"
        return base_url % urllib.urlencode({"url": self.get_full_absolute_url(), "text": self.__unicode__()})

    def get_badge_imagine_implicita(self):
        default = self.badge_set.filter(implicit_eveniment=True).first()
        if default is None:
            default = self.badge_set.filter(imagine__isnull=False).first()
        if default is None:
            return None

        if default.imagine:
            return default
        return None

    def imagine_mare(self):
        imagine = self.get_badge_imagine_implicita()
        return imagine.imagine_mare if imagine else None

    def imagine_thumbnail(self):
        imagine = self.get_badge_imagine_implicita()
        return imagine.imagine_thumbnail if imagine else None

    def posters(self):
        return self.badge_set.filter(poster__isnull=False).values_list("poster__id", flat=True)


class Badge(models.Model):
    poster = models.ForeignKey(User, null=True, blank=True)
    amintire = models.TextField(null=True, blank=True, verbose_name=u"Povestea badge-ului", help_text=u"Adică cum și de ce a ajuns la tine, ce amintiri ai din campul sau din acțiunea aia, cu cine erai acolo?")

    timestamp = models.DateTimeField(auto_now_add=True)
    acceptat = models.BooleanField(default=False)
    acceptat_pe = models.DateTimeField(null=True, blank=True)
    acceptat_de = models.ForeignKey(User, null=True, blank=True, related_name="badgeuri_acceptate")

    eveniment = models.ForeignKey("badges.Eveniment")
    implicit_eveniment = models.BooleanField(default=False)

    imagine = models.ImageField(upload_to="badges", verbose_name=u"Super-poză cu badge-ul", help_text=u"O poză de calitate cu o dimensiune justificată :)", null=True, blank=True)
    imagine_thumbnail = ImageSpecField(source='imagine', processors=[SmartResize(300, 300, False)],
                                      format='JPEG', options={'quality': 95})
    imagine_mare = ImageSpecField(source='imagine', processors=[SmartResize(1200, 1200, False)],
                                      format='JPEG', options={'quality': 95})

    class Meta:
        verbose_name = "Propunere badge"
        verbose_name_plural = "Propuneri badge"
        ordering = ["-timestamp"]

    def __unicode__(self):
        return u"{0}, {1}".format(self.eveniment.nume, self.eveniment.an)