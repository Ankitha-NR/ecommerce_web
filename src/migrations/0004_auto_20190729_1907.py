# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-29 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20190729_1901'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='storetable',
            new_name='users',
        ),
    ]
