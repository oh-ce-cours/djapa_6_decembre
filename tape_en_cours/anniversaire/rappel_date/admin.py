from django.contrib import admin
from .models import Exemple


@admin.action(description="Send email")
def send_email(modeladmin, request, queryset):
    for obj in queryset:
        obj.send_email()


class ExempleAdmin(admin.ModelAdmin):
    actions = [send_email]


# Register your models here.
admin.site.register(Exemple, ExempleAdmin)
