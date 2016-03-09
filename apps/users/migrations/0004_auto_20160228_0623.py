# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_userprofileinfo_likes_cheese'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'O', b'Others'), (b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
