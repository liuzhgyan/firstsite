# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_carmaintaindtl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmaintaindtl',
            name='job_type',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='\u64cd\u4f5c\u7c7b\u578b', choices=[('1', '\u5de5\u8d39'), ('2', '\u96f6\u4ef6')]),
        ),
    ]
