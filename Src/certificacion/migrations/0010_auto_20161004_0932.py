# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificacion', '0009_auto_20161004_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certificacion.Master'),
        ),
    ]
