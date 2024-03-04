from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Category, Question, Answer, Result


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'question_count']
    search_fields = ['name']

    def question_count(self, obj):
        return obj.question_set.count()

    question_count.short_description = 'Number of questions'


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_correct']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'category']
    list_display = ['name', 'category', ]
    inlines = [AnswerInlineModel]
    list_filter = ['category']
    search_fields = ['name', 'category__name']
    inlines = [AnswerInlineModel]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_correct', 'question']


@admin.action()
def selected_zero(modeladmin, request, queryset):
    queryset.update(score=0)


@admin.register(Result)
class ResultAdmin(ImportExportModelAdmin):
    list_display = ['user', 'category', 'total_question', 'total_correct', 'score', 'is_passed']
    list_filter = ['user', 'category']
    search_fields = ['user__phone', 'category__name']
    actions = [selected_zero]
