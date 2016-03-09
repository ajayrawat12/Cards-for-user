# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160228_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'Others', b'Others'), (b'Male', b'Male'), (b'Female', b'Female')]),
        ),
    ]
