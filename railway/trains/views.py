from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView,View
from .filters import TrainsFilter
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login,logout
# Create your views here.
from .models import Users,Trains,Booking
from django.views.decorators.csrf import csrf_protect


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
    
def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')

    context = {'form':form}
    return render(request,'Register.html',context)

@csrf_protect
def login_page(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context = {}
    return render(request,'login.html',context)

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutUserView(View):
    def get(self,request):
        logout(request)
        return redirect('home')

def booked(request):
    context = {'Bookings' : Booking.objects.filter(users='Kash')}
    return render(request,'all_booked.html',context)

class Bookings(ListView):
    context_object_name='Bookings'
    template_name='all_booked.html'
    def get_queryset(self):
        return Booking.objects.filter(users = self.request.user.username)

def search(request):
    train = Trains.objects.all()
    myFilter = TrainsFilter(request.GET,queryset=train)
    train = myFilter.qs
    context = {
        'Trains': train,
        'myFilter':myFilter,
    }
    return render(request,'search.html',context)