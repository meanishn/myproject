# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='employee',
            field=models.ForeignKey(related_name='works', to='employer.Employee'),
            preserve_default=True,
        ),
    ]
