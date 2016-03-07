# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160307_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='public_key',
            field=models.TextField(),
        ),
    ]
