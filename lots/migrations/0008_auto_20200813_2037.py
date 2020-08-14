# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-13 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0007_auction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='lot',
        ),
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lots.Auction'),
        ),
    ]
