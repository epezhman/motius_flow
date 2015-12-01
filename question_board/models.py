from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    def get_questions_for_user(self, user):
        return super(QuestionManager, self).get_queryset().filter(created_by_id=user.id)


class Question(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    created_by = models.ForeignKey(User, verbose_name="user_questions")
    created_at = models.DateTimeField(auto_now_add=True)

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    body = models.TextField()
    created_by = models.ForeignKey(User, verbose_name="user_answers")
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
