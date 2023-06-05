from django.urls import path, re_path
from . import views

app_name = 'cinema'

urlpatterns = [
    path('<int:category_id>/', views.index, name='index'),
    path('', views.index, name='index'),
    path('sessions/<int:film_id>/', views.sessions,name='sessions'),
    path('order/<int:session_id>/', views.order,name='order'),
    path('stats/', views.stats,name='stats'),
    path('edit/', views.edit,name='edit'),
]
