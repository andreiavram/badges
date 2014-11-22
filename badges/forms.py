#coding: utf-8
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div, Field, Submit
from django.core.exceptions import ValidationError
from django.forms.fields import CharField, IntegerField, ImageField
from django.forms.models import ModelForm
import datetime

from badges.models import Badge


__author__ = 'yeti'


class BadgeCreateForm(ModelForm):
    class Meta:
        model = Badge
        exclude = ("poster", "acceptat", "acceptat_pe", "acceptat_de", )

    nume_activitate = CharField(max_length=255, label=u"De unde e badge-ul?", help_text=u"În ce camp sau în ce context l-ai dobândit?")
    an_activitate = IntegerField(max_value=int(datetime.date.today().strftime("%Y")), min_value=1990, label=u"Anul")

    imagine = ImageField(label=u"Super poză cu badge-ul", help_text=u"O poză de calitate cu o dimensiune justificată :)", required=True)

    def __init__(self, **kwargs):
        super(BadgeCreateForm, self).__init__(**kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(Row(Div(Field("nume_activitate"), css_class="col-md-6 col-xs-12"),
                                        Div(Field("an_activitate"), css_class="col-md-2 col-xs-12"),
                                        Div(Field("imagine"), css_class="col-md-4 col-xs-12")),
                                    Row(Div(Field("amintire"), css_class="col-md-12 col-xs-12")))
        self.helper.add_input(Submit("submit", "Salvează", css_class="btn btn-success pull-right"))
        self.helper.form_action = "."
        self.helper.form_method = "post"
        self.helper.form_class = "form-horizontal"

    def clean_an_activitate(self):
        an = self.cleaned_data.get("an_activitate", 0)
        if an not in range(1990, 2015):
            raise ValidationError(u"Nu-i chiar posibil, nu?")


class BadgeEventCreateForm(ModelForm):
    class Meta:
        model = Badge
        fields = ("amintire", "imagine")

    def __init__(self, **kwargs):
        super(BadgeEventCreateForm, self).__init__(**kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(Row(Div(Field("amintire"), css_class="col-md-12 col-xs-12")),
                                    Row(Div(Field("imagine"), css_class="col-md-12 col-xs-12")))
        self.helper.add_input(Submit("submit", "Salvează", css_class="btn btn-success pull-right"))
        self.helper.form_action = "."
        self.helper.form_method = "post"
        self.helper.form_class = "form-horizontal"
