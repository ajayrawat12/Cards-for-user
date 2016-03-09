# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160228_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='joining_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
    ]
