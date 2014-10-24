# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20141024_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('intro', models.TextField()),
                ('active', models.BooleanField(default=False, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
