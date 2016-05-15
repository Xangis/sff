# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20160515_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='distribution_company',
            field=models.ForeignKey(blank=True, to='db.Company', null=True),
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='distribution_company',
            field=models.ForeignKey(blank=True, to='db.Company', null=True),
        ),
    ]
