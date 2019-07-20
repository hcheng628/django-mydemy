# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-07-20 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_remove_userfavorite_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='type',
            field=models.CharField(choices=[('U', 'User'), ('S', 'System')], default='U', max_length=2, verbose_name='Notification Type'),
        ),
    ]
