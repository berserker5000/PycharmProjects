# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ArticleName', models.CharField(max_length=150)),
                ('ArticleBody', models.TextField()),
            ],
        ),
    ]
