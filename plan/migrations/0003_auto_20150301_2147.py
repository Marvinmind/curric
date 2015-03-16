# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_auto_20150301_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='credit_points',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=200, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='module',
            name='number',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='moduleselections',
            name='module',
            field=models.ForeignKey(null=True, to='plan.Module', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='moduleselections',
            name='section',
            field=models.ForeignKey(null=True, to='plan.Section', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='moduleselections',
            name='studyplan',
            field=models.ForeignKey(null=True, to='plan.Studyplan', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='exclusive_subsections',
            field=models.ManyToManyField(related_name='exclusive_subsections_rel_+', to='plan.Section', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='level',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='mandatory_subsections',
            field=models.ManyToManyField(related_name='mandatory_subsections_rel_+', to='plan.Section', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='modules',
            field=models.ManyToManyField(to='plan.Module', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=200, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='parent',
            field=models.ForeignKey(null=True, to='plan.Section', blank=True),
            preserve_default=True,
        ),
    ]
