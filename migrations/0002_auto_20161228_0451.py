# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Test1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(null=True, upload_to=b'Test1/gambar', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=b'-', max_length=200),
        ),
    ]
