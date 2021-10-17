from rest_framework import serializers

from .models import Quizzes, Question, Text_Answer, Multiplechoice_Answer


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Multiplechoice_Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class TextAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Text_Answer
        fields = [
            'id',
            'answer_text',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    multiplechoice_answer = MultipleChoiceAnswerSerializer(many=True, read_only=True)
    text_answer = TextAnswerSerializer(many=True, write_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = [
            'quiz', 'title', 'multiplechoice_answer', 'text_answer',
        ]
