# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_cards_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='card_hero_image',
            field=models.ImageField(help_text=b'Add', upload_to=b'Cards', null=True, verbose_name=b'Card display image', blank=True),
        ),
    ]
