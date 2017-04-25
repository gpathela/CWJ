# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 23:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0002_jobstatus'),
        ('application', '0002_auto_20170420_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('saved_on', models.DateTimeField(default=datetime.datetime.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]