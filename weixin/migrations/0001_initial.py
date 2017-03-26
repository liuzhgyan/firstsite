# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appid', models.CharField(max_length=20, verbose_name='appID')),
                ('appsecret', models.CharField(max_length=100, verbose_name='appsecret')),
                ('access_token', models.CharField(max_length=200, null=True, verbose_name='access token')),
                ('last_access_token', models.CharField(max_length=200, null=True, verbose_name='last access token')),
                ('update_time', models.DateTimeField(null=True, verbose_name='update time')),
                ('expires_in', models.IntegerField(null=True, verbose_name='expires in')),
            ],
            options={
                'ordering': ['appid'],
                'verbose_name': 'App Token',
            },
        ),
    ]
