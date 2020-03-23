from django.contrib import admin
from .models import Run


class RunAdmin(admin.ModelAdmin):
    list_display = ['date', 'owner', 'description', 'distance', 'time']


admin.site.register(Run, RunAdmin)
