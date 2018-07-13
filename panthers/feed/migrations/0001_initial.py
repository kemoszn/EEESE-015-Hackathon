# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('author', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=30)),
                ('date', models.DateTimeField()),
                ('department', models.CharField(max_length=10, choices=[('Electrical', 'electrical'), ('Civil', 'civil'), ('Chemical', 'chemical')])),
                ('place', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=250, unique_for_date='date')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('body', models.TextField(max_length=200)),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('publish', models.DateTimeField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('description', models.CharField(max_length=10, default='Global', choices=[('Electrical', 'electrical'), ('Civil', 'civil'), ('Chemical', 'chemical'), ('Global', 'global')])),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
