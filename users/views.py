# coding: utf-8
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response

from users.forms import RegistrationForm
from users.models import Utilizator
from users.serializers import UserSerializer


class Register(CreateView):
    model = Utilizator
    form_class = RegistrationForm
    template_name = "users/registration_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        email = form.cleaned_data.get("email")
        parola = form.cleaned_data.get("parola")

        user_kwdict = dict(username=email, email=email, first_name=self.object.first_name,
                           last_name=self.object.last_name, is_active=True)
        user = User.objects.create(**user_kwdict)
        user.set_password(parola)
        user.save()

        self.object.user = user
        self.object.save()

        authed_user = authenticate(username=email, password=parola)
        if authed_user:
            login(self.request, authed_user)
        else:
            messages.error(self.request, u"Există o problemă cu crearea contului tău. Ia legătura cu andrei.avram@albascout.ro")

        return super(Register, self).form_valid(form)

    def get_success_url(self):
        return reverse("badges:badge_create")


class CurrentUserAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    model = User

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated():
            return self.request.user
        return None


