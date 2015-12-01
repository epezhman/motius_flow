from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class QuestionManager(models.Manager):
    def get_questions_for_user(self, user):
        return super(QuestionManager, self).get_queryset().filter(created_by_id=user.id)


class Question(models.Model):
    title = models.CharField("Question Title", max_length=500)
    body = models.TextField("Question Body", help_text="Describe your question more.")
    created_by = models.ForeignKey(User, verbose_name="user_questions")
    created_at = models.DateTimeField(auto_now_add=True)

    objects = QuestionManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})


class Answer(models.Model):
    question = models.ForeignKey(Question)
    body = models.TextField("Answer Body", )
    created_by = models.ForeignKey(User, verbose_name="user_answers")
    created_at = models.DateTimeField(auto_now_add=True)


class Vote(models.Model):
    question = models.OneToOneField(Question,)
    up_vote = models.IntegerField("Up Vote")
    down_vote = models.IntegerField("Down Vote")

    def get_vote_sum(self):
        return self.up_vote - self.down_vote
