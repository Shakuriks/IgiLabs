from django.contrib import admin
from cinema.models import FilmCategory, Film, Session, Hall, Seat, Ticket


class FilmInline(admin.TabularInline):
    model = Film    
    extra = 0

@admin.register(FilmCategory)
class FilmCategoryAdmin(admin.ModelAdmin):
    list_filter = [('name')]
    inlines = [FilmInline]

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_filter = ('name', 'release', 'rating')





class SeatInline(admin.TabularInline):
    model = Seat    
    extra = 0    

@admin.register(Session)   
class SessionAdmin(admin.ModelAdmin):
    list_filter = [('date')]
    list_display = ('date', 'time')
    inlines = [SeatInline]
    
@admin.register(Ticket)   
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'seat')
    
class TicketInline(admin.TabularInline):
    model = Ticket    
    extra = 0   
    
@admin.register(Hall)   
class HallAdmin(admin.ModelAdmin):
    list_filter = [('number')]
    
@admin.register(Seat)   
class SeatAdmin(admin.ModelAdmin):
    list_filter = [('session')]
    