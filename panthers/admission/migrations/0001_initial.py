# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('index', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('Request', models.TextField(max_length=140)),
            ],
        ),
    ]
