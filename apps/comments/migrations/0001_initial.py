# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_auto_20160228_1857'),
        ('users', '0009_auto_20160228_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.TextField(help_text=b'You can give your thoughts for the card.', null=True, verbose_name=b'Comments', blank=True)),
                ('cards', models.ForeignKey(to='cards.Cards')),
                ('user_profile', models.ForeignKey(to='users.UserProfile')),
            ],
        ),
    ]
