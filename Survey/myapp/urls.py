from django.urls import path
from .views import Quiz, QuizQuestions

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('q/<str:topic>/', QuizQuestions.as_view(), name='questions'),
]
