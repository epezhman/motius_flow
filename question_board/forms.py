from django.forms import ModelForm

from question_board.models import Question, Answer


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ['created_by',]


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ['created_by',]