# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(max_length=40, verbose_name='openid')),
                ('nickname', models.CharField(max_length=40, null=True, verbose_name='nickname')),
                ('subscribe', models.CharField(max_length=1, null=True, verbose_name='subscribe')),
                ('sex', models.CharField(max_length=1, null=True, verbose_name='sex')),
                ('city', models.CharField(max_length=20, null=True, verbose_name='city')),
                ('country', models.CharField(max_length=20, null=True, verbose_name='country')),
                ('province', models.CharField(max_length=20, null=True, verbose_name='province')),
                ('language', models.CharField(max_length=10, null=True, verbose_name='language')),
                ('headimgurl', models.CharField(max_length=200, null=True, verbose_name='headimgurl')),
                ('subscribe_time', models.CharField(max_length=20, null=True, verbose_name='subscribe_time')),
                ('unionid', models.CharField(max_length=40, null=True, verbose_name='unionid')),
                ('remark', models.CharField(max_length=20, null=True, verbose_name='remark')),
                ('groupid', models.CharField(max_length=2, null=True, verbose_name='groupid')),
                ('update_time', models.DateTimeField(null=True, verbose_name='update time')),
            ],
            options={
                'ordering': ['openid'],
                'verbose_name': 'My User',
            },
        ),
    ]
