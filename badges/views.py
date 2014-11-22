# coding: utf-8
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from rest_framework import viewsets

from badges.models import Badge, Eveniment
from badges.serializers import BadgeSerializer
from badges.forms import BadgeCreateForm, BadgeEventCreateForm


class BadgeList(TemplateView):
    template_name = "badges/badge_list.html"


class BadgeDetail(DetailView):
    template_name = "badges/badge_detail.html"
    model = Badge


class BadgeCreate(CreateView):
    template_name = "badges/badge_form.html"
    model = Badge
    form_class = BadgeCreateForm
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BadgeCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)

        nume_eveniment = form.cleaned_data.get("nume_activitate")
        an_eveniment = form.cleaned_data.get("an_activitate")
        eveniment, created = Eveniment.objects.get_or_create(nume=nume_eveniment, an=an_eveniment)
        self.object.eveniment = eveniment
        if created:
            self.object.implicit_eveniment = True

        self.object.poster = self.request.user
        if self.request.user.utilizator.is_auto_approved:
            self.object.marcheaza_acceptat(self.request.user, save=False)
            messages.success(self.request, u"Povestea ta a fost adăugată și apare acum în colecția de badge-uri!")
        else:
            self.object.acceptat = False
            messages.success(self.request, u"Povestea ta a fost salvată și va apărea în colecția de badge-uri după ce este verificată de cineva din echipa noastră!")
        return super(BadgeCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse("badge:index")

    def get_context_data(self, **kwargs):
        data = super(BadgeCreate, self).get_context_data(**kwargs)
        data['titlu'] = u"Adaugă un badge și spune-i povestea"
        return data


class BadgeAppend(CreateView):
    template_name = "badges/badge_form.html"
    model = Badge
    form_class = BadgeEventCreateForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.event = get_object_or_404(Eveniment, id=kwargs.pop("pk"))
        return super(BadgeAppend, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.eveniment = self.event
        self.object.save()
        if self.request.user.utilizator.is_auto_approved:
            self.object.marcheaza_acceptat(self.request.user, save=False)
            messages.success(self.request, u"Povestea ta a fost adăugată celorlalte! Mulțumim!")
        else:
            self.object.acceptat = False
            messages.success(self.request, u"Povestea ta a fost salvată și va apărea în colecția de badge-uri după ce este verificată de cineva din echipa noastră!")
        return super(BadgeAppend, self).form_valid(form)

    def get_success_url(self):
        return reverse("badge:index")

    def get_context_data(self, **kwargs):
        data = super(BadgeAppend, self).get_context_data(**kwargs)
        data['titlu'] = u"Povestea ta de la %s" % self.event
        return data

## API
class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

