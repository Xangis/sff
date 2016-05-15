# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_auto_20160515_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='writers',
            field=models.ManyToManyField(related_name='episode_writers', to='db.Person', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='producer',
            field=models.ManyToManyField(related_name='movie_producer', to='db.Person', blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writers',
            field=models.ManyToManyField(related_name='movie_writers', to='db.Person', blank=True),
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='creators',
            field=models.ManyToManyField(related_name='tvseries_creators', to='db.Person', blank=True),
        ),
    ]
