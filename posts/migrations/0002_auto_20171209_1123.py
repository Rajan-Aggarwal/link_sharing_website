# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='vote_count',
            field=models.IntegerField(default=1),
        ),
    ]