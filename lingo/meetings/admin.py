from django.contrib import admin
from .models import Meeting


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['language', 'user', 'time', 'meeting_url']
    list_filter = ['language', 'time']
    search_fields = ['user__username']
    autocomplete_fields = ['user']
