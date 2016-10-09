# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificacion', '0015_auto_20161006_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificacion',
            name='preparacion',
        ),
        migrations.AddField(
            model_name='control',
            name='ayuda',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='titulo',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
