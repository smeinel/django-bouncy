# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_bouncy', '0004_missing_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounce',
            name='feedback_timestamp',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Feedback Time'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='feedback_timestamp',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Feedback Time'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='feedback_timestamp',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Feedback Time'),
        ),
    ]
