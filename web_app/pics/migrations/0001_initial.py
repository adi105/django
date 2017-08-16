# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(max_length=100)),
                ('dslr', models.BooleanField(default=True)),
                ('folder_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('photo_name', models.CharField(max_length=100)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pics.Folder')),
            ],
        ),
    ]