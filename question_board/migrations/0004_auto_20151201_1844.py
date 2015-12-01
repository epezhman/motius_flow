# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_board', '0003_auto_20151201_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='question',
            field=models.OneToOneField(related_name='question', to='question_board.Question'),
        ),
    ]
