# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=100)),
                ('description_text', models.CharField(max_length=2000)),
                ('address_text', models.CharField(max_length=100)),
                ('is_pet_friendly', models.BooleanField(default=False)),
                ('is_alcohol_friendly', models.BooleanField(default=False)),
                ('is_open_after_10pm', models.BooleanField(default=False)),
                ('is_bonfire_friendly', models.BooleanField(default=False)),
                ('is_good_for_surfing', models.BooleanField(default=False)),
                ('photo', models.ImageField(upload_to='beaches')),
            ],
        ),
    ]
