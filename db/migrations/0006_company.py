# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20160514_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
