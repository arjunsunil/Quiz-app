# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Correct_Ans',
            new_name='correct_answer',
        ),
    ]
