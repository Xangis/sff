# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_auto_20160515_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='founded',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
