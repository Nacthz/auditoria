# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificacion', '0016_auto_20161009_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificacion',
            name='preparacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='certificacion.Certificacion'),
            preserve_default=False,
        ),
    ]
