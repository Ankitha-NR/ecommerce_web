# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-29 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20190729_1907'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='users',
            table='user_table',
        ),
    ]
