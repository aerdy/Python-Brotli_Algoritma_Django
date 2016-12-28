from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200, default='-')
    date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='Test1/gambar', null=True, blank=True)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)