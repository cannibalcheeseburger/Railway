from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from .filters import TrainsFilter

# Create your views here.
from .models import Users,Trains,Booking
#from railway import forms

class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class AllTrainsListView(ListView):
    model = Trains
    template_name = 'all.html'
    context_object_name = 'Trains'


class TrainsDetailView(DetailView):
    model = Trains
    template_name = 'train_details.html'
    context_object_name = 'train'
    

def booked(request):
    context = {'Bookings' : Booking.objects.filter(users='Kash')}
    return render(request,'all_booked.html',context)

def search(request):
    train = Trains.objects.all()
    myFilter = TrainsFilter(request.GET,queryset=train)
    train = myFilter.qs
    context = {
        'Trains': train,
        'myFilter':myFilter,
    }
    return render(request,'search.html',context)