# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizator',
            name='centrul_local',
            field=models.ForeignKey(blank=True, to='users.CentruLocal', help_text='Op\u021bional, dac\u0103 Centru t\u0103u Local nu mai exist\u0103', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='utilizator',
            name='oncr_id',
            field=models.CharField(help_text='ID-ul t\u0103u de cerceta\u0219, de la oncr.ro (op\u021bional)', max_length=10, null=True, verbose_name='ID ONCR', blank=True),
            preserve_default=True,
        ),
    ]
