# coding: utf-8
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from badges.models import Badge, Eveniment, BADGE_STATUSES
from badges.serializers import BadgeSerializer, EvenimentSerializer, PaginatedEvenimentSerializer, BadgeUpdateSerializer
from badges.forms import BadgeCreateForm, BadgeEventCreateForm


class BadgeList(TemplateView):
    template_name = "badges/badge_list.html"


class BadgeDetail(DetailView):
    template_name = "badges/eveniment_detail.html"
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
        # import pdb; pdb.set_trace()
        eveniment, created = Eveniment.objects.get_or_create(nume=nume_eveniment, an=an_eveniment)
        self.object.eveniment = eveniment
        if created:
            self.object.implicit_eveniment = True

        self.object.poster = self.request.user
        if self.request.user.utilizator.is_auto_approved:
            self.object.marcheaza_acceptat(self.request.user, save=False)
            messages.success(self.request, u"Povestea ta a fost adăugată și apare acum în colecția de badge-uri!")
        else:
            messages.success(self.request, u"Povestea ta a fost salvată și va apărea în colecția de badge-uri după ce este verificată de cineva din echipa noastră!")
        return super(BadgeCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse("badges:index")

    def get_context_data(self, **kwargs):
        data = super(BadgeCreate, self).get_context_data(**kwargs)
        data['titlu'] = u"Adaugă un badge și spune-i povestea"
        return data


class EvenimentDetail(DetailView):
    template_name = "badges/eveniment_detail.html"
    model = Eveniment


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
        self.object.poster = self.request.user
        if self.request.user.utilizator.is_auto_approved:
            self.object.marcheaza_acceptat(self.request.user, save=False)
            messages.success(self.request, u"Povestea ta a fost adăugată celorlalte! Mulțumim!")
        else:
            messages.success(self.request, u"Povestea ta a fost salvată și va apărea în colecția de badge-uri după ce este verificată de cineva din echipa noastră!")
        return super(BadgeAppend, self).form_valid(form)

    def get_success_url(self):
        return reverse("badges:index")

    def get_context_data(self, **kwargs):
        data = super(BadgeAppend, self).get_context_data(**kwargs)
        data['titlu'] = u"Povestea ta de la %s" % self.event
        return data


class BadgeAproba(ListView):
    model = Badge
    template_name = "badges/badge_approve_list.html"

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        self.status = int(request.GET.get("status", 1))
        if self.status not in [a[0] for a in BADGE_STATUSES]:
            self.status = 1
        return super(BadgeAproba, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(BadgeAproba, self).get_queryset()
        qs = qs.filter(acceptat_status=self.status)
        return qs

    def get_context_data(self, **kwargs):
        data = super(BadgeAproba, self).get_context_data(**kwargs)
        data['statuses'] = BADGE_STATUSES
        data['current_status'] = self.status
        data['current_status_name'] = next((a[1] for a in BADGE_STATUSES if a[0] == self.status))
        return data

## API
class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.filter(acceptat_status=2)
    serializer_class = BadgeSerializer


class EvenimentViewSet(viewsets.ModelViewSet):
    queryset = Eveniment.objects.filter(badge__acceptat_status=2).annotate(num_badges=Count('badge')).filter(num_badges__gte=0)
    serializer_class = EvenimentSerializer


class UpdateBadgeStatus(UpdateAPIView):
    model = Badge
    model_serializer_class = BadgeUpdateSerializer
    permission_classes = [IsAdminUser, ]





