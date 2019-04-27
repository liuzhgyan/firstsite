# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180304_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmaintaindtl',
            name='remark',
            field=models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
