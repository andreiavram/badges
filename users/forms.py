# coding: utf-8
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput
from django.forms.models import ModelForm, ModelChoiceField
from django.forms import CharField
from users.models import Utilizator

__author__ = 'yeti'


class RegistrationForm(ModelForm):
    class Meta:
        model = Utilizator
        exclude = ('user', 'is_auto_approved')

    email = EmailField(label=u"Email", help_text=u"Emailul va fi și username-ul tău.")
    parola = CharField(label=u"Parola", widget=PasswordInput)
    parola_verificare = CharField(label=u"Parola (verificare)", widget=PasswordInput)
    first_name = CharField(required=True, max_length=255, label=u"Prenume")
    last_name = CharField(required=True, max_length=255, label=u"Nume")

    def __init__(self, **kwargs):
        super(RegistrationForm, self).__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal"
        self.helper.form_method = "post"

        self.helper.layout = Layout(Div(Div(Field("oncr_id", ), css_class="col-md-4 col-xs-12"),
                                        Div(Field("first_name"), css_class="col-md-4 col-xs-12"),
                                        Div(Field("last_name"), css_class="col-md-4 col-xs-12"),
                                        css_class="row"),
                                    Div(Div(Field("porecla"), css_class="col-md-6 col-xs-12"),
                                        Div(Field("centrul_local"), css_class="col-md-6 col-xs-12"),
                                        css_class="row"),
                                    Div(Div(Field("email"), css_class="col-md-4 col-xs-12"),
                                        Div(Field("parola"), css_class="col-md-4 col-xs-12"),
                                        Div(Field("parola_verificare"), css_class="col-md-4 col-xs-12"),
                                        css_class="row"))

        self.helper.add_input(Submit("submit", "Trimite", css_class="btn btn-success pull-right"))
        self.helper.form_action = "."

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email is not None and User.objects.filter(username=email).exists():
            raise ValidationError(u"Adresa de email există deja, poate ți-ai făcut deja cont?")
        return email

    def clean(self):
        parola = self.cleaned_data.get("parola", "")
        parola_verificare = self.cleaned_data.get("parola_verificare", "")
        if not len(parola) or parola != parola_verificare:
            self._errors['parola'] = [u"Cele două parole nu sunt identice!"]
            self.cleaned_data["parola"] = None
            self.cleaned_data["parola_verificare"] = None
            raise ValidationError(u"Probleme verificare parole")

        return self.cleaned_data
