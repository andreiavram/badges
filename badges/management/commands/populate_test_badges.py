# coding: utf-8
from django.contrib.auth.models import User
from badges.models import Eveniment, Badge
from users.models import Utilizator, CentruLocal
import random
import string
from loremipsum import get_sentences
__author__ = 'andrei'


from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        #   first, create test users
        rand_len = lambda: random.randint(4, 12)
        rand_string = lambda: ''.join(random.choice(string.ascii_lowercase) for i in range(rand_len()))
        # for i in range(1, 6):
        #     ukwargs = dict(
        #         centrul_local = CentruLocal.objects.order_by('?')[0],
        #         porecla = rand_string(),
        #         first_name = rand_string(),
        #         last_name = rand_string(),
        #         oncr_id = "AA147")
        #
        #     u = Utilizator.objects.create(**ukwargs)
        #     email = "user%d@albascout.ro" % i
        #     user = User.objects.create_user(username=email, email=email, first_name=ukwargs.get("first_name"),
        #                                  last_name=ukwargs.get("last_name"), password="test123.")
        #     u.user = user
        #     u.save()

        import os
        base_path = os.path.join(settings.MEDIA_ROOT, "badges")
        files = [f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))]

        #   generate badges and events
        for i in range(1, 60):
            event = Eveniment.objects.create(nume=rand_string(), an=random.randint(1996, 2015))
            user = User.objects.filter(username__startswith="user").order_by('?')[0]
            amintire = " ".join(get_sentences(rand_len()))
            implicit_eveniment = True
            imagine = "badges/%s" % files[random.randint(0, len(files) - 1)]
            Badge.objects.create(poster=user, amintire=amintire, implicit_eveniment=True,
                                 eveniment=event, imagine=imagine)