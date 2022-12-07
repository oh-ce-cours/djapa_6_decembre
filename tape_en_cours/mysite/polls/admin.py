from django.contrib import admin

from .models import Question, Choice


from django.db.models.functions import ExtractYear


class SearchByYear(admin.SimpleListFilter):
    title = _("title")
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
            return queryset.filter(date__year=self.value())
        return queryset


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date")
    list_filter = ("pub_date", SearchByYear)
    date_hierarchy = "pub_date"


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
