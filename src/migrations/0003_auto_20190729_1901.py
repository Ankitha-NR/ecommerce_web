# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-29 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20190729_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='storetable',
            name='salt',
            field=models.CharField(default=b'', max_length=18),
        ),
        migrations.AlterField(
            model_name='storetable',
            name='email_id',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='storetable',
            name='name',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='storetable',
            name='password',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
