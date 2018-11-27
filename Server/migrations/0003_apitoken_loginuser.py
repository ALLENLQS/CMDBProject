# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0002_auto_20181113_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiToken',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=32, verbose_name='token值')),
                ('time', models.DateTimeField(verbose_name='生成时间')),
                ('user_id', models.CharField(max_length=32, verbose_name='token用户')),
            ],
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, verbose_name='用户')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
    ]
