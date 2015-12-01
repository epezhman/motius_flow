# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_board', '0002_auto_20151201_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('up_vote', models.IntegerField(verbose_name='Up Vote')),
                ('down_vote', models.IntegerField(verbose_name='Down Vote')),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(verbose_name='Answer Body'),
        ),
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(help_text='Describe your question more.', verbose_name='Question Body'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Question Title'),
        ),
        migrations.AddField(
            model_name='vote',
            name='question',
            field=models.ForeignKey(to='question_board.Question'),
        ),
    ]
