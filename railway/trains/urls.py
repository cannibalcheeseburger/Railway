from django.urls import path
from .views import HomeTemplateView, AllTrainsListView,booked,TrainsDetailView
from .views import search


urlpatterns = [
    path('',HomeTemplateView.as_view(),name = 'home'),
    path('all/',AllTrainsListView.as_view(),name = 'all_trains'),
    path('all_booked/',booked,name = 'all_booked'),
    path('trains/<int:pk>',TrainsDetailView.as_view(),name ='trains'),
    path('search/',search,name='search')
]
