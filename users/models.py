# coding: utf-8
from django.db import models

# Create your models here.
NIVEL_CENTRU = (('gi', u'Grup de inițiativă'), ('gi-old', u'Grup de inițiativă > 6 luni'), ('cl', 'Centru Local'))
STARE_CENTRU = (('ok', u'La zi'), ('probleme-cotizatie', u'Probleme cotizație'), ('suspendat', u'Suspendat'),
                ('propus-desfiintare', u'Propus pentru desființare'), ('desfiintat', u'Desființat'),)
SPECIFICE_CENTRE_LOCALE = (("catolic", "Catolic"), ("marinaresc", "Marinăresc"), ("traditional", "Tradițional"))


class CentruLocal(models.Model):
    """
    Centru Local al ONCR, cu suport pentru specificul garantat prin statut.
    @todo: campul 'stare' trebuie sa devina un camp urmarit, nu un camp static
    @todo: campul 'adresa_tmp' trebuie sa treaca in ContactInfo
    """

    nume = models.CharField(max_length=200, blank=True, null=True)
    localitate = models.CharField(max_length=200)

    specific = models.CharField(max_length=300, choices=SPECIFICE_CENTRE_LOCALE, blank=True, null=True)
    stare = models.CharField(max_length=100, choices=STARE_CENTRU)
    nivel = models.CharField(max_length=255, choices=NIVEL_CENTRU, default="cl")

    nume_sef_centru = models.CharField(max_length=255, null=True, blank=True)

    geo_lat = models.FloatField(null = True, blank = True)
    geo_long = models.FloatField(null = True, blank = True)

    oncr_id = models.IntegerField(default=0, null=True, blank=True, verbose_name="ONCR ID")
    numar_cercetasi = models.IntegerField(default=0)
    oncr_status = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['localitate']
        verbose_name = "Centru Local"
        verbose_name_plural = "Centre Locale"

    def __unicode__(self):
        return self.nume_complet

    def _get_nume(self):
        """
        Obține numele de referință al Centrului Local, cu nume, dacă există, și cu localitatea
        """

        if self.nume is not None:
            ret = self.nume + " " + self.localitate
            return ret.strip()
        else:
            return self.localitate

    nume_complet = property(_get_nume)

    def _tip_specific(self):
        """
        Obține specificul Centrului Local
        """

        if self.specific is not None:
            return self.get_specific_display()
        else:
            return "General"

    tip_specific = property(_tip_specific)


class Utilizator(models.Model):
    user = models.OneToOneField("auth.User", null=True, blank=True)
    centrul_local = models.ForeignKey("badges.CentruLocal", null=True, blank=True)
    porecla = models.CharField(max_length=255, null=True, blank=True)
    oncr_id = models.CharField(max_length=10, null=True, blank=True)

    #   we might want to allow anonymous users
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
