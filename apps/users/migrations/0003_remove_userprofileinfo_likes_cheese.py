# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='likes_cheese',
        ),
    ]
