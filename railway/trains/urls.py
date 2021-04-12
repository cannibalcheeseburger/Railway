from django.urls import path
from .views import HomeTemplateView, AllTrainsListView,Bookings,TrainsDetailView,LogoutUserView
from .views import search,register_page,login_page


urlpatterns = [
    path('',HomeTemplateView.as_view(),name = 'home'),
    path('all/',AllTrainsListView.as_view(),name = 'all_trains'),
    path('all_booked/',Bookings.as_view(),name = 'all_booked'),
    path('trains/<int:pk>',TrainsDetailView.as_view(),name ='trains'),
    path('search/',search,name='search'),
    path('register/',register_page,name='register'),
    path('login/',login_page,name='login'),
    path('logout/',LogoutUserView.as_view(),name='logout')

]
