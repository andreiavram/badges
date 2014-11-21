# coding: utf-8
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.widgets import PasswordInput

__author__ = 'yeti'


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        exclude = ('user', )

    email = EmailField(label=u"Email", help_text=u"Emailul va fi și username-ul tău.")
    parola = CharField(label=u"Parola", widget=PasswordInput)
    parola_verificare = CharField(label=u"Parola (verificare)", widget=PasswordInput)

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
