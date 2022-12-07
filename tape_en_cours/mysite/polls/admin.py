from django.contrib import admin

from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
