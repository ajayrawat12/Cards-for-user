# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20160228_0751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cards',
            options={'verbose_name': 'Cards', 'verbose_name_plural': 'Cards'},
        ),
    ]
