# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-06-30 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('college', 'College'), ('institution', 'Institution'), ('individual', 'Individual')], default='college', max_length=30, verbose_name='Organization Category'),
        ),
    ]
