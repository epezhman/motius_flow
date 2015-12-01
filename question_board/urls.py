from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^question/(?P<pk>\d+)/$', views.question_detail, name="question_detail"),
    url(r'^up_vote/(?P<pk>\d+)/$', views.question_up_vote, name="question_up_vote"),
    url(r'^down_vote/(?P<pk>\d+)/$', views.question_down_vote, name="question_down_vote"),
    url(r'^new_question/$', views.new_question, name="new_question"),
    url(r'^new_answer/$', views.new_answer, name="new_answer"),

]
