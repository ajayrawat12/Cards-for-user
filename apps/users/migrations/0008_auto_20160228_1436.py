# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160228_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'UserProfile', 'verbose_name_plural': 'UserProfiles'},
        ),
        migrations.AlterModelOptions(
            name='userprofileinfo',
            options={'verbose_name': 'UserProfileInfo', 'verbose_name_plural': "UserProfileInfo's"},
        ),
    ]
