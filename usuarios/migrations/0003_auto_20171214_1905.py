# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-14 19:05
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20171214_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, default='/static/img/default/defaultProfile.png', storage=django.core.files.storage.FileSystemStorage(location='/media/'), upload_to=b''),
        ),
    ]