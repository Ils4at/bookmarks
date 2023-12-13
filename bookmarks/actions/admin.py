from django.contrib import admin
from .models import Action


@admin.register(Action)
class AdminAction(admin.ModelAdmin):
    list_display = ['user', 'verb', 'target', 'created']
    list_filter = ['created']
    list_fields = ['verb']
