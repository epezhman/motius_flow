from django.contrib import admin
from .models import Question, Answer, Vote


class InlineAnswer(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'created_at']
    search_fields = ['title', 'body']
    inlines = [InlineAnswer]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer)

admin.site.register(Vote)
