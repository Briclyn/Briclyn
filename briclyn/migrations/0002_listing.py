# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briclyn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(blank=True, max_length=100)),
                ('customer_type', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(blank=True, max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('baths', models.IntegerField(default=0)),
                ('area', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
