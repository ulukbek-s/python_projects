from django.contrib import admin

from . import models


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]


class MultipleChoiceAnswerInlineModel(admin.TabularInline):
    model = models.Multiplechoice_Answer
    fields = ['answer_text', 'is_right', ]


class TextAnswerInlineModel(admin.TabularInline):
    model = models.Text_Answer
    fields = ['answer_text', ]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'quiz', 'is_active', 'multiple_answers', ]
    list_display = ['title', 'quiz', 'date_updated', ]
    inlines = [
        MultipleChoiceAnswerInlineModel,
        TextAnswerInlineModel,
    ]


@admin.register(models.Multiplechoice_Answer)
class MultipleChoiceAnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_right', 'question', ]


@admin.register(models.Text_Answer)
class TextAnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'question', ]
