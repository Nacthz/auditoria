# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='ejemplo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='comentario',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]