# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_subgenre_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subgenre',
            options={'ordering': ('genre', 'name')},
        ),
        migrations.AlterField(
            model_name='movie',
            name='subgenre',
            field=models.ForeignKey(blank=True, to='db.Subgenre', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='subgenre',
            field=models.ForeignKey(blank=True, to='db.Subgenre', null=True),
            preserve_default=True,
        ),
    ]
