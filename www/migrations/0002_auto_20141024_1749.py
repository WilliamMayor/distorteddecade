# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='more',
            field=models.URLField(verbose_name=b'More info URL', blank=True),
            preserve_default=True,
        ),
    ]
