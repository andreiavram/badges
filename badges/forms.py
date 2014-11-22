#coding: utf-8
from django.contrib.auth.models import User
from django.forms.models import ModelForm, ModelChoiceField
from django.forms import CharField
from badges.models import Badge

__author__ = 'yeti'


class BadgeCreateForm(ModelForm):
    class Meta:
        model = Badge
        exclude = ("poster", "acceptat", "acceptat_pe", "acceptat_de", )

    def __init__(self, **kwargs):
        super(BadgeCreateForm, self).__init__(**kwargs)

