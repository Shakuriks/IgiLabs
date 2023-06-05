from django.db import models
from django.core.validators import MaxValueValidator
import requests
from users.models import User
from django.conf import settings
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
import logging


class FilmCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    number = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class FilmQuerrySet(models.QuerySet):
    def get_all_empty_movies(self):
        for film in self.filter(is_empty = True):
            data = film.get_movie()
            if not data[4]:
                film.save_movie(data)
            
    def get_stats(self):
        for film in self:
            sessions = Session.objects.filter(movie=film)
            film.sessions_count = sessions.count()
            sessions_prices = []
            for session in sessions:
                sessions_prices.append(session.price)
            if sessions.count() != 0:    
                film.avg_price = sum(sessions_prices)/sessions.count()
            else:
                film.avg_price = 0
            total_tickets_sold = 0
            total_price = 0
            for session in sessions:
                tickets = Ticket.objects.filter(session=session)
                total_tickets_sold += tickets.count()
                session_price = total_tickets_sold * session.price
                total_price += session_price
                
            film.total_tickets_sold = total_tickets_sold  
            film.total_price = total_price
            film.save()
            
            


class Film(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    release = models.PositiveIntegerField(null=True, blank=True)
    category = models.ForeignKey(to=FilmCategory, on_delete=models.PROTECT)
    rating = models.DecimalField(max_digits=2, decimal_places=1,
                                 null=True, blank=True, validators=[MaxValueValidator(10)])
    poster = models.ImageField(null=True, blank=True)
    is_empty = models.BooleanField(default=True)
    sessions_count = models.PositiveIntegerField(null=True, blank=True)
    avg_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_tickets_sold = models.PositiveIntegerField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    
    objects = FilmQuerrySet.as_manager()

    def get_treiler_id(self):
        logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
        api_service_name = "youtube"
        api_version = "v3"
        api_key = settings.YOUTUBE_DATA_API_KEY

        youtube = build(api_service_name, api_version, developerKey=api_key)

        try:
            search_response = youtube.search().list(
                q="Трейлер " + self.name,
                part="id",
                maxResults=1,
                type="video"
            ).execute()

            # Получение videoId первого найденного видео
            if "items" in search_response:
                video_id = search_response["items"][0]["id"]["videoId"]
                logging.debug(video_id)
                return video_id
        except HttpError as e:
            print("An error occurred:", e)

        return None

    def get_movie(self):
        logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
        api_key = settings.TMDB_API_KEY  # Замените на свой API-ключ
        movie_title = self.name  # Название фильма, которое вы хотите найти
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=ru-RU&query={movie_title}"
        logging.debug(url)
        response = requests.get(url)
        if response.status_code == 200:
            search_results = response.json()
            failed = True
            if len(search_results['results']) != 0:
                description = search_results['results'][0]['overview']
                rating = search_results['results'][0]['vote_average']
                release = search_results['results'][0]['release_date'][:4]
                poster = search_results['results'][0]['poster_path']
                failed = False
            else:
                description = ""
                rating = 0
                release = 1111
                poster = ""
            return description, rating, release, poster, failed
        else:
            raise Exception("No film found!")


    def save_movie(self, data):
        logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
        base_url = "https://image.tmdb.org/t/p/w500"
        url = f'{base_url}{data[3]}'
        logging.debug(url)
        Film.objects.filter(id=self.id).update(
            description=data[0], rating=data[1], release=data[2], poster=url, is_empty=False)

    def __str__(self) -> str:
        return self.name


class Hall(models.Model):
    number = models.PositiveIntegerField()
    rows = models.PositiveIntegerField()
    seats_in_a_row = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.number}"


class Session(models.Model):
    date = models.DateField()
    time = models.TimeField()
    hall = models.ForeignKey(to=Hall, on_delete=models.PROTECT)
    movie = models.ForeignKey(to=Film, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_seats_empty = models.BooleanField(default=True)
    
    def check_session_date(self):
        if datetime.datetime.combine(self.date, self.time) < datetime.datetime.now():
            return False
        return True
    
    def create_seats(self):
        logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
        rows = self.hall.rows
        seats_in_a_row = self.hall.seats_in_a_row
        
        logging.debug(rows)
        logging.debug(seats_in_a_row)
        
        for row in range(1, rows + 1):
            for seat_in_a_row in range(1, seats_in_a_row + 1):
                seat = Seat()
                seat.row = row
                seat.seat_in_a_row = seat_in_a_row
                seat.session = self
                seat.save()
                
                
            
        self.is_seats_empty = False
        self.save()
    
    def __str__(self) -> str:
        return f"{self.date}"


class Seat(models.Model):
    row = models.PositiveIntegerField()
    seat_in_a_row = models.PositiveIntegerField()
    session = models.ForeignKey(to=Session, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    
class Ticket(models.Model):
    seat = models.OneToOneField(to=Seat, on_delete=models.CASCADE, null=True, blank=True)
    session = models.ForeignKey(to=Session, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    
