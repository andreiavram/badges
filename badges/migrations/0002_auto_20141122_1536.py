# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='imagine',
            field=models.ImageField(help_text='O poz\u0103 de calitate cu o dimensiune justificat\u0103 :)', upload_to=b'badges', null=True, verbose_name='Super-poz\u0103 cu badge-ul', blank=True),
            preserve_default=True,
        ),
    ]
