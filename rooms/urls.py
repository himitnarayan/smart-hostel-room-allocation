from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('add/', views.add_room, name='add_room'),
    path('search/', views.search_room_view, name='search_room'),
    path('allocate/', views.allocate_room_view, name='allocate_room'),
]