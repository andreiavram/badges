from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from rest_framework import routers, serializers, viewsets
from badges.models import Badge
from badges.serializers import BadgeSerializer
from badges.forms import BadgeCreateForm


class BadgeList(TemplateView):
    template_name = "badges/badge_list.html"


class BadgeDetail(DetailView):
    template_name = "badges/badge_detail.html"
    model = Badge


class BadgeCreate(CreateView):
    template_name = "badges/badge_form.html"
    model = Badge
    form_class = BadgeCreateForm

## API
class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

