#coding: utf-8
import datetime
from django.contrib.auth.models import User
from django.db import models


class Eveniment(models.Model):
    nume = models.CharField(max_length=255)
    an = models.IntegerField()

    def __unicode__(self):
        return u"{0}, {1}".format(self.nume, self.an)


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

    class Meta:
        verbose_name = "Propunere badge"
        verbose_name_plural = "Propuneri badge"
        ordering = ["-eveniment__an"]

    def __unicode__(self):
        return u"{0}, {1}".format(self.nume_activitate, self.an_activitate)