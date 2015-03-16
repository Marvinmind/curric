# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('credit_points', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModuleSelections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('module', models.ForeignKey(to='plan.Module')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('level', models.IntegerField()),
                ('exclusive_subsections', models.ManyToManyField(related_name='exclusive_subsections_rel_+', to='plan.Section')),
                ('mandatory_subsections', models.ManyToManyField(related_name='mandatory_subsections_rel_+', to='plan.Section')),
                ('modules', models.ManyToManyField(to='plan.Module')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Studyplan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('student', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='moduleselections',
            name='section',
            field=models.ForeignKey(to='plan.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moduleselections',
            name='studyplan',
            field=models.ForeignKey(to='plan.Studyplan'),
            preserve_default=True,
        ),
    ]
