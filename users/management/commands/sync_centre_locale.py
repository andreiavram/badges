#coding: utf-8
from users.models import CentruLocal

__author__ = 'andrei'


from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        import requests
        import re

        s = requests.session()
        # r1 = s.get("https://www.oncr.ro/login")
        # login_data = {"_username": settings.ONCR_USER, "_password": settings.ONCR_PASSWORD}
        # regex = 'name="_csrf_token" value="([A-Za-z0-9_]*)"'
        # csrf = re.findall(regex, r1.text)
        #
        # if len(csrf) == 0:
        #     self.stdout.write("ERROR connecting to ONCR.ro")
        #
        # login_data['_csrf_token'] = csrf[0]
        #
        # r2 = s.post("https://www.oncr.ro/login_check", login_data)
        # # r3 = s.get("https://www.oncr.ro/%s.json", scout_id)

        urls = ["https://www.oncr.ro/local_center/center/datatable/0",
                 "https://www.oncr.ro/local_center/center/datatable/1"]

        for centre_locale_url in urls:
            r3 = s.get(centre_locale_url)
            if r3.status_code != 200:
                self.stdout.write("Error getting CL\n")

            new_groups = 0
            centre_locale = r3.json()
            for centru in centre_locale.get('aaData', []):
                list_number = centru[0]
                localitate = centru[1]
                nume = centru[2]
                judet = centru[3]
                membri = centru[4]
                activ_string = centru[5]
                link = centru[6]

                activ_translation = {"Activ" : "ok", "Suspendat": "suspendat", "Activ, cotizatie restanta": "probleme-cotizatie"}
                status_list = re.findall(r"<span class='label center-status-([\w]+)'>([\w]+)<\/span>", activ_string)
                if len(status_list):
                    activ = status_list[0][1]
                    # print "activ: %s\n" % activ

                link_id = re.findall(r"(\d+)", link)
                if len(link_id):
                    oncr_id = link_id[0]
                    # print "oncr id: %s\n" % oncr_id

                try:
                    centru_local = CentruLocal.objects.get(oncr_id=oncr_id)
                except CentruLocal.DoesNotExist, e:
                    centru_local = CentruLocal(oncr_id=int(oncr_id))
                    if centre_locale_url.endswith("0"):
                        centru_local.nivel = "cl"
                    else:
                        centru_local.nivel = "gi"
                    new_groups += 1

                centru_local.numar_cercetasi = membri
                centru_local.oncr_status = activ
                centru_local.localitate = localitate
                centru_local.nume = nume if nume != localitate else None
                centru_local.stare = activ_translation.get(activ, "ok")
                centru_local.save()

        self.stdout.write("Created %s Centre Locale\n" % new_groups)