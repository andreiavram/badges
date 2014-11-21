#coding: utf-8
import datetime
from django.contrib.auth.models import User
from django.db import models


class Badge(models.Model):
    nume_activitate = models.CharField(max_length=255)
    an_activitate = models.IntegerField()
    poster = models.ForeignKey(User, null=True, blank=True)
    amintire = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    acceptat = models.BooleanField(default=False)
    acceptat_pe = models.DateTimeField(null=True, blank=True)
    acceptat_de = models.ForeignKey(User, null=True, blank=True, related_name="badgeuri_acceptate")

    imagine = models.ImageField(upload_to="badges")

    class Meta:
        verbose_name = "Propunere badge"
        verbose_name_plural = "Propuneri badge"
        ordering = ["-an_activitate"]

    def __unicode__(self):
        return u"{0}, {1}".format(self.nume_activitate, self.an_activitate)