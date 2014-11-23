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
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amintire', models.TextField(help_text='Adic\u0103 cum \u0219i de ce a ajuns la tine, ce amintiri ai din campul sau din ac\u021biunea aia, cu cine erai acolo?', null=True, verbose_name='Povestea badge-ului', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('acceptat', models.BooleanField(default=False)),
                ('acceptat_pe', models.DateTimeField(null=True, blank=True)),
                ('implicit_eveniment', models.BooleanField(default=False)),
                ('imagine', models.ImageField(help_text='O poz\u0103 de calitate cu o dimensiune justificat\u0103 :)', upload_to=b'badges', verbose_name='Super-poz\u0103 cu badge-ul')),
                ('acceptat_de', models.ForeignKey(related_name='badgeuri_acceptate', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-eveniment__an'],
                'verbose_name': 'Propunere badge',
                'verbose_name_plural': 'Propuneri badge',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Eveniment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nume', models.CharField(max_length=255)),
                ('an', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='badge',
            name='eveniment',
            field=models.ForeignKey(to='badges.Eveniment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='badge',
            name='poster',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
