# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarMaintainDtl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_name', models.CharField(max_length=200, verbose_name='\u4f5c\u4e1a\u9879\u76ee')),
                ('job_type', models.CharField(max_length=20, null=True, verbose_name='\u64cd\u4f5c\u7c7b\u578b', blank=True)),
                ('count', models.IntegerField(verbose_name='\u6570\u91cf')),
                ('amount', models.IntegerField(verbose_name='\u8d39\u7528')),
                ('mileage', models.IntegerField(verbose_name='\u91cc\u7a0b')),
                ('work_date', models.DateField(verbose_name='\u4fdd\u517b\u65e5\u671f')),
                ('remark', models.CharField(max_length=200, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'ordering': ['-mileage', 'job_type', 'job_name'],
                'verbose_name': '\u6c7d\u8f66\u4fdd\u517b\u660e\u7ec6',
            },
        ),
    ]
