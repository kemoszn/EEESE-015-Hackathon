# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_event_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='approved',
        ),
    ]
