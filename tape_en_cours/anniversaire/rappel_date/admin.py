from django.contrib import admin
from .models import Anniversaire, Notification


@admin.action(description="Send email")
def send_email(modeladmin, request, queryset):
    for obj in queryset:
        obj.send_email()


class AnniversaireAdmin(admin.ModelAdmin):
    actions = [send_email]


# Register your models here.
admin.site.register(Anniversaire, AnniversaireAdmin)
admin.site.register(Notification)
