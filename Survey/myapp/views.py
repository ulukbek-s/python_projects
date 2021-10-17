from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Quizzes, Question
from .serialziers import QuizSerializer, QuestionSerializer


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class QuizQuestions(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)


