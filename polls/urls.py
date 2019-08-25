from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render
from .views import question_view, quiz_home, result_view


app_name = 'polls'
urlpatterns = [
    # quiz_home which will have the link to attempt all the quizzes
    path('', quiz_home, name="quiz_home"),

    # page to attempt a given quiz
    path('quiz<int:quiz_id>/', question_view, name="any_quiz"),

    # results of a given quiz to be shown once the user has attempted the quiz
    path('quiz<int:quiz_id>/results/', result_view, name="results")
]
