from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import  generics,viewsets,permissions
from .serializers import MenuSerializers,UserSerializers,BookingSerializers
from .models import Menu,Booking
from .form import BookingForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django import http
# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 


@csrf_exempt
def book(request):
    if request.method == 'POST':
        
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Thanks for Reservation")
            return http.HttpResponseRedirect('/restaurant/book/')
            # return redirect('success_page')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = BookingForm()
    context = {'form': form}
    return render(request, 'book.html', context)

class UserView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
class MenuView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class Single_Menu_View(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers 
    
# class BookingcreateView(CreateView):
#     model = Booking
#     form_class = BookingForm
#     template_name = 'book.html'
#     success_url = reverse_lazy('success_page')
    