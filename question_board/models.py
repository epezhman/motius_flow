from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    created_by = models.ForeignKey(User, verbose_name="user_questions")
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    body = models.TextField()
    created_by = models.ForeignKey(User, verbose_name="user_answers")
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
