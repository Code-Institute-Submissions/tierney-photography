# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-19 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_remove_orderlineitem_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='second_name',
            new_name='last_name',
        ),
    ]