from django.urls import path
from . import views

urlpatterns = [
    path('', views.places_list, name='places_list'),
    path('options/', views.place_options, name='place_options'),
    path('route/', views.route_page, name='route_page'),
    path('info/', views.place_info, name='place_info'),
    path('between/', views.places_between, name='places_between'),
    path('review/<int:place_id>/', views.add_review, name='add_review'),

    
]
