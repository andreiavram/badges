import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Badge(models.Model):
    nume_activitate = models.CharField(max_length=255)
    an_activitate = models.IntegerField()
    poster = models.ForeignKey(User)
    amintire = models.TextField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    acceptate = models.BooleanField(default=False)

    imagine = models.ImageField(upload_to="badges")

    def __unicode__(self):
        return u"{0}, {1}".format(self.nume_activitate, self.an_activitate)