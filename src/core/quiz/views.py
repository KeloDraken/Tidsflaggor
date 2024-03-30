from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def get_quiz(request: HttpRequest, quiz_id: str) -> HttpResponse:
    return render(request, "quizzes/quiz.html", {"quiz_id": quiz_id})
