# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-18 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_merge'),
        ('dtm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_id', models.CharField(max_length=1024)),
                ('name', models.CharField(max_length=1024)),
                ('student', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='scheduleshare',
            name='gcal_ids',
        ),
        migrations.AddField(
            model_name='scheduleshare',
            name='start_day',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='scheduleshare',
            name='google_calendars',
            field=models.ManyToManyField(blank=True, to='dtm.GoogleCalendar'),
        ),
    ]