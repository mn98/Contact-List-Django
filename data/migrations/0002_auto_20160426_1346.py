# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('PRD', 'Production'), ('DEV', 'Development'), ('PR', 'Public Relations'), ('HR', 'Human Resources'), ('FIN', 'Finance')], max_length=3),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='title',
            field=models.CharField(choices=[('MR', 'Mr'), ('MIS', 'Miss'), ('MRS', 'Mrs'), ('MS', 'Ms')], max_length=3),
        ),
    ]
