from django.contrib import admin
from .models import Exemple


@admin.action(description="Send email")
def send_email(modeladmin, request, queryset):
    for obj in queryset:
        obj.send_email()


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    ordering = ["title"]
    actions = [make_published]


# Register your models here.
admin.site.register(Exemple)
