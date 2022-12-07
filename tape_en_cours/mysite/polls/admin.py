from django.contrib import admin

from .models import Question, Choice

from django.db.models.functions import Lower
from django.db.models.functions import ExtractYear


class SearchByYear(admin.SimpleListFilter):
    title = "title"
    parameter_name = "year"

    def lookups(self, request, model_admin):
        year_list = (
            Question.objects.annotate(y=ExtractYear("pub_date"))
            .order_by("y")
            .values_list("y", flat=True)
            .distinct()
        )
        return [(str(y), (str(y))) for y in year_list]

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(pub_date__year=self.value())
        return queryset


class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        order_by = ["pub_date"]

    list_display = ("question_text", "pub_date")
    list_filter = ("pub_date", SearchByYear)
    date_hierarchy = "pub_date"


class ChoiceAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "question":
            formfield.queryset = Question.objects.order_by(Lower("question_text"))
        return formfield


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
