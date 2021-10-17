from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Quizzes(models.Model):
    title = models.CharField(max_length=255, default=_('New Quiz'), verbose_name=_('Quiz Title'))
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ['id']


class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_('Last Update'), auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    is_active = models.BooleanField(default=False, verbose_name=_('Active_Status'))
    multiple_answers = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']


class Multiplechoice_Answer(Updated):
    question = models.ForeignKey(Question, related_name='choice_answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_('choice_Text'))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = _('MultipleChoice_Answer')
        verbose_name_plural = _('MultipleChoice_Answers')
        ordering = ['id']


class Text_Answer(Updated):
    question = models.ForeignKey(Question, related_name='text_answer', on_delete=models.DO_NOTHING)
    answer_text = models.TextField(verbose_name=_('Answer_Text'))

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = _('Text_Answer')
        verbose_name_plural = _('Text_Answers')
        ordering = ['id']
