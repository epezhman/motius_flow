from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from question_board.forms import QuestionForm, AnswerForm
from question_board.models import Question, Answer


@login_required
def new_question(request):
    if request.method == 'POST':
        question = Question(created_by=request.user)
        form = QuestionForm(data=request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    else:
        form = QuestionForm()

    return render(request, 'question_board/new_question_answer.html', {'form': form})


@login_required
def new_answer(request):
    if request.method == 'POST':
        answer = Answer(created_by=request.user)
        form = AnswerForm(data=request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    else:
        form = AnswerForm()

    return render(request, 'question_board/new_question_answer.html', {'form': form})