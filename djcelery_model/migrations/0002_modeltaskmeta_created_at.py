# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('djcelery_model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltaskmeta',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 3, 23, 54, 463935, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
