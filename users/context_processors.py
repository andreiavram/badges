from django.contrib.sites.models import Site

__author__ = 'yeti'

def url_root(request):
    return { "URL_ROOT" : Site.objects.get_current().domain }