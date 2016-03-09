# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20160228_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='card_created_on',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
        ),
    ]
