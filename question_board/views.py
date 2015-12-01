from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from question_board.forms import QuestionForm, AnswerForm
from question_board.models import Question, Answer, Vote


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


@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if not hasattr(question, 'vote'):
        vote = Vote(question=question, up_vote=0, down_vote=0)
        vote.save()
    return render(request, 'question_board/question_detail.html', {'question': question})


@login_required
def question_up_vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    vote = question.vote
    vote.up_vote += 1
    vote.save()
    return redirect('question_detail', pk=pk)


@login_required
def question_down_vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    vote = question.vote
    vote.down_vote += 1
    vote.save()
    return redirect('question_detail', pk=pk)
