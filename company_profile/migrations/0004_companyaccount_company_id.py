# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-09 05:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0003_auto_20171209_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyaccount',
            name='company_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
