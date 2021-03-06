# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-04-02 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quots', '0005_auto_20170402_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='in',
            name='answered',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quots.Outer'),
        ),
        migrations.AlterField(
            model_name='in',
            name='orderer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quots.Inner'),
        ),
        migrations.AlterField(
            model_name='out',
            name='handler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quots.Outer'),
        ),
        migrations.AlterField(
            model_name='out',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quots.In'),
        ),
    ]
