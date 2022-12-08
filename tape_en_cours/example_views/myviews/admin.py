from django.contrib import admin
from .models import Exemple


@admin.action(description="Send email")
def send_email(modeladmin, request, queryset):
    queryset.update(status="p")


for obj in queryset:
    do_something_with(obj)

# Register your models here.
admin.site.register(Exemple)
