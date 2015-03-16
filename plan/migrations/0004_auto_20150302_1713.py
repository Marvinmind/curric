# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20150301_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='exclusive_subsections',
            field=models.ManyToManyField(blank=True, default=0, null=True, related_name='exclusive_subsections_rel_+', to='plan.Section'),
            preserve_default=True,
        ),
    ]
