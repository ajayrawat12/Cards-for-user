# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'', b'Others'), (b'M', b'Male'), (b'F', b'Female')])),
                ('likes_cheese', models.NullBooleanField(default=None, max_length=3, choices=[(None, b'Others'), (True, b'Male'), (False, b'Female')])),
                ('full_name', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('profile_picture', models.ImageField(upload_to=b'uploaded_files')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
