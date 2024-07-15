from django.contrib import admin
from .models import Quiz, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  # Number of empty answer fields to display

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of empty question fields to display
    inlines = [AnswerInline]  # Nesting AnswerInline within QuestionInline

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
