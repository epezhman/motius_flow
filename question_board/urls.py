from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new_question/$', views.new_question, name="new_question"),
    url(r'^new_answer/$', views.new_answer, name="new_answer"),

]
