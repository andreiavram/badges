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
                ('nume_activitate', models.CharField(max_length=255)),
                ('an_activitate', models.IntegerField()),
                ('amintire', models.TextField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('acceptate', models.BooleanField(default=False)),
                ('imagine', models.ImageField(upload_to=b'badges')),
                ('poster', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
