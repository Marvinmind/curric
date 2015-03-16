# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_auto_20150302_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='exclusive_subsections',
            field=models.ManyToManyField(null=True, blank=True, related_name='more_stuff', to='plan.Section'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='mandatory_subsections',
            field=models.ManyToManyField(null=True, blank=True, related_name='stuff', to='plan.Section'),
            preserve_default=True,
        ),
    ]
