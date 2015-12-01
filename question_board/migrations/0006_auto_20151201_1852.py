# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_board', '0005_auto_20151201_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='id',
            field=models.AutoField(verbose_name='ID', default=1, auto_created=True, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vote',
            name='question',
            field=models.OneToOneField(related_name='question', to='question_board.Question'),
        ),
    ]
