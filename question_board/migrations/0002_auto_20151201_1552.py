# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('question_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user_answers'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user_questions'),
        ),
    ]
