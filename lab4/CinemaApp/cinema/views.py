from django.shortcuts import render, HttpResponseRedirect
from cinema.models import Film, FilmCategory, Session, Seat, Ticket
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import FilmSearchForm

# Create your views here.
def index(request, category_id=0):
    Film.objects.get_all_empty_movies()
    form = FilmSearchForm(request.GET)
    sort_by = request.GET.get('sort', None)
    reset_filter = request.GET.get('reset', None)
    
    if category_id:
        category = FilmCategory.objects.get(id=category_id)
        films = Film.objects.filter(category=category)
    else:
        films = Film.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        films = films.filter(name__icontains=search_query)

    if sort_by == 'release':
        films = films.order_by('-release')
    elif sort_by == 'rating':
        films = films.order_by('-rating')

    if reset_filter:
        # Сбросить фильтр, показать все фильмы
        films = Film.objects.all()
    
    context = {
        'title': 'Mycinema - Главная',
        'categories': FilmCategory.objects.order_by('number'),
        'films': films,
        'form': form,
    }
    return render(request, 'cinema/index.html', context)

def sessions(request, film_id):
    film = Film.objects.get(id=film_id)
    sessions = Session.objects.filter(movie=film).order_by('date', 'time')
    treiler_id = film.get_treiler_id()
    
    context = {
        'title': 'Mycinema - Сеансы',
        'sessions': sessions,
        'film': film,
        'treiler_id': treiler_id,
    }
    return render(request, 'cinema/sessions.html', context)

@login_required
def order(request, session_id):
    session = Session.objects.get(id=session_id)
    context = {
        'title': 'Mycinema - Сеансы',
        'unavailable_seats': Seat.objects.filter(session=session, is_available = False),
        'session': session,
        'rows': range(1, session.hall.rows + 1),
        'seats_in_a_row': range(1, session.hall.seats_in_a_row + 1)
        }
    
    if request.method == 'POST':
        selected_seat = request.POST['selected_seats']
        seat_row = selected_seat.split(' ')[0]
        seat_in_a_row = selected_seat.split(' ')[1]
        
        seat = Seat.objects.get(session = session, row = seat_row, seat_in_a_row = seat_in_a_row)
        if seat.is_available == False:
            return render(request, 'cinema/order.html', context)
        seat.is_available = False
        seat.save()
        
        ticket = Ticket()
        ticket.session = session
        ticket.seat = seat
        ticket.user = request.user
        ticket.save()
        return HttpResponseRedirect('/')
    else:
        if session.is_seats_empty:
            session.create_seats()            
            
    return render(request, 'cinema/order.html', context)


def stats(request):
    Film.objects.get_stats()
    films = Film.objects.all()
    context = {
        'title': 'Mycinema - Сеансы',
        'films': films,
    }
    return render(request, 'cinema/stats.html', context)

    