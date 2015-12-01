# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_board', '0006_auto_20151201_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='question',
            field=models.OneToOneField(to='question_board.Question'),
        ),
    ]
