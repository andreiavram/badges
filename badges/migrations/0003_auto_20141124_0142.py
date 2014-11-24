# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0002_auto_20141122_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='badge',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Propunere badge', 'verbose_name_plural': 'Propuneri badge'},
        ),
        migrations.AlterModelOptions(
            name='eveniment',
            options={'ordering': ['-an']},
        ),
        migrations.RemoveField(
            model_name='badge',
            name='acceptat',
        ),
        migrations.AddField(
            model_name='badge',
            name='acceptat_status',
            field=models.IntegerField(default=1, choices=[(1, 'Indecis'), (2, 'Acceptat'), (3, 'Respins')]),
            preserve_default=True,
        ),
    ]
