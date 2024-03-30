from django.urls import path

from core.quiz.views import get_quiz

app_name = "quiz"

urlpatterns = [
    path("<str:quiz_id>/", get_quiz, name="get_quiz"),
]
