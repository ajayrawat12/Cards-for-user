# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_auto_20160228_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='card_created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date published'),
        ),
    ]
