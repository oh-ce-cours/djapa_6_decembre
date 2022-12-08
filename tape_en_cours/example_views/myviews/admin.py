from django.contrib import admin
from .models import Exemple

for obj in queryset:
    do_something_with(obj)

# Register your models here.
admin.site.register(Exemple)
