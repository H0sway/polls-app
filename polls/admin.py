from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.StackedInLine):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date Information',    {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
