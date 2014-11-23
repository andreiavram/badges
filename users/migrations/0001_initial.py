# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CentruLocal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nume', models.CharField(max_length=200, null=True, blank=True)),
                ('localitate', models.CharField(max_length=200)),
                ('specific', models.CharField(blank=True, max_length=300, null=True, choices=[(b'catolic', b'Catolic'), (b'marinaresc', b'Marin\xc4\x83resc'), (b'traditional', b'Tradi\xc8\x9bional')])),
                ('stare', models.CharField(max_length=100, choices=[(b'ok', 'La zi'), (b'probleme-cotizatie', 'Probleme cotiza\u021bie'), (b'suspendat', 'Suspendat'), (b'propus-desfiintare', 'Propus pentru desfiin\u021bare'), (b'desfiintat', 'Desfiin\u021bat')])),
                ('nivel', models.CharField(default=b'cl', max_length=255, choices=[(b'gi', 'Grup de ini\u021biativ\u0103'), (b'gi-old', 'Grup de ini\u021biativ\u0103 > 6 luni'), (b'cl', b'Centru Local')])),
                ('nume_sef_centru', models.CharField(max_length=255, null=True, blank=True)),
                ('geo_lat', models.FloatField(null=True, blank=True)),
                ('geo_long', models.FloatField(null=True, blank=True)),
                ('oncr_id', models.IntegerField(default=0, null=True, verbose_name=b'ONCR ID', blank=True)),
                ('numar_cercetasi', models.IntegerField(default=0)),
                ('oncr_status', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ['localitate'],
                'verbose_name': 'Centru Local',
                'verbose_name_plural': 'Centre Locale',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Utilizator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porecla', models.CharField(help_text="Dac\u0103 ai un 'nume de cerceta\u0219' dup\u0103 care e\u0219ti cunoscut", max_length=255, null=True, blank=True)),
                ('oncr_id', models.CharField(help_text='ID-ul t\u0103u de cerceta\u0219, de la oncr.ro', max_length=10, null=True, verbose_name='ID ONCR', blank=True)),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name='Nume', blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, verbose_name='Prenume', blank=True)),
                ('is_auto_approved', models.BooleanField(default=False, verbose_name='Este aprobat automat')),
                ('centrul_local', models.ForeignKey(blank=True, to='users.CentruLocal', null=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
