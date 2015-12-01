from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from question_board.models import Question


@login_required
def home(request):
    questions = Question.objects.get_questions_for_user(request.user)
    return render(request, 'user/home.html', {'questions': questions})
