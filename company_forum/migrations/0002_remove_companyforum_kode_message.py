# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyforum',
            name='kode_message',
        ),
    ]