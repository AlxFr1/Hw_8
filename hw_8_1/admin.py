from django.contrib import admin
from hw_8_1.models import LogRequest


@admin.register(LogRequest)
class LoginRequestAdmin(admin.ModelAdmin):
    list_display = ['path', 'method', 'timestamp']
