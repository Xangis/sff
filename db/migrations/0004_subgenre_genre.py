# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20160514_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='subgenre',
            name='genre',
            field=models.IntegerField(default=0, choices=[(0, b'Science Fiction'), (1, b'Fantasy'), (2, b'Horror')]),
            preserve_default=False,
        ),
    ]
