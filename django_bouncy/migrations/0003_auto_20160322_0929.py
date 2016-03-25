# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_bouncy', '0002_auto_20150927_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounce',
            name='action',
            field=models.CharField(null=True, blank=True, verbose_name='Action', max_length=150, db_index=True),
        ),
        migrations.AlterField(
            model_name='bounce',
            name='bounce_subtype',
            field=models.CharField(verbose_name='Bounce Subtype', max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='bounce',
            name='bounce_type',
            field=models.CharField(verbose_name='Bounce Type', max_length=50, db_index=True),
        ),
        migrations.AlterField(
            model_name='bounce',
            name='feedback_timestamp',
            field=models.DateTimeField(verbose_name='Feedback Time'),
        ),
        migrations.AlterField(
            model_name='bounce',
            name='hard',
            field=models.BooleanField(verbose_name='Hard Bounce', db_index=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='feedback_timestamp',
            field=models.DateTimeField(verbose_name='Feedback Time'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='feedback_type',
            field=models.CharField(null=True, blank=True, verbose_name='Complaint Type', max_length=150, db_index=True),
        ),
    ]
