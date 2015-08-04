# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0002_auto_20150804_0100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name_plural': 'Coaches'},
        ),
    ]
