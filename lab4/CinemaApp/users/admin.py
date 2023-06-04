from django.contrib import admin
from users.models import User
from cinema.admin import TicketInline


@admin.register(User)   
class SessionAdmin(admin.ModelAdmin):
    inlines = [TicketInline]