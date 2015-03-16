# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='parent',
            field=models.ForeignKey(default=0, to='plan.Section'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='modules',
            field=models.ManyToManyField(to='plan.Module', null=True),
            preserve_default=True,
        ),
    ]
