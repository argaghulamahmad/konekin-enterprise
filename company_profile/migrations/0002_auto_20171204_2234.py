# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyaccount',
            name='company_website',
            field=models.URLField(),
        ),
    ]