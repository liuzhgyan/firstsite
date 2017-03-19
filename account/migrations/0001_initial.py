# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chandate', models.CharField(max_length=8, verbose_name='\u65e5\u671f')),
                ('chantype', models.CharField(max_length=10, verbose_name='\u7c7b\u578b')),
                ('chanflag', models.CharField(max_length=1, verbose_name='\u6536\u652f\u6807\u5fd7')),
                ('amt', models.IntegerField(verbose_name='\u91d1\u989d')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('regdate', models.DateTimeField(null=True, verbose_name='\u767b\u8bb0\u65f6\u95f4', blank=True)),
            ],
            options={
                'ordering': ['-chandate'],
                'verbose_name': '\u6536\u652f\u8bb0\u5f55',
            },
        ),
    ]
